import importlib
import logging
import traceback
from pkgutil import ModuleInfo, walk_packages

import click
from redbaron import RedBaron

from .common import get_stub_path
from .generate_cmds_stubs import generate_cmds_stubs
from .generate_generic_stubs import generate_generic_stub

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def replace_override(override_red, input_red, output_red):
    for override_node in override_red:
        if override_node.type == "def":
            generated_function = input_red.find("def", name=override_node.name)
            if generated_function:
                index = -1
                for node in output_red:
                    if node.dumps() == generated_function.dumps():
                        index = output_red.index(node)

                decorators = override_node.decorators or []

                is_overloaded = False
                for decorator in decorators:
                    if decorator.name.value == "overload":
                        is_overloaded = True

                if is_overloaded:
                    output_red.insert(index, override_node)
                else:
                    output_red[index] = override_node

        if override_node.type == "class":
            generated_class = input_red.find("class", name=override_node.name)
            result_class = output_red.find("class", name=override_node.name)
            if generated_class and result_class:
                replace_override(override_node, generated_class, result_class)


def apply_stub_override(module: ModuleInfo, stub_source: str) -> str:
    """Apply the hand written stub overrides to the stubs of the given module.

    Args:
        module_name: The name of the module to apply the stubs for.
        stub_source: stubs string to apply the stubs to.

    Returns:
        The stubs string with the overrides applied.
    """
    stub_override_path = get_stub_path(module, override=True)
    stub_override_source = stub_override_path.read_text(encoding="utf8")

    override_red = RedBaron(stub_override_source)
    input_red = RedBaron(stub_source)

    # the output red instantiated in the same was as the input red
    # but gets updated by `replace_override`
    output_red = RedBaron(stub_source)

    replace_override(override_red, input_red, output_red)

    return output_red.dumps()


def generate_stubs_for_module(module: ModuleInfo):
    logger.info("Generating stubs for %s.", module.name)
    logger.debug("Generating stubs.")

    if module.name == "maya.cmds":
        content = generate_cmds_stubs()
    else:
        content = generate_generic_stub(module)

    logger.debug("Applying stubs overrides.")
    content = apply_stub_override(module, content)

    stub_path = get_stub_path(module)
    stub_path.parent.mkdir(parents=True, exist_ok=True)
    with stub_path.open("w", encoding="utf8") as f:
        logger.debug("Writing content to %s.", stub_path)
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
        "maya.cmds",
        "maya.standalone",
        "maya.utils",
        "maya.mel",
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
