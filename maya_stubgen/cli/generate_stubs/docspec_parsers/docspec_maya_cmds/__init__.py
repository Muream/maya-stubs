import inspect
import logging
from pkgutil import ModuleInfo

import requests
from docspec import Argument, Function, Module
from maya import cmds

from ..common import NULL_LOCATION
from .html_parser import DocumentationNotFound, function_from_documentation
from .synopsis_parser import SynopsisNotFound, function_from_synopsis

logger = logging.getLogger(__name__)

__all__ = ["parse_cmds_module"]


def parse_cmds_module(module: ModuleInfo) -> Module:
    logger.debug("Parsing module: %s", module.name)

    module_name = module.name
    docspec_members = []

    docstring = inspect.getdoc(module)

    for command_name, _ in inspect.getmembers(cmds, callable):
        if command_name[0].isupper():
            continue

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

        docspec_members.append(docspec_member)

    return Module(NULL_LOCATION, module_name, docstring, docspec_members)
