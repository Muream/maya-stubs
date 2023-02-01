from __future__ import annotations

import concurrent.futures
import inspect
import logging
from pkgutil import ModuleInfo

import docspec
from maya import cmds
from maya_stubgen.utils import timed

from ..common import NULL_LOCATION, degraded_function
from .html_parser import DocumentationNotFound, function_from_documentation
from .synopsis_parser import SynopsisNotFound, function_from_synopsis

logger = logging.getLogger(__name__)

__all__ = ["parse_cmds_module"]


@timed
def parse_cmds_module(
    module: ModuleInfo,
    executor: concurrent.futures.Executor,
) -> docspec.Module:
    logger.debug("Parsing module: %s", module.name)

    module_name = module.name
    docspec_members = []

    commands = [command_name for command_name, _ in inspect.getmembers(cmds, callable)]

    with executor:
        results = executor.map(parse_cmds_command, commands)
        for docspec_member in results:
            if docspec_member is not None:
                docspec_members.append(docspec_member)

    return docspec.Module(
        location=NULL_LOCATION,
        name=module_name,
        docstring=None,
        members=docspec_members,
    )


def parse_cmds_command(command_name) -> docspec.Function | None:
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

    # Default Docspec member overwritten if the parsers are successful
    docspec_function = degraded_function(command_name)

    try:
        synopsis_docspec_function = function_from_synopsis(command_name)
    except SynopsisNotFound:
        logger.debug("Couldn't find synopsis for %s.", command_name)
        synopsis_docspec_function = None

    try:
        docs_docspec_function = function_from_documentation(command_name)
    except DocumentationNotFound:
        logger.debug("Couldn't find documentation for %s", command_name)
        docs_docspec_function = None

    # The docs parser doesn't parse positional arguments but the synopsis parser does
    if synopsis_docspec_function and docs_docspec_function:
        for arg in synopsis_docspec_function.args:
            if arg.type is docspec.Argument.Type.POSITIONAL_REMAINDER:
                docs_docspec_function.args.insert(0, arg)

        positional_args = [
            arg
            for arg in synopsis_docspec_function.args
            if arg.type is docspec.Argument.Type.POSITIONAL_ONLY
        ]
        if positional_args:
            positional_args.append(
                docspec.Argument(
                    NULL_LOCATION, "/", docspec.Argument.Type.POSITIONAL_ONLY
                )
            )

            for arg in reversed(positional_args):
                docs_docspec_function.args.insert(0, arg)

    if docspec_function:
        docspec_function = synopsis_docspec_function

    if docs_docspec_function:
        docspec_function = docs_docspec_function

    return docspec_function
