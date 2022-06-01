from __future__ import annotations

import inspect
import logging
import traceback
from importlib import import_module
from pathlib import Path
from pkgutil import ModuleInfo, walk_packages
from typing import *

import click

from .common import STUB_HEADER, Class, Function, FunctionType, Variable
from .generate_cmds_stubs import generate_cmds_stubs

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_stub_path(module: ModuleInfo):
    stub_path = Path(module.name.replace("maya", "maya-stubs", 1).replace(".", "/"))
    if module.ispkg:
        stub_path = stub_path / "__init__.pyi"
    else:
        stub_path = stub_path.with_suffix(".pyi")
    return stub_path


def generate_generic_stub(module: ModuleInfo) -> str:
    module = import_module(module.name)
    lines = []

    for name, member in inspect.getmembers(module):
        stub_member = None

        if inspect.ismodule(member):
            continue
        elif inspect.isclass(member):
            stub_member = Class.from_object(member, name)
        elif callable(member):
            stub_member = Function.from_object(member)
        else:
            # member has to be a variable now?
            stub_member = Variable(name, type(member), member)

        if stub_member is not None:
            lines.append(stub_member.stub)

    return STUB_HEADER + "\n".join(lines)


def generate_stubs_for_module(module: ModuleInfo):
    logger.info("Generating stubs for: %s", module.name)

    stub_path = get_stub_path(module)
    if module.name == "maya.cmds":
        content = generate_cmds_stubs()
    else:
        content = generate_generic_stub(module)

    stub_path.parent.mkdir(parents=True, exist_ok=True)

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
        package = import_module("maya")
        for module in walk_packages(package.__path__, package.__name__ + "."):
            if ignore_module(module):
                continue
            if module.name in whitelist:  # temporary work on a specific stub
                generate_stubs_for_module(module)
    except BaseException as e:
        logger.error("Failed to generate stubs: %s", traceback.format_exc())
    else:
        logger.success("Stubs generated")
