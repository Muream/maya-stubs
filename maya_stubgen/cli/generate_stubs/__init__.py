import ast
import importlib
import logging
import traceback
from copy import deepcopy
from pkgutil import ModuleInfo, walk_packages

import black
import click

from .common import get_stub_path
from .generate_cmds_stubs import generate_cmds_stubs
from .generate_generic_stubs import generate_generic_stub

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def apply_override(input_node: ast.AST, override_node: ast.AST, output_node: ast.AST):
    """Merge the input node with the override node into the output node.


    Notes:
        - For Classes, this will be called recursively and only apply the overridden
            methods
        - This function doesn't return anything but modifies the reference to the output
            node.

    Args:
        input_node: The node to be overridden.
        override_node: The node containing the overrides.
        output_node: The node containing the result of the merge.
    """
    for input_subnode in input_node.body:
        result_nodes = []

        if isinstance(input_subnode, (ast.FunctionDef, ast.ClassDef)):
            for override_subnode in override_node.body:
                if not isinstance(override_subnode, type(input_subnode)):
                    continue

                if input_subnode.name == override_subnode.name:
                    if isinstance(input_subnode, ast.ClassDef):
                        result_node = deepcopy(override_subnode)
                        result_node.body = []
                        apply_override(input_subnode, override_subnode, result_node)
                        result_nodes.append(result_node)
                    else:
                        result_nodes.append(override_subnode)

        if not result_nodes:
            result_nodes = [input_subnode]

        output_node.body.extend(result_nodes)


def apply_stub_override(module: ModuleInfo, stub_source: str) -> str:
    """Apply the hand written stub overrides to the stubs of the given module.

    Args:
        module_name: The name of the module to apply the stubs for.
        stub_source: stubs string to apply the stubs to.

    Returns:
        The stubs string with the overrides applied.
    """
    stub_override_path = get_stub_path(module, override=True)

    if not stub_override_path.exists():
        return stub_source

    stub_override_source = stub_override_path.read_text(encoding="utf8")

    override_tree = ast.parse(stub_override_source)
    input_tree = ast.parse(stub_source)
    output_tree = ast.parse("")

    apply_override(input_tree, override_tree, output_tree)

    return ast.unparse(output_tree)


def generate_stubs_for_module(module: ModuleInfo):
    logger.info("Generating stubs for %s.", module.name)
    logger.debug("Generating stubs.")

    if module.name == "maya.cmds":
        content = generate_cmds_stubs()
    else:
        content = generate_generic_stub(module)

    logger.debug("Applying stubs overrides.")
    content = apply_stub_override(module, content)

    logger.debug("Formatting stubs.")
    content = black.format_str(
        content,
        mode=black.Mode(line_length=10_000, is_pyi=True),
    )

    stub_path = get_stub_path(module)
    stub_path.parent.mkdir(parents=True, exist_ok=True)
    with stub_path.open("w", encoding="utf8") as f:
        logger.debug("Writing content to %s", stub_path)
        f.write(content)


def ignore_module(module: ModuleInfo):
    blacklist = ["ge", "internal", "test", "unsupported"]
    ignore = False

    if module.name.split(".")[-1].startswith("_"):
        ignore = True

    for name in module.name.split("."):
        if name in blacklist:
            ignore = True

    return ignore


@click.command()
def generate_stubs() -> None:
    logger.info("Generating Stubs")

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

    try:
        package = importlib.import_module("maya")
        for module in walk_packages(package.__path__, package.__name__ + "."):
            if ignore_module(module):
                continue
            if module.name in whitelist:  # temporary work on a specific stub
                generate_stubs_for_module(module)
    except BaseException:
        logger.error("Failed to generate stubs: %s", traceback.format_exc())
    else:
        logger.success("Stubs generated")
