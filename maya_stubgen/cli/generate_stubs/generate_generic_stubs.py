from __future__ import annotations

import inspect
import logging
from importlib import import_module
from pkgutil import ModuleInfo
from typing import *

from .common import STUB_HEADER, Class, Function, Variable, get_classes

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def imports_for_module(module: ModuleInfo) -> str:
    """Get the relevant imports for the given module

    Args:
        module: The module to get the imports for.

    Returns:
        The imports string.
    """

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

    return imports


def generate_generic_stub(module: ModuleInfo) -> str:
    """Generate stubs for any given python module.

    Args:
        module: Module to generate stubs for.

    Returns:
        The generated stubs.
    """

    module = import_module(module.name)
    content = []

    for name, member in inspect.getmembers(module):
        stub_member = None

        if name.startswith("_"):
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
        if name in ["type", "object"]:
            continue

        stub_member = Class.from_object(cls, name)
        content.append(stub_member.stub)

    imports = imports_for_module(module)

    return STUB_HEADER.format(imports=imports) + "\n".join(content)
