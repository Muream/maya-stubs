from __future__ import annotations

import importlib
import itertools
import logging
import os
from pathlib import Path
import pkgutil
from typing import Optional

import docspec
import docspec_to_jinja

from .parsers.cmds_parsers import CmdsParser
from .parsers.common import Parser
from ... import _logging
from ...utils import maya_standalone, timed

from .parsers import BuiltinParser, CmdsParser

logger = _logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# def apply_override(input_node: ast.AST, override_node: ast.AST, output_node: ast.AST):
#     """Merge the input node with the override node into the output node.

#     Notes:
#         - For Classes, this will be called recursively and only apply the overridden
#             methods
#         - This function doesn't return anything but modifies the reference to the output
#             node.

#     Args:
#         input_node: The node to be overridden.
#         override_node: The node containing the overrides.
#         output_node: The node containing the result of the merge.
#     """
#     for input_subnode in input_node.body:
#         result_nodes = []

#         if isinstance(input_subnode, (ast.FunctionDef, ast.ClassDef)):
#             for override_subnode in override_node.body:
#                 if not isinstance(override_subnode, type(input_subnode)):
#                     continue

#                 if input_subnode.name == override_subnode.name:
#                     if isinstance(input_subnode, ast.ClassDef):
#                         result_node = deepcopy(override_subnode)
#                         result_node.body = []
#                         apply_override(input_subnode, override_subnode, result_node)
#                         result_nodes.append(result_node)
#                     else:
#                         result_nodes.append(override_subnode)

#         if not result_nodes:
#             result_nodes = [input_subnode]

#         output_node.body.extend(result_nodes)


# def apply_stub_override(module: ModuleInfo, stub_source: str) -> str:
#     """Apply the hand written stub overrides to the stubs of the given module.

#     Args:
#         module_name: The name of the module to apply the stubs for.
#         stub_source: stubs string to apply the stubs to.

#     Returns:
#         The stubs string with the overrides applied.
#     """
#     stub_override_path = get_stub_path(module, override=True)

#     if not stub_override_path.exists():
#         return stub_source

#     stub_override_source = stub_override_path.read_text(encoding="utf8")

#     override_tree = ast.parse(stub_override_source)
#     input_tree = ast.parse(stub_source)
#     output_tree = ast.parse("")

#     apply_override(input_tree, override_tree, output_tree)

#     return ast.unparse(output_tree)


# def generate_stubs_for_module(module: ModuleInfo):
#     logger.info("Generating stubs for %s.", module.name)
#     logger.debug("Generating stubs.")

#     if module.name == "maya.cmds":
#         content = generate_cmds_stubs()
#     else:
#         content = generate_generic_stub(module)

#     logger.debug("Applying stubs overrides.")
#     content = apply_stub_override(module, content)

#     logger.debug("Formatting stubs.")
#     content = black.format_str(
#         content,
#         mode=black.FileMode(line_length=10_000, is_pyi=True),
#     )

#     stub_path = get_stub_path(module)
#     stub_path.parent.mkdir(parents=True, exist_ok=True)
#     with stub_path.open("w", encoding="utf8") as f:
#         logger.debug("Writing content to %s", stub_path)
#         f.write(content)


class MayaParser(Parser):
    def parse_package(
        self,
        name: str,
        whitelist: Optional[list[str]] = None,
        member_pattern: Optional[str] = None,
    ) -> list[docspec.Module]:
        logger.debug("Parsing package: %s", name)

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
            if whitelist is not None and module_name not in whitelist:
                continue

            if module_name == "maya.cmds":
                docspec_module = CmdsParser(executor).parse_module(
                    module_name, member_pattern=member_pattern
                )
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


@timed
def dump_docspec(
    whitelist: Optional[list[str]] = None, member_pattern: Optional[str] = None
) -> None:
    whitelist = whitelist or [
        # OpenMaya 1.0
        "maya.OpenMaya",
        "maya.OpenMayaAnim",
        "maya.OpenMayaFX",
        "maya.OpenMayaMPx",
        "maya.OpenMayaRender",
        "maya.OpenMayaUI",
        # OpenMaya 2.0
        "maya.api.MDGContextGuard",
        "maya.api.OpenMaya",
        "maya.api.OpenMayaAnim",
        "maya.api.OpenMayaRender",
        "maya.api.OpenMayaUI",
        # other
        "maya.cmds",
        "maya.standalone",
        "maya.utils",
        "maya.mel",
        "maya",
    ]

    logger.info("Dumping Docspec for %s", ", ".join(whitelist))

    with maya_standalone():
        modules = MayaParser().parse_package(
            "maya", whitelist=whitelist, member_pattern=member_pattern
        )

    for module in modules:
        docspec_cache = (
            Path().resolve()
            / ".cache"
            / "docspec"
            / (module.name.replace(".", "/") + ".json")
        )

        os.makedirs(docspec_cache.parent, exist_ok=True)

        logger.debug("Dumping %s to %s", module.name, docspec_cache)
        docspec.dump_module(module, target=str(docspec_cache))


def build_stubs(
    path: Path,
    reuse_cache: bool = False,
    whitelist: Optional[list[str]] = None,
    member_pattern: Optional[str] = None,
) -> None:
    if not reuse_cache:
        dump_docspec(whitelist=whitelist, member_pattern=member_pattern)

    whitelist_patterns = []
    if whitelist:
        whitelist_patterns = [
            pattern
            for mod in whitelist
            for pattern in (
                # whitelist entry may be a module or a package
                mod.replace(".", "/") + ".json",
                mod.replace(".", "/") + "/__init__.json",
            )
        ]

    docspec_cache = Path().resolve() / ".cache" / "docspec"
    for f in docspec_cache.glob("**/*.json"):
        if whitelist_patterns and not any(
            f.match(pattern) for pattern in whitelist_patterns
        ):
            continue

        logger.debug("Loading %s", f)
        module = docspec.load_module(str(f))

        logger.debug("Rendering %s", module.name)
        stub = docspec_to_jinja.render_module(module, "pyi")

        stub_path = path / (
            module.name.replace("maya", "maya-stubs").replace(".", "/") + ".pyi"
        )

        os.makedirs(stub_path.parent, exist_ok=True)

        logger.debug("Writing %s to %s", module.name, stub_path)
        with stub_path.open("w", encoding="utf-8") as out_f:
            out_f.write(stub)

        if stub_path.parent.resolve() != docspec_cache.resolve():
            # create empty __init__ if it does not exist already
            init_path = stub_path.parent / "__init__.pyi"
            with init_path.open("a"):
                pass


def build_docs(path: Path, reuse_cache: bool = False) -> None:
    logger.info("Building docs")

    if not reuse_cache:
        dump_docspec()

    module_paths = {
        # Commands
        "maya.cmds": "maya/cmds",
        # Open Maya 1.0
        "maya.MDGContextGuard": "maya/open-maya-1/MDGContextGuard",
        "maya.OpenMaya": "maya/open-maya-1/OpenMaya",
        "maya.OpenMayaAnim": "maya/open-maya-1/OpenMayaAnim",
        "maya.OpenMayaRender": "maya/open-maya-1/OpenMayaRender",
        "maya.OpenMayaUI": "maya/open-maya-1/OpenMayaUI",
        "maya.OpenMayaFX": "maya/open-maya-1/OpenMayaFX",
        "maya.OpenMayaMPx": "maya/open-maya-1/OpenMayaMPx",
        # Open Maya 2.0
        "maya.api.MDGContextGuard": "maya/open-maya-2/MDGContextGuard",
        "maya.api.OpenMaya": "maya/open-maya-2/OpenMaya",
        "maya.api.OpenMayaAnim": "maya/open-maya-2/OpenMayaAnim",
        "maya.api.OpenMayaRender": "maya/open-maya-2/OpenMayaRender",
        "maya.api.OpenMayaUI": "maya/open-maya-2/OpenMayaUI",
        # Other
        "maya.mel": "maya/other/mel",
        "maya.utils": "maya/other/utils",
        "maya.standalone": "maya/other/standalone",
    }
    docspec_cache = Path().resolve() / ".cache" / "docspec"

    for f in docspec_cache.glob("**/*.json"):
        module = docspec.load_module(str(f))

        logger.debug("Building docs for: %s", module.name)

        rendered_module = docspec_to_jinja.render_module(module, "markdown")
        module_doc_path = path / "content" / module_paths[module.name] / "_index.md"

        os.makedirs(module_doc_path.parent, exist_ok=True)

        with module_doc_path.open("w", encoding="utf-8") as doc_f:
            doc_f.write(rendered_module)

        for member in module.members:
            logger.debug("Building docs for: %s", member.name)

            if isinstance(member, docspec.Class):
                rendered_member = docspec_to_jinja.render_class(member, "markdown")
            elif isinstance(member, docspec.Function):
                rendered_member = docspec_to_jinja.render_function(member, "markdown")
            else:
                continue

            member_doc_path = (
                Path().resolve()
                / "docs"
                / "content"
                / module_paths[module.name]
                / f"{member.name}.md"
            )

            os.makedirs(member_doc_path.parent, exist_ok=True)

            with member_doc_path.open("w", encoding="utf-8") as member_doc_f:
                member_doc_f.write(rendered_member)
