import importlib
import inspect
import logging
import sys
import traceback
from pathlib import Path
from pkgutil import ModuleInfo, walk_packages
from types import ModuleType

import click

from .common import get_stub_path
from .generate_cmds_stubs import generate_cmds_stubs
from .generate_generic_stubs import generate_generic_stub

logger = logging.getLogger(__name__)


def import_from_path(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def apply_stub_override(module: ModuleInfo, content: str) -> str:
    stub_path_override = get_stub_path(module, override=True)
    stub_path_temp = get_stub_path(module, temp=True)

    stub_path_override.parent.mkdir(parents=True, exist_ok=True)
    if not stub_path_override.exists():
        with stub_path_override.open("w", encoding="utf8") as f:
            f.write("# fmt: off\nfrom __future__ import annotations\n")

    stub_path_temp.parent.mkdir(parents=True, exist_ok=True)
    with stub_path_temp.open("w", encoding="utf8") as f:
        f.write(content)

    stub_override = import_from_path(module.name + "_override", stub_path_override)
    stub_generated = import_from_path(module.name + "_generated", stub_path_temp)

    for name, override_member in inspect.getmembers(stub_override):
        stub_member = getattr(stub_generated, name, None)
        if not stub_member:
            continue

        if inspect.ismodule(override_member):
            continue
        elif inspect.isclass(override_member):
            stub_src = inspect.getsource(stub_member)
            overridden_stub_src = stub_src

            for cls_member_name, cls_override_member in inspect.getmembers(
                override_member
            ):
                if cls_member_name.startswith("_"):
                    # ignore private members
                    continue
                cls_stub_member = getattr(stub_member, cls_member_name, None)
                if not cls_stub_member:
                    continue
                overridden_stub_src = overridden_stub_src.replace(
                    inspect.getsource(cls_stub_member),
                    inspect.getsource(cls_override_member),
                )

            content = content.replace(
                stub_src,
                overridden_stub_src,
            )

        elif callable(override_member):
            content = content.replace(
                inspect.getsource(stub_member),
                inspect.getsource(override_member),
            )

    return content


def generate_stubs_for_module(module: ModuleInfo):
    logger.info("Generating stubs for: %s", module.name)

    if module.name == "maya.cmds":
        content = generate_cmds_stubs()
    else:
        content = generate_generic_stub(module)

    stub_path = get_stub_path(module)

    stub_path.parent.mkdir(parents=True, exist_ok=True)

    content = apply_stub_override(module, content)

    with stub_path.open("w", encoding="utf8") as f:
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
