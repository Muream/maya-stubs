"""A Docspec parser for python builtins.

As opposed to docspec-python, this is uses runtime introspection instead of static analysis.
"""
from __future__ import annotations

import concurrent.futures
import importlib
import inspect
import logging
from pkgutil import ModuleInfo
from typing import Any, Callable, List

from docspec import (
    Argument,
    Class,
    Docstring,
    Function,
    FunctionSemantic,
    Module,
    Variable,
)

from .common import NULL_LOCATION

logger = logging.getLogger(__name__)


def parse_builtin_module(
    module: ModuleInfo,
    executor: concurrent.futures.Executor,
) -> Module:
    logger.debug("Parsing module: %s", module.name)

    module_name = module.name

    module = importlib.import_module(module.name)

    docspec_members = []
    docstring = inspect.getdoc(module)
    if docstring is not None:
        docstring = Docstring(NULL_LOCATION, docstring)

    members = inspect.getmembers(module)
    with executor:
        results = executor.map(parse_builtin_member, members)
        for docspec_member in results:
            if docspec_member is not None:
                docspec_members.append(docspec_member)

    return Module(NULL_LOCATION, module_name, docstring, docspec_members)


def parse_builtin_member(member):
    member_name, py_member = member
    docspec_member = None

    if member_name.startswith("_"):
        return

    if inspect.ismodule(py_member):
        # Ignore modules
        return

    elif inspect.isclass(py_member):
        # we will add classes in a 2nd pass
        docspec_member = parse_builtin_class(member_name, py_member)

    elif callable(py_member):
        docspec_member = parse_builtin_function(member_name, py_member)
    else:
        # member has to be a variable now?
        # docspec_member = parse_builtin_variable(name, py_member)
        pass

    return docspec_member


def parse_builtin_class(name: str, cls: Any) -> Class:
    logger.debug("Parsing class: %s", name)
    docstring = Docstring(NULL_LOCATION, inspect.getdoc(cls) or "")
    members = []

    ignored_members = [
        # These members somehow sometime share their id with their `super`
        # but sometimes don't
        "__dict__",
        "__bases__",
        "__mro__",
        "__name__",
        "__qualname__",
        "__doc__",
        "__hash__",
        "__init_subclass__",
        "__module__",
        "__subclasscheck__",
        "__subclasshook__",
        "__weakref__",
    ]

    try:
        parent = type.mro(cls)[1]
    except IndexError:
        parent = object

    if parent is not None:
        parent_members = [id(m[1]) for m in inspect.getmembers(parent)]
    else:
        parent_members = []

    for member_name, member in inspect.getmembers(cls):
        if member_name in ignored_members:
            continue

        is_inherited = id(member) in parent_members
        if is_inherited:
            continue

        if inspect.isclass(member):
            members.append(parse_builtin_class(member_name, member))
        elif callable(member):
            method = parse_builtin_function(member_name, member, is_method=True)
            members.append(method)
        # elif inspect.isgetsetdescriptor(member):
        #     getter = Function.from_object(member, member_name, FunctionType.getter)
        #     setter = Function.from_object(member, member_name, FunctionType.setter)
        #     members.append(getter)
        #     members.append(setter)
        else:
            members.append(parse_builtin_variable(member_name, member))

    return Class(
        location=NULL_LOCATION,
        name=name,
        docstring=docstring,
        bases=[base.__name__ for base in cls.__bases__],
        members=members,
        metaclass=None,
        modifiers=[],
        semantic_hints=[],
        decorations=[],
    )


def parse_builtin_function(
    name: str,
    function: Callable,
    is_method: bool = False,
) -> Function:
    logger.debug("Parsing function: %s", name)

    docstring_content = inspect.getdoc(function)
    docstring = (
        Docstring(NULL_LOCATION, docstring_content) if docstring_content else None
    )

    args = get_args(function, is_method)
    return_type = get_return_type(function)

    semantic_hints = []
    if is_method:
        semantic_hints.append(FunctionSemantic.INSTANCE_METHOD)

    return Function(
        location=NULL_LOCATION,
        name=name,
        docstring=docstring,
        modifiers=[],
        args=args,
        return_type=return_type,
        decorations=[],
    )


def parse_builtin_variable(name, variable: Any) -> Variable:
    logger.debug("Parsing variable: %s", name)
    return Variable(
        location=NULL_LOCATION,
        name=name,
        docstring=None,
        datatype=variable.__class__.__name__,
        value=str(variable),
        modifiers=[],
        semantic_hints=[],
    )


def get_args(function: Callable, is_method: bool = False) -> List[Argument]:
    try:
        args = arguments_from_signature(function)
    except RuntimeError:
        args = []

        if is_method:
            args.append(
                Argument(
                    location=NULL_LOCATION,
                    name="self",
                    type=Argument.Type.POSITIONAL_ONLY,
                    decorations=[],
                    datatype=None,
                    default_value=None,
                )
            )

        for _arg in ["*args", "**kwargs"]:
            arg = Argument(
                location=NULL_LOCATION,
                name=_arg,
                type=Argument.Type.POSITIONAL,
                decorations=[],
                datatype="Any",
                default_value=None,
            )
            args.append(arg)
    return args


def get_return_type(function: Callable) -> str:
    try:
        signature = inspect.signature(function)
    except Exception:
        return "Any"

    return (
        signature.return_annotation
        if signature.return_annotation is not inspect.Signature.empty
        else "Any"
    )


def arguments_from_signature(function: Callable) -> List[Argument]:
    """Returns the docspec.Arguments from the function signature.

    Args:
        function: The function to get the arguments for

    Raises:
        RuntimeError: If `inspect.signature` failed for whatever reason

    Returns:
        The docspec arguments of the function.
    """
    try:
        signature = inspect.signature(function)
    except Exception as exc:
        raise RuntimeError(f"Failed to get the signature from {function!r}") from exc

    args = []
    for param in signature.parameters.values():
        args.append(param_to_argument(param))

    return args


def param_to_argument(param: inspect.Parameter) -> Argument:
    """Convert an `inspect.Parameter` to a `docspec.Argument`

    Args:
        param: The `inspect.parameter` to convert

    Returns:
        The converted `docspec.Argument`
    """

    arg_name = str(param)
    arg_type = Argument.Type(param.kind)
    arg_decorations = []
    arg_datatype = (
        param.annotation if param.annotation is not inspect.Signature.empty else None
    )
    arg_default_value = (
        str(param.default) if param.default is not inspect.Signature.empty else None
    )
    return Argument(
        location=NULL_LOCATION,
        name=arg_name,
        type=arg_type,
        decorations=arg_decorations,
        datatype=arg_datatype,
        default_value=arg_default_value,
    )
