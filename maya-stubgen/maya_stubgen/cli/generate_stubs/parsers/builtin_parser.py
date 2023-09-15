"""A Docspec parser for python builtins.

As opposed to docspec-python, this is uses runtime introspection instead of static analysis.
"""
from __future__ import annotations

import importlib
import inspect
import logging
import re
from pkgutil import resolve_name
from typing import Any, Callable, List, Optional, Type

import docspec
from attrs import define

from .common import NULL_LOCATION, Parser

logger = logging.getLogger(__name__)


@define
class BuiltinParser(Parser):
    """Parser for builtins that works by inspecting objects at runtime."""

    def parse_package(self, name: str) -> list[docspec.Module]:
        raise NotImplementedError

    def parse_module(
        self, name: str, member_pattern: Optional[str] = None
    ) -> docspec.Module:
        logger.debug("Parsing module: %s", name)

        module = importlib.import_module(name)

        docspec_members: list[docspec.Class | docspec.Function | docspec.Variable] = []
        docstring = inspect.getdoc(module)
        if docstring is not None:
            docstring = docspec.Docstring(NULL_LOCATION, docstring)

        if self.executor:
            pass
            # with self.executor:
            #     results = self.executor.map(self._parse_builtin_member, members)
            #     for docspec_member in results:
            #         if docspec_member is not None:
            #             docspec_members.append(docspec_member)
        else:
            members = inspect.getmembers(module)
            for member_name, member_value in members:
                qualified_name = "{}.{}".format(name, member_name)
                if member_pattern is not None and not re.search(
                    member_pattern, qualified_name
                ):
                    continue

                docspec_member = self._parse_builtin_member(
                    name, member_name, member_value
                )
                if docspec_member is not None:
                    docspec_members.append(docspec_member)

        return docspec.Module(NULL_LOCATION, name, docstring, docspec_members)

    # these crash maya 2024 when attempting to instantiate them
    _SKIP_INSTANTIATE = [
        "maya.OpenMayaMPx.MPxGlBuffer",
    ]

    # built-in class attributes we don't need
    _IGNORE_MEMBERS = [
        "__dict__",
        "__doc__",
        "__hash__",
        "__module__",
        "__weakref__",
    ]

    def parse_class(self, module_name: str, name: str) -> docspec.Class:
        logger.debug("Parsing class: %s", name)

        cls = self._members[name]

        parser = BuiltinParser()

        docstring = docspec.Docstring(NULL_LOCATION, inspect.getdoc(cls) or "")
        members = []

        parent_members = {
            id(inspect.getattr_static(parent, name))
            for parent in type.mro(cls)[1:]
            for name, _ in inspect.getmembers(parent)
        }

        # attempt to instantiate the class using the empty constructor
        # to extract more information from it
        instance = None
        qualified_name = ".".join((module_name, cls.__qualname__))
        if qualified_name not in BuiltinParser._SKIP_INSTANTIATE:
            try:
                instance = cls()
            except Exception as e:
                logger.warning("Could not instantiate type %s: %s", cls.__name__, e)

        for member_name, member in inspect.getmembers(cls):
            if member_name in BuiltinParser._IGNORE_MEMBERS:
                continue

            member = inspect.getattr_static(cls, member_name)
            parser.add_member(member_name, member)

            is_inherited = id(member) in parent_members
            if is_inherited:
                continue

            # get the underlying object if decorated
            unwrapped = inspect.unwrap(member)

            if inspect.isclass(unwrapped):
                members.append(parser.parse_class(module_name, member_name))
            elif callable(unwrapped):
                method = parser.parse_function(module_name, member_name, is_method=True)
                members.append(method)
            else:
                members.append(
                    parser.parse_variable(module_name, member_name, instance=instance)
                )

        return docspec.Class(
            location=NULL_LOCATION,
            name=name,
            docstring=docstring,
            bases=[
                self._maybe_qualified(module_name, base)
                for base in cls.__bases__
                if base is not object
            ],
            members=members,
            metaclass=None,
            modifiers=[],
            semantic_hints=[],
            decorations=[],
        )

    def parse_function(
        self, module_name: str, name: str, is_method: bool = False
    ) -> docspec.Function:
        logger.debug("Parsing function: %s", name)
        member = self._members[name]
        function: Callable = inspect.unwrap(member)

        docstring_content = inspect.getdoc(function)
        docstring = (
            docspec.Docstring(NULL_LOCATION, docstring_content)
            if docstring_content
            else None
        )

        semantic_hints = []
        if is_method:
            if isinstance(member, classmethod):
                semantic_hints.append(docspec.FunctionSemantic.CLASS_METHOD)
            elif isinstance(member, staticmethod):
                semantic_hints.append(docspec.FunctionSemantic.STATIC_METHOD)
            else:
                semantic_hints.append(docspec.FunctionSemantic.INSTANCE_METHOD)

        args = self._get_args(module_name, function, semantic_hints)
        return_type = self.get_return_type(function)

        return docspec.Function(
            location=NULL_LOCATION,
            name=name,
            docstring=docstring,
            modifiers=[],
            args=args,
            return_type=return_type,
            decorations=[],
            semantic_hints=semantic_hints,
        )

    def parse_variable(
        self, module_name: str, name: str, instance: Any = None
    ) -> docspec.Variable:
        logger.debug("Parsing variable: %s", name)

        variable = self._members[name]
        variable_value = None
        if self._is_simple_literal(variable):
            variable_value = repr(variable)

        datatype = self._maybe_qualified(module_name, type(variable))
        if isinstance(variable, property) or inspect.isgetsetdescriptor(variable):
            datatype = self._get_descriptor_type(module_name, name, instance)

        return docspec.Variable(
            location=NULL_LOCATION,
            name=name,
            docstring=None,
            datatype=datatype,
            value=variable_value,
            modifiers=[],
            semantic_hints=[],
        )

    # these crash maya 2024 on access
    _SKIP_DESCRIPTORS = [
        "maya.api.OpenMayaUI.MSelectInfo.highestPriority",
        "maya.api.OpenMaya.MArgParser.numberOfFlagsUsed",
        "maya.api.OpenMaya.MPxGeometryData.matrix",
        "maya.api.OpenMaya.MPxSurfaceShape.isRenderable",
    ]

    def _get_descriptor_type(self, module_name: str, name: str, instance: Any) -> str:
        if instance is None:
            return "Any"

        qualified_name = ".".join((module_name, type(instance).__name__, name))
        if qualified_name in BuiltinParser._SKIP_DESCRIPTORS:
            return "Any"

        try:
            value = getattr(instance, name)
        except Exception as e:
            logger.warning("Could not access descriptor %s: %s", name, e)
            return "Any"

        if value is None:
            return "Any"

        return self._maybe_qualified(module_name, type(value))

    @staticmethod
    def _is_simple_literal(value: Any, allow_none: bool = False) -> bool:
        simple_types = (str, bytes, int, float, complex)
        collection_types = (list, dict)
        simple_values = ([], {})
        return (
            (value is None and allow_none)
            or isinstance(value, simple_types)
            or (isinstance(value, collection_types) and value in simple_values)
        )

    _TYPE_OVERRIDES = {
        "builtins.SwigPyObject": "Any",
        "builtins.swigvarlink": "Any",
        "builtins.list": "List[Any]",
        "builtins.tuple": "Tuple[Any, ...]",
        "builtins.dict": "Dict[str, Any]",
    }

    @staticmethod
    def _maybe_qualified(module_name: str, cls: Type[Any]) -> str:
        """
        Returns the fully qualified name of a class.
        """
        class_module = cls.__module__
        # maya.api classes report relative module names (e.g. "OpenMayaUI")
        # instead of the full module path (e.g. "maya.api.OpenMayaUI");
        # attempt to resolve the module as a full path, and if we can't,
        # assume that it's a sibling of the current module
        try:
            resolve_name(class_module)
        except (ImportError, AttributeError):
            parent_package = module_name.rsplit(".", 1)[0]
            class_module = ".".join((parent_package, class_module))

        qualified_name = ".".join((class_module, cls.__qualname__))
        if override := BuiltinParser._TYPE_OVERRIDES.get(qualified_name):
            return override

        # no need to qualify builtin types or types from the same module
        if class_module in ("builtins", module_name):
            return cls.__qualname__
        return qualified_name

    def _parse_builtin_member(
        self,
        module_name: str,
        member_name: str,
        py_member: Any,
    ) -> Optional[
        docspec.Class
        | docspec.Function
        | docspec.Indirection
        | docspec.Module
        | docspec.Variable
    ]:
        self._members[member_name] = py_member
        docspec_member = None

        if member_name.startswith("_"):
            return
        elif inspect.ismodule(py_member):
            # Ignore modules
            return
        elif (mod := inspect.getmodule(py_member)) and not mod.__name__.startswith(
            "maya."
        ):
            # filter imported builtins
            return
        elif inspect.isclass(py_member):
            # we will add classes in a 2nd pass
            docspec_member = self.parse_class(module_name, member_name)
        elif callable(py_member):
            docspec_member = self.parse_function(module_name, member_name)
        else:
            docspec_member = self.parse_variable(module_name, member_name)

        return docspec_member

    def _get_args(
        self,
        module_name: str,
        function: Callable[[Any], Any],
        hints: Optional[List[docspec.FunctionSemantic]] = None,
    ) -> List[docspec.Argument]:
        try:
            args = self._arguments_from_signature(module_name, function)
        except RuntimeError:
            args = []

            if hints:
                if docspec.FunctionSemantic.CLASS_METHOD in hints:
                    args.append(
                        docspec.Argument(
                            location=NULL_LOCATION,
                            name="cls",
                            type=docspec.Argument.Type.POSITIONAL_ONLY,
                        )
                    )
                elif docspec.FunctionSemantic.INSTANCE_METHOD in hints:
                    args.append(
                        docspec.Argument(
                            location=NULL_LOCATION,
                            name="self",
                            type=docspec.Argument.Type.POSITIONAL_ONLY,
                        )
                    )

            args.extend(
                [
                    docspec.Argument(
                        location=NULL_LOCATION,
                        name="args",
                        type=docspec.Argument.Type.POSITIONAL_REMAINDER,
                    ),
                    docspec.Argument(
                        location=NULL_LOCATION,
                        name="kwargs",
                        type=docspec.Argument.Type.KEYWORD_REMAINDER,
                    ),
                ]
            )
        return args

    def get_return_type(self, function: Callable) -> str:
        try:
            signature = inspect.signature(function)
        except (ValueError, TypeError):
            return "Any"

        if function.__name__ == "__init__":
            return "None"

        if signature.return_annotation is inspect.Signature.empty:
            return "Any"

        return signature.return_annotation

    def _arguments_from_signature(
        self,
        module_name: str,
        function: Callable[[Any], Any],
    ) -> List[docspec.Argument]:
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
            raise RuntimeError(
                f"Failed to get the signature from {function!r}"
            ) from exc

        args = []
        for param in signature.parameters.values():
            args.append(self._param_to_argument(module_name, param))

        return args

    def _param_to_argument(
        self, module_name: str, param: inspect.Parameter
    ) -> docspec.Argument:
        """Convert an `inspect.Parameter` to a `docspec.Argument`"""

        arg_name = param.name
        arg_type = docspec.Argument.Type(param.kind)
        arg_decorations = []

        arg_datatype = None
        if param.annotation is not inspect.Signature.empty:
            arg_datatype = param.annotation
        elif param.default is not inspect.Signature.empty and param.default is not None:
            # guess datatype from default value
            arg_datatype = self._maybe_qualified(module_name, type(param.default))

        arg_default_value = None
        if param.default is not inspect.Signature.empty:
            if self._is_simple_literal(param.default, allow_none=True):
                arg_default_value = repr(param.default)
            else:
                arg_default_value = "..."

        return docspec.Argument(
            location=NULL_LOCATION,
            name=arg_name,
            type=arg_type,
            decorations=arg_decorations,
            datatype=arg_datatype,
            default_value=arg_default_value,
        )
