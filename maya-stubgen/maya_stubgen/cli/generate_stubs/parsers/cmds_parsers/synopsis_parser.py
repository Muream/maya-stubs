from __future__ import annotations

import keyword
import re

import docspec
from attrs import define
from maya import cmds

from ..... import _logging
from ..common import NULL_LOCATION, Parser
from .common import mel_to_python_type
from .....utils import cache_dir

logger = _logging.getLogger(__name__)

__all__ = [
    "SynopsisNotFound",
    "CmdsSynopsisParser",
]

#: Regex used to parse the header of a command's synopsis
#: https://regex101.com/r/9595nC/1
synopsis_header_regex = re.compile(
    r"Synopsis: (?P<name>\w+)( (\[flags\])? ?(?P<positional_args>.*))?"
)

# used to tokenize the arguments of the synopsis header
# https://regex101.com/r/65YWDk/1
synopsis_args_regex = re.compile(
    r"(?P<type>[\w+|]+)\[?(?P<repeat>\.\.\.)?\]?(?P<repeat2> \(up to \d+ times\))?"
)

#: Regex used to parse a flag line in the command's synopsis
#: https://regex101.com/r/bBZoCh/3
synopsis_flag_regex = re.compile(
    r"-(?P<short_name>\w+)\s+"
    r"-(?P<long_name>\w+)"
    r"(?P<types>[\w\|\s\[\].]+)?\s?"
    r"(?P<multi_use>\(multi-use\))?\s?"
    r"(\(Query Arg (?P<query_arg_mandatory>Mandatory|Optional)\))?"
)


class SynopsisNotFound(Exception):
    """Exception raised when the cmds synopsis is not found."""


@define
class CmdsSynopsisParser(Parser):
    def parse_package(self, name: str) -> list[docspec.Module]:
        raise NotImplementedError

    def parse_module(self, name: str) -> docspec.Module:
        raise NotImplementedError

    def parse_class(self, module_name: str, name: str) -> docspec.Class:
        raise NotImplementedError

    def parse_function(self, module_name: str, name: str) -> docspec.Function:
        """Return a docspec Function parsed from command's synopsis

        Args:
            name: The name of the command.

        Raises:
            SynopsisNotFound: when the synopsis isn't available

        Returns:
            The generated docspec Function
        """
        logger.debug("Parsing synopsis for: %s", name)

        try:
            synopsis = self.get_synopsis(name)
        except SynopsisNotFound as exc:
            # Explicitly re-raise the error
            raise exc from exc

        arguments: list[docspec.Argument] = []
        if "Quick help is not available" in synopsis:
            logger.warning(
                "Synopsis not available, using default arguments for function"
            )
            arguments = [
                docspec.Argument(
                    NULL_LOCATION,
                    "args",
                    docspec.Argument.Type.POSITIONAL_REMAINDER,
                    decorations=None,
                    datatype="Any",
                    default_value=None,
                ),
                docspec.Argument(
                    NULL_LOCATION,
                    "kwargs",
                    docspec.Argument.Type.KEYWORD_REMAINDER,
                    decorations=None,
                    datatype="Any",
                    default_value=None,
                ),
            ]
        else:
            for line in synopsis.splitlines():
                line = line.strip()

                match_header = synopsis_header_regex.match(line)
                if match_header:
                    arguments.extend(self.parse_header(match_header))
                    continue

                match_flag = synopsis_flag_regex.match(line)
                if match_flag:
                    argument = self.parse_flag(match_flag)
                    if argument not in arguments:
                        arguments.append(argument)
                    continue

        return docspec.Function(
            location=NULL_LOCATION,
            name=name,
            docstring=None,
            modifiers=[],
            args=arguments,
            return_type=None,
            decorations=None,
            semantic_hints=[],
        )

    def parse_variable(self, module_name: str, name: str) -> docspec.Variable:
        raise NotImplementedError

    def parse_flag(self, match_flag: re.Match[str]) -> docspec.Argument:
        """Generate a docstring Argument from a flag string."""

        long_name = match_flag["long_name"]
        short_name = match_flag["short_name"]

        if not long_name or long_name in keyword.kwlist:
            arg_name = short_name
        else:
            arg_name = long_name

        types = match_flag["types"]
        types = types.strip() if types else None
        if not types:
            # boolean flag if no type specified
            arg_type = "bool"
        elif " " in types:
            # multiple space-separated types; parse as tuple
            arg_type = mel_to_python_type(f"[{types}]")
        else:
            # single argument type
            arg_type = mel_to_python_type(types)

        if match_flag["multi_use"]:
            arg_type = f"Multiuse[{arg_type}]"

        return docspec.Argument(
            NULL_LOCATION,
            arg_name,
            docspec.Argument.Type.KEYWORD_ONLY,
            datatype=arg_type,
            default_value="...",
        )

    def parse_header(self, match_header: re.Match[str]) -> list[docspec.Argument]:
        positional_args = match_header["positional_args"]

        if not positional_args:
            return []

        positional_args = positional_args.strip()
        return_args: list[docspec.Argument] = []

        # arg list can look like:
        # String -> arg0: str
        # [String...] -> *args: str
        # String String [String...] -> arg0: str, arg1: str, *args: str
        # Float Float Float [String...] -> arg0: float, arg2: float, arg3: float, *args: str
        # [String String String String ] -> arg0: str, arg1: str, arg2: str, arg3: str
        # String Float Int String [String] (up to 6 times) -> arg0: str, arg1: float, arg2: int, arg3: str, *args: str

        for i, arg in enumerate(synopsis_args_regex.finditer(positional_args)):
            groups = arg.groupdict()
            datatype = mel_to_python_type(groups["type"])
            if groups.get("repeat") or groups.get("repeat2"):
                # *args
                return_args.append(
                    docspec.Argument(
                        location=NULL_LOCATION,
                        name="args",
                        type=docspec.Argument.Type.POSITIONAL_REMAINDER,
                        datatype=datatype,
                    )
                )
            else:
                # positional argument
                return_args.append(
                    docspec.Argument(
                        location=NULL_LOCATION,
                        name="arg{}".format(i),
                        type=docspec.Argument.Type.POSITIONAL_ONLY,
                        datatype=datatype,
                        default_value="...",
                    )
                )

        return return_args

    def get_synopsis(self, command_name: str) -> str:
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
        cache_page = cache_dir() / "synopsis" / f"{command_name}.txt"

        synopsis: str
        if not cache_page.exists():
            try:
                synopsis = cmds.help(command_name)  # type: ignore
            except RuntimeError as exc:
                # Explicitly raise a more specific error that is meant to be caught upstream.
                raise SynopsisNotFound(
                    f"Synopsis not found for {command_name}"
                ) from exc

            cache_page.parent.mkdir(parents=True, exist_ok=True)
            with cache_page.open("w", encoding="utf8") as f:
                f.write(synopsis.strip())

        logger.debug("Synopsis cache: %s", str(cache_page))
        synopsis = cache_page.read_text()

        return synopsis
