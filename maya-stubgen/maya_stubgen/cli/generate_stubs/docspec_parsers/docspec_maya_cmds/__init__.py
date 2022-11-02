import concurrent.futures
import inspect
import logging
from pkgutil import ModuleInfo
from typing import Optional

from docspec import Argument, Function, Module
from maya import cmds
from maya_stubgen.utils import timed

from ..common import NULL_LOCATION
from .html_parser import DocumentationNotFound, function_from_documentation
from .synopsis_parser import SynopsisNotFound, function_from_synopsis

logger = logging.getLogger(__name__)

__all__ = ["parse_cmds_module"]


@timed
def parse_cmds_module(
    module: ModuleInfo,
    executor: concurrent.futures.Executor,
) -> Module:
    logger.debug("Parsing module: %s", module.name)

    module_name = module.name
    docspec_members = []

    commands = [command_name for command_name, _ in inspect.getmembers(cmds, callable)]

    with executor:
        results = executor.map(parse_cmds_command, commands)
        for docspec_member in results:
            if docspec_member is not None:
                docspec_members.append(docspec_member)

    return Module(
        location=NULL_LOCATION,
        name=module_name,
        docstring=None,
        members=docspec_members,
    )


def parse_cmds_command(command_name) -> Optional[Function]:
    """Parse a cmds command and return a docspec Function.

    The html Documentation is scrapped first as it gives the best results.
    If no documentation exists, we fallback to parsing the synopsis of the command.
    If the synopsis also does not exist, we fallback to generating a degraded Function.

    Args:
        command_name: The name of the maya command.

    Returns:
        The Docspec Function for the maya command.
        None: When the command should not be included in the stubs/documentation
    """

    if command_name[0].isupper():
        return

    docspec_member = None

    try:
        docspec_member = function_from_documentation(command_name)
    except DocumentationNotFound:
        logger.debug(
            "Couldn't find documentation for %s, falling back to parsing synopsis.",
            command_name,
        )
        try:
            docspec_member = function_from_synopsis(command_name)
        except SynopsisNotFound:
            logger.debug(
                "Couldn't find synopsis for %s, using degraded signature.",
                command_name,
            )
            docspec_member = Function(
                location=NULL_LOCATION,
                name=command_name,
                docstring=None,
                modifiers=None,
                args=[
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
                ],
                return_type="Any",
                decorations=None,
                semantic_hints=[],
            )

    return docspec_member
