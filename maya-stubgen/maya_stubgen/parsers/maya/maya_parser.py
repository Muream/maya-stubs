from __future__ import annotations

import importlib
import itertools
import logging
import pkgutil
from typing import Optional

import docspec

from maya_stubgen.parsers.common import NULL_LOCATION

from .. import BuiltinParser, CmdsParser, Parser

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class MayaParser(Parser):
    def parse_package(
        self,
        name: str,
        whitelist: Optional[list[str]] = None,
        member_pattern: Optional[str] = None,
    ) -> list[docspec.Module]:
        logger.debug("Parsing package: %s", name)

        if whitelist is None:
            whitelist = []

        docspec_modules: list[docspec.Module] = []

        # Executor with pre-initialized maya interpreters passed around to
        # the different parsers
        # executor = concurrent.futures.ProcessPoolExecutor(initializer=initialize_maya)
        executor = None

        package = importlib.import_module(name)

        submodules = pkgutil.walk_packages(package.__path__, package.__name__ + ".")
        # include root package
        all_modules = itertools.chain(
            [(package.__name__, True)], ((mod.name, mod.ispkg) for mod in submodules)
        )
        for module_name, ispkg in all_modules:
            if module_name not in whitelist:
                continue

            if module_name == "maya.cmds":
                docspec_module = CmdsParser(executor).parse_module(
                    module_name, member_pattern=member_pattern
                )
                new_module = docspec.Module(
                    NULL_LOCATION,
                    name=f"{module_name}",
                    docstring=docspec.Docstring(NULL_LOCATION, ""),
                    members=[],
                )

                for cmds_function in docspec_module.members:
                    cmds_module = docspec.Module(
                        NULL_LOCATION,
                        name=f"{module_name}._{cmds_function.name}",
                        docstring=docspec.Docstring(NULL_LOCATION, ""),
                        members=[cmds_function],
                    )
                    docspec_modules.append(cmds_module)
                    new_module.members.append(cmds_module)

                docspec_module = new_module
            else:
                docspec_module = BuiltinParser(executor).parse_module(
                    module_name, member_pattern=member_pattern
                )

            if ispkg:
                docspec_module.name += ".__init__"

            docspec_modules.append(docspec_module)

        return docspec_modules

    def parse_module(self, name: str) -> docspec.Module:
        raise NotImplementedError

    def parse_function(self, module_name: str, name: str) -> docspec.Function:
        raise NotImplementedError

    def parse_class(self, module_name: str, name: str) -> docspec.Class:
        raise NotImplementedError

    def parse_variable(self, module_name: str, name: str) -> docspec.Variable:
        raise NotImplementedError
