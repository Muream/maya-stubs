"""A Docspec parser for python builtins.

As opposed to docspec-python, this is uses runtime introspection instead of static analysis.
"""
from __future__ import annotations

import importlib
import inspect
import logging
import re
from typing import Any, Callable, List, Optional

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

    def parse_class(self, module_name: str, name: str) -> docspec.Class:
        logger.debug("Parsing class: %s", name)

        cls = self._members[name]

        parser = BuiltinParser()

        docstring = docspec.Docstring(NULL_LOCATION, inspect.getdoc(cls) or "")
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

        parent_members = []
        if parent is not None:
            parent_members = [id(member[1]) for member in inspect.getmembers(parent)]

        for member_name, member in inspect.getmembers(cls):
            if member_name in ignored_members:
                continue

            parser.add_member(member_name, member)

            is_inherited = id(member) in parent_members
            if is_inherited:
                continue

            if inspect.isclass(member):
                members.append(parser.parse_class(module_name, member_name))
            elif callable(member):
                method = parser.parse_function(module_name, member_name, is_method=True)
                members.append(method)
            # elif inspect.isgetsetdescriptor(member):
            #     getter = Function.from_object(member, member_name, FunctionType.getter)
            #     setter = Function.from_object(member, member_name, FunctionType.setter)
            #     members.append(getter)
            #     members.append(setter)
            else:
                members.append(parser.parse_variable(module_name, member_name))

        return docspec.Class(
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

    def parse_function(
        self, module_name: str, name: str, is_method: bool = False
    ) -> docspec.Function:
        logger.debug("Parsing function: %s", name)
        function: Callable = self._members[name]

        docstring_content = inspect.getdoc(function)
        docstring = (
            docspec.Docstring(NULL_LOCATION, docstring_content)
            if docstring_content
            else None
        )

        args = self._get_args(module_name, function, is_method)
        return_type = self.get_return_type(function)

        semantic_hints = []
        if is_method:
            semantic_hints.append(docspec.FunctionSemantic.INSTANCE_METHOD)

        return docspec.Function(
            location=NULL_LOCATION,
            name=name,
            docstring=docstring,
            modifiers=[],
            args=args,
            return_type=return_type,
            decorations=[],
        )

    def parse_variable(self, module_name: str, name: str) -> docspec.Variable:
        logger.debug("Parsing variable: %s", name)

        variable = self._members[name]

        return docspec.Variable(
            location=NULL_LOCATION,
            name=name,
            docstring=None,
            datatype=variable.__class__.__name__,
            value=str(variable),
            modifiers=[],
            semantic_hints=[],
        )

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

        elif inspect.isclass(py_member):
            # we will add classes in a 2nd pass
            docspec_member = self.parse_class(module_name, member_name)
        elif callable(py_member):
            docspec_member = self.parse_function(module_name, member_name)
        else:
            # member has to be a variable now?
            # docspec_member = parse_builtin_variable(name, py_member)
            pass

        return docspec_member

    def _get_args(
        self,
        module_name: str,
        function: Callable[[Any], Any],
        is_method: bool = False,
    ) -> List[docspec.Argument]:
        try:
            args = self._arguments_from_signature(module_name, function)
        except RuntimeError:
            args = []

            if is_method:
                args.append(
                    docspec.Argument(
                        location=NULL_LOCATION,
                        name="self",
                        type=docspec.Argument.Type.POSITIONAL_ONLY,
                        decorations=[],
                        datatype=None,
                        default_value=None,
                    )
                )

            for _arg in ["*args", "**kwargs"]:
                arg = docspec.Argument(
                    location=NULL_LOCATION,
                    name=_arg,
                    type=docspec.Argument.Type.POSITIONAL,
                    decorations=[],
                    datatype="Any",
                    default_value=None,
                )
                args.append(arg)
        return args

    def get_return_type(self, function: Callable) -> str:
        try:
            signature = inspect.signature(function)
        except Exception:
            return "Any"

        return (
            signature.return_annotation
            if signature.return_annotation is not inspect.Signature.empty
            else "Any"
        )

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

        arg_name = str(param)
        arg_type = docspec.Argument.Type(param.kind)
        arg_decorations = []
        arg_datatype = (
            param.annotation
            if param.annotation is not inspect.Signature.empty
            else None
        )
        arg_default_value = (
            str(param.default) if param.default is not inspect.Signature.empty else None
        )
        return docspec.Argument(
            location=NULL_LOCATION,
            name=arg_name,
            type=arg_type,
            decorations=arg_decorations,
            datatype=arg_datatype,
            default_value=arg_default_value,
        )
