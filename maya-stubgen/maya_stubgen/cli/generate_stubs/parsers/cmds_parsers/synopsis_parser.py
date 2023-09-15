from __future__ import annotations

import keyword
import logging
import re
from pathlib import Path

import docspec
from attrs import define
from maya import cmds

from ..common import NULL_LOCATION, Parser
from .common import mel_to_python_type

logger = logging.getLogger(__name__)

__all__ = [
    "SynopsisNotFound",
    "CmdsSynopsisParser",
]

#: Regex used to parse the header of a command's synopsis
#: https://regex101.com/r/9595nC/1
synopsis_header_regex = re.compile(
    r"Synopsis: (?P<name>\w+)( (\[flags\])? ?(?P<positional_args>.*))?"
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


@define
class CmdsSynopsisParser(Parser):
    def parse_package(self, name: str) -> list[docspec.Module]:
        return super().parse_package(name)

    def parse_module(self, name: str) -> docspec.Module:
        return super().parse_module(name)

    def parse_class(self, module_name: str, name: str) -> docspec.Class:
        return super().parse_class(module_name, name)

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

        if "Quick help is not available" in synopsis:
            arguments = [
                docspec.Argument(
                    NULL_LOCATION,
                    "*args",
                    docspec.Argument.Type.POSITIONAL_REMAINDER,
                    decorations=None,
                    datatype="Any",
                    default_value=None,
                ),
                docspec.Argument(
                    NULL_LOCATION,
                    "**kwargs",
                    docspec.Argument.Type.KEYWORD_REMAINDER,
                    decorations=None,
                    datatype="Any",
                    default_value=None,
                ),
            ]
        else:
            arguments: list[docspec.Argument] = []

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
        return super().parse_variable(module_name, name)

    def parse_flag(self, match_flag: re.Match) -> docspec.Argument:
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

        if "..." in positional_args:
            # the type is a list. Eg: [String...]
            # We'll convert that in `*args: str`

            # Remove any unwanted characters to get a clean type string
            positional_args = positional_args.replace("[", "").replace("]", "").strip()
            positional_args = positional_args.replace("...", "")

            return [
                docspec.Argument(
                    NULL_LOCATION,
                    "*args",
                    docspec.Argument.Type.POSITIONAL_REMAINDER,
                    decorations=None,
                    datatype=mel_to_python_type(positional_args),
                    default_value=None,
                )
            ]
        elif positional_args.count(" ") > 0:
            # the type is a tuple. Eg: [str, int, str]
            # This means we need a specific number of positional only arguments
            # each with the relevant type
            # we'll convert that to `arg0: str, arg1: int, arg2: str`

            # Remove any unwanted characters to get a clean "space" separated types string
            positional_args = positional_args.replace("[", "").replace("]", "").strip()

            out_args: list[docspec.Argument] = []
            for i, data_type in enumerate(positional_args.split(" ")):
                out_args.append(
                    docspec.Argument(
                        NULL_LOCATION,
                        f"arg{i}",
                        docspec.Argument.Type.POSITIONAL_ONLY,
                        decorations=None,
                        datatype=mel_to_python_type(data_type),
                        default_value=None,
                    )
                )
            return out_args
        else:
            # the type is a basic type
            return [
                docspec.Argument(
                    NULL_LOCATION,
                    "arg0",
                    docspec.Argument.Type.POSITIONAL_ONLY,
                    decorations=None,
                    datatype=mel_to_python_type(positional_args),
                    default_value=None,
                )
            ]

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
        cache_page = Path() / ".cache" / "synopsis" / f"{command_name}.txt"
        cache_page = cache_page.resolve()

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
