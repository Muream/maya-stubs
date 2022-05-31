import inspect
import keyword
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from textwrap import indent
from typing import *
from typing import Callable

import click

logger = logging.getLogger(__name__)

DEBUG = False


from maya import cmds


@dataclass
class Argument:
    long_name: str
    short_name: str
    type: Optional[Type] = None
    value: Optional[Any] = None

    def __post_init__(self):
        if self.long_name in keyword.kwlist:
            self.long_name = self.short_name
        elif self.short_name in keyword.kwlist:
            self.short_name = self.long_name
        # sometimes the long_name is empty, so we'll use the short_name for both
        elif self.long_name == "":
            self.long_name = self.short_name

    def __str__(self) -> str:
        res = self.long_name

        if self.type:
            res += f": {self.type}"

        if self.value:
            res += f" = {self.value}"

        return res


@dataclass
class Function:
    name: str
    arguments: List[Union[Argument, str]] = field(default_factory=list)
    docstring: Optional[str] = None
    return_type: Type = Any

    def __post_init__(self):
        self.docstring = self._process_docstring(self.docstring)

    @staticmethod
    def _process_docstring(docstring: Optional[str]) -> str:
        if docstring is None:
            return None

        docstring = docstring.strip()

        lines = docstring.splitlines()

        if len(lines) == 0:
            return None
        elif len(docstring.splitlines()) == 1:
            docstring = f'"""{docstring}"""'
        else:
            for i, line in enumerate(docstring.splitlines()):
                line = line.strip()
                if line.startswith("-"):
                    line = indent(line, 4 * " ")
                lines[i] = line

            if not lines[1] == "":
                lines.insert(1, "")

            docstring = "\n".join(lines)
            docstring = f'"""{docstring}\n"""'

        docstring = indent(docstring, 4 * " ")

        return docstring

    @property
    def arguments_str(self) -> str:
        return ", ".join(map(str, self.arguments))

    @property
    def return_type_str(self):
        return str(self.return_type).replace("typing.", "")

    @property
    def signature(self):
        signature = f"def {self.name}({self.arguments_str})"

        if self.return_type:
            signature += f" -> {self.return_type_str}"

        signature += ":"

        return signature

    @property
    def stub(self):
        stub = self.signature

        if self.docstring is not None and DEBUG:
            stub += "\n" + self.docstring
            stub += "\n    ..."
        else:
            stub += " ..."

        return stub

    def __str__(self) -> str:
        return self.stub


def cmds_functions() -> List[Callable]:

    return inspect.getmembers(cmds, callable)


def _args_from_help(synopsis: str) -> List[Argument]:
    if "No Flags" in synopsis:
        arguments = []
    elif "Quick help is not available" in synopsis:
        arguments = ["*args", "**kwargs"]
    else:
        arguments = []

        # https://regex101.com/r/9595nC/1
        header_regex = r"Synopsis: (?P<name>\w+)( \[flags\] ?(?P<implicit_args>.*))?"

        # https://regex101.com/r/bBZoCh/3
        flag_regex = (
            r"-(?P<short_name>\w+)\s+"
            r"-(?P<long_name>\w+)"
            r"(?P<types>[\w\|\s\[\]]+)?\s?"
            r"(?P<multi_use>\(multi-use\))?\s?"
            r"(\(Query Arg (?P<query_arg_mandatory>Mandatory|Optional)\))?"
        )

        for line in synopsis.splitlines():
            line = line.strip()

            match_header = re.match(header_regex, line)
            if match_header:
                implicit_args = match_header["implicit_args"]

                if not implicit_args:
                    continue

                implicit_args = implicit_args.strip()

                if "..." in implicit_args:
                    # the type is a list. Eg [String...]
                    implicit_args = implicit_args[1:-1].replace("...", "")
                    list_type = mel_to_python_type(implicit_args)
                    arg_type = f"List[{list_type}]"
                    arg_name = "*args"
                elif implicit_args.count(" ") > 0:
                    # the type is a tuple
                    implicit_args = implicit_args.replace("[", "").replace("]", "")
                    tuple_types = map(mel_to_python_type, implicit_args.split())
                    arg_type = f"Tuple[{', '.join(tuple_types)}]"
                    arg_name = "*args"
                else:
                    # the type is a basic type
                    arg_type = mel_to_python_type(implicit_args)
                    arg_name = "arg0"

                argument = Argument(arg_name, None, arg_type)
                arguments.append(argument)

                continue

            match_flag = re.match(flag_regex, line)
            if match_flag:
                long_name = match_flag["long_name"]
                short_name = match_flag["short_name"]

                # types can be either
                # - One type. eg: Float
                # - Multiple types. eg: Float String Int
                # - Union of types?. eg: [Float on|off]  # TODO: Unsupported
                # - None (when no type is specified).
                types = str(match_flag["types"]).split()
                types = [mel_to_python_type(t) for t in types]

                if len(types) == 1:
                    arg_type = types[0]
                else:
                    arg_type = f"Tuple[{', '.join(types)}]"

                multi_use = match_flag["multi_use"]
                if multi_use:
                    arg_type = f"List[{arg_type}]"

                argument = Argument(long_name, short_name, arg_type)
                if argument not in arguments:
                    arguments.append(argument)
                continue

    return arguments


def mel_to_python_type(type: str) -> str:
    """Transform the given MEL type to a python type

    Notes:
        None is converted to bool as an unnamed argument in mel is equivalent to a bool
        on|off is converted to bool
    """
    type_map = {
        # str
        "String": "str",
        "Name": "str",
        "Script": "Callable",
        # float
        "Float": "float",
        "Length": "float",
        "Angle": "float",
        # int
        "Int": "int",
        "Int64": "int",
        "UnsignedInt": "int",
        "Time": "int",
        # bool
        "": "bool",
        None: "bool",
        "None": "bool",
        "on|off": "bool",
    }
    return type_map.get(type, "Incomplete")


def generate_stubs_content() -> str:
    lines = [
        "from typing import *",
        "from _typeshed import Incomplete",
        "",
        "",
    ]

    for func, _ in cmds_functions():
        logger.debug("Generating signature for %s", func)
        try:
            help = cmds.help(func).strip("\n")
        except RuntimeError:
            help = ""

        args = _args_from_help(help)

        function = Function(func, arguments=args, docstring=help)
        lines.append(function.stub)

    return "\n".join(lines)


def write_stubs(stubs: str) -> None:
    stubs_path = Path(__file__).parent.parent / "maya-stubs" / "cmds" / "__init__.pyi"

    logger.debug("Writing stubs in %s", stubs_path)

    stubs_path.parent.mkdir(parents=True, exist_ok=True)

    with stubs_path.open("w") as f:
        f.write(stubs)

    return stubs_path


@click.command()
def generate_stubs() -> None:
    logger.info("Generating Stubs")

    try:
        stubs = generate_stubs_content()
        stubs_path = write_stubs(stubs)
    except BaseException as e:
        logger.error("Failed to generate stubs")
        raise e
    else:
        logger.success("Stubs generated in %s", stubs_path)
