from __future__ import annotations

import concurrent.futures
import importlib
import logging
import os
from pathlib import Path
from pkgutil import walk_packages
from typing import Optional

import black
import docspec
import docspec_to_jinja
from maya_stubgen.utils import initialize_maya, timed

from .common import get_stub_path

logger = logging.getLogger(__name__)
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


def parse_package(
    package_name: str,
    whitelist: Optional[list[str]] = None,
) -> list[docspec.Module]:
    logger.debug("Parsing package: %s", package_name)
    from .docspec_parsers import parse_builtin_module, parse_cmds_module

    docspec_modules: list[docspec.Module] = []

    # Executor with pre-initialized maya interpreters passed around to
    #  the different parsers
    executor = concurrent.futures.ProcessPoolExecutor(initializer=initialize_maya)

    package = importlib.import_module(package_name)

    for module in walk_packages(package.__path__, package.__name__ + "."):

        if whitelist is not None and module.name not in whitelist:
            continue

        if module.name == "maya.cmds":
            docspec_module = parse_cmds_module(module, executor)
        else:
            docspec_module = parse_builtin_module(module, executor)
        docspec_modules.append(docspec_module)

    return docspec_modules


@timed
def dump_docspec():
    whitelist = [
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
    ]

    modules = parse_package("maya", whitelist=whitelist)
    for module in modules:
        docspec_cache = (
            Path().resolve()
            / ".cache"
            / "docspec"
            / (module.name.replace(".", "/") + ".json")
        )

        os.makedirs(docspec_cache.parent, exist_ok=True)

        logger.debug("Dumping %s", module.name)
        docspec.dump_module(module, target=str(docspec_cache))


def build_stubs(path: Path, reuse_cache: bool = False):

    if not reuse_cache:
        dump_docspec()

    docspec_cache = Path().resolve() / ".cache" / "docspec"

    for f in docspec_cache.glob("**/*.json"):
        module = docspec.load_module(str(f))

        stub = docspec_to_jinja.render_module(module, "pyi")

        stub_path = path / (
            module.name.replace("maya", "maya-stubs").replace(".", "/") + ".pyi"
        )

        os.makedirs(stub_path.parent, exist_ok=True)

        with stub_path.open("w", encoding="utf-8") as f:
            f.write(stub)


def build_docs(path: Path, reuse_cache: bool = False):
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

        with module_doc_path.open("w", encoding="utf-8") as f:
            f.write(rendered_module)

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

            with member_doc_path.open("w", encoding="utf-8") as f:
                f.write(rendered_member)
