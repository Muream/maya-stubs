import inspect
import keyword
import logging
import re
from typing import *

import bs4
import requests
from maya import cmds

from .common import STUB_HEADER, Docstring, Function, Variable

logger = logging.getLogger(__name__)

cmds_documentation_url = (
    "https://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/{}.html"
)


def cmds_functions() -> List[Callable]:
    return inspect.getmembers(cmds, callable)


def function_from_synopsis(command: str) -> Function:
    """Returns a `Function` Object from the command's synopsis

    Args:
        command: the command to generate the Function from

    Raises:
        NameError: if the command doesn't exist or any other reason why
            `cmds.help` might fail.

    Returns:
        The Function.
    """
    try:
        synopsis = cmds.help(command)
    except RuntimeError as exc:
        raise NameError(exc) from exc

    if "No Flags" in synopsis:
        arguments = []
    elif "Quick help is not available" in synopsis:
        arguments = ["*args", "**kwargs"]
    else:
        arguments = []

        # https://regex101.com/r/9595nC/1
        header_regex = r"Synopsis: (?P<name>\w+)( \[flags\] ?(?P<positional_args>.*))?"

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

            match_flag = re.match(flag_regex, line)
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

    return Function(command, arguments, docstring=synopsis)


def function_from_documentation(command: str) -> Function:
    """Returns a `Function` object from the command's HTML documentation

    Args:
        command: the name of the command

    Returns:
        the Function with all the relevant data parsed from the doc.
    Raises:
        requests.exceptions.HTTPError: If there's any error with loading the page.
    """
    command_url = cmds_documentation_url.format(command)

    response = requests.get(command_url)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.content, "html.parser")

    arguments = []

    # The docstring is the only piece of text in the body that has no tag.
    body_text = [t.strip() for t in soup.body.findAll(text=True, recursive=False)]
    # filter the "," and "", that we get with the previous line.
    body_text = [t for t in body_text if len(t) > 1]
    description = "".join(body_text)

    docstring = Docstring(description)

    # for title in soup.find_all("h2"):
    #     title: bs4.element.Tag
    #     if title.text == "Synopsis":
    #         while True:
    #             tag = title.find_next()
    #         pass

    return Function(command, arguments, docstring)


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
    for command, _ in cmds_functions():
        if command != "createNode":
            continue

        if command[0].isupper():
            continue

        try:
            function = function_from_documentation(command)
        except requests.exceptions.HTTPError:
            try:
                function = function_from_synopsis(command)
            except NameError:
                function = Function(command, arguments=[])

        lines.append(function.stub)

    return STUB_HEADER.format(imports="") + "\n".join(lines)
