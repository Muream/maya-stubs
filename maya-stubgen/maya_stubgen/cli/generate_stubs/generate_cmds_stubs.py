import inspect
import keyword
import logging
import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import *

import bs4
import cchardet
import lxml
import requests
from maya import cmds

from .common import STUB_HEADER, DocstringBuilder, Function, Variable

logger = logging.getLogger(__name__)

cmds_documentation_url = (
    "https://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/{}.html"
)

# https://regex101.com/r/9595nC/1
synopsis_header_regex = re.compile(
    r"Synopsis: (?P<name>\w+)( \[flags\] ?(?P<positional_args>.*))?"
)

# https://regex101.com/r/bBZoCh/3
synopsis_flag_regex = re.compile(
    r"-(?P<short_name>\w+)\s+"
    r"-(?P<long_name>\w+)"
    r"(?P<types>[\w\|\s\[\]]+)?\s?"
    r"(?P<multi_use>\(multi-use\))?\s?"
    r"(\(Query Arg (?P<query_arg_mandatory>Mandatory|Optional)\))?"
)

#: Reusable request session to improve performance when
#: getting pages from the same domain
requests_session = requests.Session()


class Property(Enum):
    create = "create"
    query = "query"
    edit = "edit"
    multiuse = "multiuse"


@dataclass
class Flag(Variable):
    short_name: Optional[str] = None
    properties: List[Property] = field(default_factory=list)
    description: str = ""

    # A flag is always an argument
    is_argument: bool = field(default=True, init=False)

    def __post_init__(self) -> None:
        super().__post_init__()
        self.type = mel_to_python_type(self.type)

        self.description = self.description.replace("\\n\\0", "")
        self.description = self.description.strip()


@dataclass
class ReturnValue:
    type: Type = Any
    description: str = ""

    def __post_init__(self) -> None:
        self.type = mel_to_python_type(self.type)

    def __str__(self) -> str:
        return self.stub()

    def stub(self) -> str:
        return str(self.type).replace("typing.", "")


flag_name_re = r"(?P<long_name>\w+)\((?P<short_name>\w*)\)"


def function_from_synopsis(command: str, asdf: str) -> Function:
    """Returns a `Function` Object from the command's synopsis

    Args:
        command: the command to generate the Function from

    Raises:
        NameError: if the command doesn't exist or any other reason why
            `cmds.help` might fail.

    Returns:
        The Function.
    """
    logger.debug("Parsing synopsis for: %s", command)

    cache_page = Path() / ".cache" / "synopsis" / f"{command}.txt"
    cache_page = cache_page.resolve()
    if not cache_page.exists():

        try:
            synopsis = cmds.help(command)
        except RuntimeError as exc:
            raise NameError(exc) from exc

        cache_page.parent.mkdir(parents=True, exist_ok=True)
        with cache_page.open("w", encoding="utf8") as f:
            f.write(synopsis.strip())

    logger.debug("Synopsis cache: %s", str(cache_page))
    synopsis = cache_page.read_text()

    if "No Flags" in synopsis:
        arguments = []
    elif "Quick help is not available" in synopsis:
        arguments = ["*args", "**kwargs"]
    else:
        arguments = []

        for line in synopsis.splitlines():
            line = line.strip()

            match_header = synopsis_header_regex.match(line)
            if match_header:
                positional_args = match_header["positional_args"]

                if not positional_args:
                    continue

                positional_args = positional_args.strip()

                add_positional_arguments_separator = False
                if "..." in positional_args:
                    # the type is a list. Eg: [String...]
                    positional_args = positional_args[1:-1].replace("...", "")
                    list_type = mel_to_python_type(positional_args)
                    arg_type = f"List[{list_type}]"
                    arg_name = "*args"
                elif positional_args.count(" ") > 0:
                    # the type is a tuple
                    positional_args = positional_args.replace("[", "").replace("]", "")
                    tuple_types = map(mel_to_python_type, positional_args.split())
                    arg_type = f"Tuple[{', '.join(tuple_types)}]"
                    arg_name = "*args"
                else:
                    # the type is a basic type
                    arg_type = mel_to_python_type(positional_args)
                    arg_name = "arg0"
                    add_positional_arguments_separator = True

                argument = Variable(arg_name, arg_type)
                arguments.append(argument)

                if add_positional_arguments_separator:
                    arguments.extend(("/"))

                continue

            match_flag = synopsis_flag_regex.match(line)
            if match_flag:
                long_name = match_flag["long_name"]
                short_name = match_flag["short_name"]

                if not long_name or long_name in keyword.kwlist:
                    name = short_name
                else:
                    name = long_name

                # types can be either
                # - One type. eg: Float
                # - Multiple types. eg: Float String Int
                # - Union of types?. eg: [Float on|off]  # TODO: Unsupported
                # - None (when no type is specified).
                types = str(match_flag["types"]).split()
                types = [mel_to_python_type(t) for t in types]

                if len(types) == 0:
                    arg_type = "bool"
                elif len(types) == 1:
                    arg_type = types[0]
                else:
                    arg_type = f"Tuple[{', '.join(types)}]"

                multi_use = match_flag["multi_use"]
                if multi_use:
                    arg_type = f"List[{arg_type}]"

                argument = Variable(name, arg_type, is_argument=True)
                if argument not in arguments:
                    arguments.append(argument)
                continue

    return Function(command, arguments)


def function_from_documentation(command: str) -> Function:
    """Returns a `Function` object from the command's HTML documentation

    Args:
        command: the name of the command

    Returns:
        the Function with all the relevant data parsed from the doc.
    """
    logger.debug("Scraping docs for: %s", command)

    cache_page = Path() / ".cache" / "docs" / "maya" / "cmds" / f"{command}.html"
    cache_page = cache_page.resolve()
    if not cache_page.exists():
        command_url = cmds_documentation_url.format(command)

        response = requests_session.get(command_url)
        response.raise_for_status()

        cache_page.parent.mkdir(parents=True, exist_ok=True)
        with cache_page.open("w", encoding="utf8") as f:
            f.write(response.text)

    logger.debug("Documentation cache: %s", str(cache_page))
    soup = bs4.BeautifulSoup(cache_page.read_text(), "lxml")

    flags = []
    return_value = ReturnValue("Any")
    return_description = ""
    examples = ""
    for title in soup.find_all("h2"):
        title: bs4.element.Tag
        if title.text == "Flags":
            # All the flags are stored in the first table after the Flags H2 Title.
            table = title.find_next("table")

            # each link in the table corresponds to a flag name
            flag_links = table.find_all("a")

            for link in flag_links:
                # We can now easily get the parent row of the link to get access
                flag_data_row: bs4.element.Tag = link.find_parent("tr")
                long_name = None
                short_name = None
                flag_type = None
                properties = None
                for i, child in enumerate(flag_data_row.findChildren("td")):
                    if i == 0:
                        # First column is the flag name
                        name = child.text.strip()
                        match = re.match(flag_name_re, name)
                        if match:
                            long_name = match["long_name"]
                            short_name = match["short_name"]
                    elif i == 1:
                        # Second column is the flag Type
                        flag_type = child.text.strip()
                    elif i == 2:
                        # Third column is the flag properties
                        properties = [
                            Property(img["alt"]) for img in child.find_all("img")
                        ]
                flag_description_row = flag_data_row.find_next_sibling("tr")
                flag_description = flag_description_row.text.strip()

                flag = Flag(
                    name=long_name,
                    type=flag_type,
                    short_name=short_name,
                    properties=properties,
                    description=flag_description,
                )
                flags.append(flag)

        if title.text == "Return value":
            next_tag: bs4.element.Tag = title.find_next_sibling()
            if next_tag.name == "table":
                first_return_type_row = next_tag.find("tr")
                return_type, return_description = [
                    t.text.strip() for t in first_return_type_row.find_all("td")
                ]
                return_value = ReturnValue(return_type, return_description)
            elif next_tag.name == "p":
                return_type = next_tag.text
                return_description = "\n".join(
                    [p.text for p in next_tag.find_next_siblings("p")]
                )
            return_value = ReturnValue(return_type, return_description)

        if title.text == "Python examples":
            examples = title.find_next("pre").text
            examples = examples.replace(
                "import maya.cmds as cmds", "from maya import cmds"
            )

    # The docstring is the only piece of text in the body that has no tag.
    body_text = [t.strip() for t in soup.body.findAll(text=True, recursive=False)]
    # filter the "," and "", that we get with the previous line.
    body_text = [t for t in body_text if len(t) > 1]
    description = "".join(body_text)

    docstring = DocstringBuilder(
        short_description=description,
        parameters=flags,
        returns=return_description,
        examples=examples,
    )

    return Function(command, flags, docstring, return_type=return_value)


def mel_to_python_type(type_name: str) -> str:
    """Transform the given MEL type to a python type

    Notes:
        None is converted to bool as an unnamed argument in mel is equivalent to a bool
        on|off is converted to bool
    """
    type_map = {
        # str
        "string": "str",
        "name": "str",
        "script": "Callable",
        # float
        "float": "float",
        "length": "float",
        "angle": "float",
        # int
        "int": "int",
        "int64": "int",
        "unsignedint": "int",
        "time": "int",
        # bool
        "": "bool",
        "boolean": "bool",
        None: "bool",
        "none": "bool",
        "on|off": "bool",
        "any": "Any",
    }

    class SequenceType(Enum):
        NONE = "None"
        LIST = "List"
        TUPLE = "Tuple"

    type_name = type_name.lower()

    array_regex = r"(?P<type>\w+)\[(?P<length>\d+)?\]"
    tuple_regex = r"\[(?P<types>(\w+(, )?)+)\]"

    match_array = re.match(array_regex, type_name)
    match_tuple = re.match(tuple_regex, type_name)

    if match_array:
        match_dict = match_array.groupdict()
        type_name = match_dict.get("type")
        length = int(match_dict.get("length") or 0)

        python_type = type_map.get(type_name, "Incomplete")
        if length:
            sequence_type = SequenceType.TUPLE
            python_type = ", ".join([python_type] * length)
        else:
            sequence_type = SequenceType.LIST
    elif match_tuple:
        match_dict = match_tuple.groupdict()
        types = match_dict["types"].split(", ")
        python_types = [type_map.get(t.lower(), "Incomplete") for t in types]
        python_type = ", ".join(python_types)
        sequence_type = SequenceType.TUPLE
    else:
        sequence_type = SequenceType.NONE
        python_type = type_map.get(type_name, "Incomplete")

    if sequence_type is not SequenceType.NONE:
        python_type = f"{sequence_type.value}[{python_type}]"

    return python_type


def load_plugins() -> None:
    """Load plugins that register maya commands."""
    logger.debug("Loading plugins that register maya commands")

    plugins = ["poseInterpolator.mll", "invertShape.mll"]

    for plugin in plugins:
        if not cmds.pluginInfo(plugin, query=True, loaded=True):
            try:
                cmds.loadPlugin(plugin)
            except RuntimeError as exc:
                logger.warning(exc)


def generate_cmds_stubs() -> str:
    """Generate stubs for maya.cmds

    Returns:
        stub source for maya.cmds
    """

    load_plugins()

    lines = []
    for command, _ in inspect.getmembers(cmds, callable):
        # if command != "createNode":
        #     continue

        if command[0].isupper():
            continue

        try:
            function = function_from_documentation(command)
        except requests.exceptions.HTTPError:
            logger.debug(
                "Couldn't find documentation for %s, falling back to parsing synopsis.",
                command,
            )
            try:
                function = function_from_synopsis(command)
            except NameError:
                function = Function(command, arguments=[])

        lines.append(function.stub)

    return STUB_HEADER.format(imports="") + "\n".join(lines)
