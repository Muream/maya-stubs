import inspect
import keyword
import logging
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from textwrap import indent
from typing import *
from typing import Callable

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

DEBUG = False

if __name__ == "__main__":
    import maya.standalone

    try:
        logger.info("Initializing Maya Standalone.")
        maya.standalone.initialize()
    except BaseException:
        logger.info("Failed to initialize Maya Standalone.")
    else:
        logger.info("Initialized Maya Standalone Successfully.")


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


def _args_from_docstring(docstring: str) -> List[Argument]:
    if "No Flags" in docstring:
        arguments = []
    elif "Quick help is not available" in docstring:
        arguments = ["*args", "**kwargs"]
    else:
        arguments = []
        types_regex = (
            r"(\s+((?P<types>[\w\|]+( \w+)?)) ?(?P<multi_use>\(multi-use\))?)?$"
        )
        flag_regex = r"^-(?P<short_name>\w+)\s+-(?P<long_name>\S+)" + types_regex
        for line in docstring.splitlines():
            line = line.strip()
            match = re.match(flag_regex, line)
            if match:
                long_name = match["long_name"]
                short_name = match["short_name"]

                # types can be either
                # - One type. eg: Float
                # - Multiple types. eg: Float String Int
                # - None (when no type is specified).
                types = str(match["types"]).split()
                types = [mel_to_python_type(t) for t in types]

                if len(types) == 1:
                    type_ = types[0]
                else:
                    type_ = f"Tuple[{', '.join(types)}]"

                multi_use = match["multi_use"]
                if multi_use:
                    type_ = f"List[{type_}]"

                argument = Argument(long_name, short_name, type_)
                if argument not in arguments:
                    arguments.append(argument)

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
            docstring = cmds.help(func).strip("\n")
        except RuntimeError:
            docstring = ""

        args = _args_from_docstring(docstring)

        function = Function(func, arguments=args, docstring=docstring)
        lines.append(function.stub)

    return "\n".join(lines)


def write_stubs(stubs: str) -> None:
    stubs_path = Path(__file__).parent.parent / "maya-stubs" / "cmds" / "__init__.pyi"
    logger.debug("Writing stubs in %s", stubs_path)
    stubs_path.parent.mkdir(parents=True, exist_ok=True)

    with stubs_path.open("w") as f:
        f.write(stubs)


def generate_stubs() -> None:
    logger.info("Generating Stubs")

    stubs = generate_stubs_content()
    write_stubs(stubs)

    logger.info("Stubs Generated Successfully")


def main():
    global DEBUG
    DEBUG = "--debug" in sys.argv

    generate_stubs()


if __name__ == "__main__":
    main()

    import maya.standalone

    try:
        logger.info("Uninitializing Maya Standalone.")
        maya.standalone.uninitialize()
    except BaseException:
        logger.info("Failed to uninitialize Maya Standalone.")
    else:
        logger.info("Uninitialized Maya Standalone Successfully.")
