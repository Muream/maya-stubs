import keyword
import logging
import re
from difflib import Match
from pathlib import Path
from typing import Optional

from docspec import Argument, Function
from maya import cmds

from ..common import NULL_LOCATION
from .common import mel_to_python_type

logger = logging.getLogger(__name__)

__all__ = [
    "SynopsisNotFound",
    "function_from_synopsis",
]

#: Regex used to parse the header of a command's synopsis
#: https://regex101.com/r/9595nC/1
synopsis_header_regex = re.compile(
    r"Synopsis: (?P<name>\w+)( \[flags\] ?(?P<positional_args>.*))?"
)

#: Regex used to parse a flag line in the command's synopsis
#: https://regex101.com/r/bBZoCh/3
synopsis_flag_regex = re.compile(
    r"-(?P<short_name>\w+)\s+"
    r"-(?P<long_name>\w+)"
    r"(?P<types>[\w\|\s\[\]]+)?\s?"
    r"(?P<multi_use>\(multi-use\))?\s?"
    r"(\(Query Arg (?P<query_arg_mandatory>Mandatory|Optional)\))?"
)


class SynopsisNotFound(Exception):
    """Exception raised when the cmds synopsis is not found."""


def function_from_synopsis(command_name: str) -> Function:
    """Return a docspec Function parsed from command's synopsis

    Args:
        command_name: The name of the command.

    Raises:
        SynopsisNotFound: when the synopsis isn't available

    Returns:
        The generated docspec Function
    """
    logger.debug("Parsing synopsis for: %s", command_name)

    try:
        synopsis = get_synopsis(command_name)
    except SynopsisNotFound as exc:
        # Explicitly re-raise the error
        raise exc from exc

    if "No Flags" in synopsis:
        arguments = []
    elif "Quick help is not available" in synopsis:
        arguments = [
            Argument(
                NULL_LOCATION,
                "*args",
                Argument.Type.POSITIONAL_REMAINDER,
                decorations=None,
                datatype="Any",
                default_value=None,
            ),
            Argument(
                NULL_LOCATION,
                "**kwargs",
                Argument.Type.KEYWORD_REMAINDER,
                decorations=None,
                datatype="Any",
                default_value=None,
            ),
        ]
    else:
        arguments = []

        for line in synopsis.splitlines():
            line = line.strip()

            match_header = synopsis_header_regex.match(line)
            if match_header:
                argument = parse_header(match_header)
                if argument is not None:
                    arguments.append(argument)
                continue

            match_flag = synopsis_flag_regex.match(line)
            if match_flag:
                argument = parse_flag(match_flag)
                if argument not in arguments:
                    arguments.append(argument)
                continue

    return Function(
        location=NULL_LOCATION,
        name=command_name,
        docstring=None,
        modifiers=[],
        args=arguments,
        return_type=None,
        decorations=None,
        semantic_hints=[],
    )


def parse_flag(match_flag: re.Match) -> Argument:
    """Generate a docstring Argument from a flag string."""

    long_name = match_flag["long_name"]
    short_name = match_flag["short_name"]

    if not long_name or long_name in keyword.kwlist:
        arg_name = short_name
    else:
        arg_name = long_name

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

    return Argument(
        location=NULL_LOCATION,
        name=arg_name,
        type=Argument.Type.KEYWORD_ONLY,
        datatype=arg_type,
        default_value="...",
    )


def parse_header(match_header: re.Match) -> Optional[Argument]:

    positional_args = match_header["positional_args"]

    if not positional_args:
        return

    positional_args = positional_args.strip()

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

    return Argument(
        location=NULL_LOCATION,
        name=arg_name,
        type=Argument.Type.POSITIONAL_ONLY,
        datatype=arg_type,
        default_value=None,
    )


def get_synopsis(command_name: str) -> str:
    """Get the synopsis for the given command

    This tries to find a cached synopsis first as cmds.help() is pretty slow.
    If not found, it gets the synopsis from cmds.help() and caches it.

    Args:
        command_name: The command to get the synopsis for.

    Raises:
        SynopsisNotFound: when the synopsis isn't available

    Returns:
        The synopsis for the command.
    """
    cache_page = Path() / ".cache" / "synopsis" / f"{command_name}.txt"
    cache_page = cache_page.resolve()

    if not cache_page.exists():
        try:
            synopsis = cmds.help(command_name)
        except RuntimeError as exc:
            # Explicitly raise a more specific error that is meant to be caught upstream.
            raise SynopsisNotFound(f"Synopsis not found for {command_name}") from exc

        cache_page.parent.mkdir(parents=True, exist_ok=True)
        with cache_page.open("w", encoding="utf8") as f:
            f.write(synopsis.strip())

    logger.debug("Synopsis cache: %s", str(cache_page))
    synopsis = cache_page.read_text()

    return synopsis
