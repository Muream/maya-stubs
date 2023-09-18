from __future__ import annotations

import inspect
import re
from typing import Optional

import docspec
from attrs import Factory, define
from maya import cmds

from ..... import _logging
from ..common import NULL_LOCATION, Parser, degraded_function, DocspecModuleMembers
from .html_parser import CmdsDocsParser, DocumentationNotFound
from .synopsis_parser import CmdsSynopsisParser, SynopsisNotFound

logger = _logging.getLogger(__name__)

__all__ = ["CmdsParser"]


@define
class CmdsParser(Parser):
    docs_parser: CmdsDocsParser = Factory(CmdsDocsParser)
    synposis_parser: CmdsSynopsisParser = Factory(CmdsSynopsisParser)

    def parse_package(self, name: str) -> list[docspec.Module]:
        raise NotImplementedError

    def parse_module(
        self, name: str, member_pattern: Optional[str] = None
    ) -> docspec.Module:
        logger.debug("Parsing module: %s", name)

        module_name = name
        docspec_members: list[DocspecModuleMembers] = []

        commands = [
            command_name
            for command_name, _ in inspect.getmembers(cmds, callable)
            if not command_name[0].isupper()
            and (
                member_pattern is None
                or re.search(member_pattern, "{}.{}".format(name, command_name))
            )
        ]

        results = self.map(lambda cmd: self.parse_function(module_name, cmd), commands)
        docspec_members.extend(results)

        return docspec.Module(
            location=NULL_LOCATION,
            name=module_name,
            docstring=None,
            members=docspec_members,
        )

    def parse_function(self, module_name: str, name: str) -> docspec.Function:
        """Parse a cmds command and return a docspec Function.

        The html Documentation is scrapped first as it gives the best results.
        If no documentation exists, we fallback to parsing the synopsis of the command.
        If the synopsis also does not exist, we fallback to generating a degraded Function.

        Args:
            name: The name of the maya command.

        Returns:
            The Docspec Function for the maya command.
            None: When the command should not be included in the stubs/documentation
        """

        # Default Docspec member overwritten if the parsers are successful
        docspec_function = degraded_function(name)

        try:
            synopsis_docspec_function = self.synposis_parser.parse_function(
                module_name, name
            )
        except SynopsisNotFound:
            logger.warning("Couldn't find synopsis for %s.", name)
            synopsis_docspec_function = None

        try:
            docs_docspec_function = self.docs_parser.parse_function(module_name, name)
        except DocumentationNotFound:
            logger.warning("Couldn't find documentation for %s", name)
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
            docs_docspec_function.args = positional_args + docs_docspec_function.args

        if docs_docspec_function:
            docspec_function = docs_docspec_function
        elif synopsis_docspec_function:
            docspec_function = synopsis_docspec_function

        return docspec_function

    def parse_class(self, module_name: str, name: str) -> docspec.Class:
        raise NotImplementedError

    def parse_variable(self, module_name: str, name: str) -> docspec.Variable:
        raise NotImplementedError
