from __future__ import annotations

import imp
import importlib.util
import inspect
import logging
import sys
import traceback
from importlib import import_module
from pathlib import Path
from pkgutil import ModuleInfo, walk_packages
from types import ModuleType
from typing import *

import click

from .common import STUB_HEADER, Class, Function, Variable
from .generate_cmds_stubs import generate_cmds_stubs

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_classes(module: ModuleInfo) -> List[Tuple[str, Type]]:
    """Return the classes in the module sorted by inheritance."""
    sorted_classes = []
    classes = inspect.getmembers(module, inspect.isclass)
    for _, cls in classes:
        for base in reversed(type.mro(cls)):
            base_tuple = (base.__name__, base)
            if base_tuple not in sorted_classes and base_tuple in classes:
                sorted_classes.append(base_tuple)
    return sorted_classes


def get_stub_path(module: ModuleInfo, override=False, temp=False) -> Path:
    folder_name = "maya-stubs-override" if override else "maya-stubs"
    extension = "py" if override or temp else "pyi"

    stub_path = Path(module.name.replace("maya", folder_name, 1).replace(".", "/"))

    if module.ispkg:
        stub_path = stub_path / f"__init__.{extension}"
    else:
        stub_path = stub_path.with_name(f"{stub_path.name}.{extension}")

    if temp:
        stub_path = "temp" / stub_path

    return stub_path.resolve()


def generate_generic_stub(module: ModuleInfo) -> str:
    module = import_module(module.name)
    content = []

    for name, member in inspect.getmembers(module):
        stub_member = None

        if name.startswith("_"):
            # ignore private members
            continue

        if inspect.ismodule(member):
            # Ignore modules
            continue
        elif inspect.isclass(member):
            # we will add classes in a 2nd pass
            continue
        elif callable(member):
            stub_member = Function.from_object(member)
        else:
            # member has to be a variable now?
            stub_member = Variable(name, type(member), member)

        if stub_member is not None:
            content.append(stub_member.stub)

    for name, cls in get_classes(module):
        if name.startswith("_"):
            # ignore private members
            continue
        if name in ["type", "object"]:
            continue

        stub_member = Class.from_object(cls, name)
        content.append(stub_member.stub)

    imports = ""

    # maya.OpenMaya
    if module.__name__ == "maya.OpenMayaAnim":
        imports = "from maya.OpenMaya import *\n"
    if module.__name__ == "maya.OpenMayaFX":
        imports = "from maya.OpenMaya import *\n"
    if module.__name__ == "maya.OpenMayaMPx":
        imports = "from maya.OpenMaya import *\n"
    if module.__name__ == "maya.OpenMayaRender":
        imports = "from maya.OpenMaya import *\n"
    if module.__name__ == "maya.OpenMayaUI":
        imports = "from maya.OpenMaya import *\n"
        imports += "from maya.OpenMayaRender import *\n"

    # maya.api.OpenMaya
    if module.__name__ == "maya.api.OpenMayaAnim":
        imports = "from maya.api.OpenMaya import *\n"
    if module.__name__ == "maya.api.OpenMayaUI":
        imports = (
            "from maya.api.OpenMaya import *\n"
            "from maya.api.OpenMayaRender import *\n"
        )

    # maya.utils
    if module.__name__ == "maya.utils":
        imports = "from logging import Handler\n"

    return STUB_HEADER.format(imports=imports) + "\n".join(content)


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
            overriden_stub_src = stub_src

            for cls_member_name, cls_override_member in inspect.getmembers(
                override_member
            ):
                if cls_member_name.startswith("_"):
                    # ignore private members
                    continue
                cls_stub_member = getattr(stub_member, cls_member_name, None)
                if not cls_stub_member:
                    continue
                overriden_stub_src = overriden_stub_src.replace(
                    inspect.getsource(cls_stub_member),
                    inspect.getsource(cls_override_member),
                )

            content = content.replace(
                stub_src,
                overriden_stub_src,
            )

        elif callable(override_member):
            content = content.replace(
                inspect.getsource(stub_member),
                inspect.getsource(override_member),
            )

    return content


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
        package = import_module("maya")
        for module in walk_packages(package.__path__, package.__name__ + "."):
            if ignore_module(module):
                continue
            if module.name in whitelist:  # temporary work on a specific stub
                generate_stubs_for_module(module)
    except BaseException:
        logger.error("Failed to generate stubs: %s", traceback.format_exc())
    else:
        logger.success("Stubs generated")
