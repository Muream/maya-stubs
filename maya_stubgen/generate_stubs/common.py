from __future__ import annotations

import inspect
from abc import ABC, abstractclassmethod, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from textwrap import indent
from typing import *

from typing_extensions import Self

STUB_HEADER = """\
# fmt: off
from typing import *
from typing_extensions import Self
from _typeshed import Incomplete
\n
"""

TAB_LENGTH = 4
TAB = TAB_LENGTH * " "


class MISSING:
    """Used when a value is not specified as opposed to specified but purposefully None."""


class FunctionType(Enum):
    function = "function"
    method = "method"
    classmethod = "classmethod"
    staticmethod = "staticmethod"
    getter = "property"
    setter = "{name}.setter"


@dataclass
class StubItem(ABC):
    @abstractclassmethod
    def from_object(cls, obj: type, name: Optional[str] = None) -> Self:
        ...

    @property
    @abstractmethod
    def stub(self) -> str:
        ...

    def __str__(self) -> str:
        return self.stub


@dataclass
class Class(StubItem):
    name: str
    parent: Optional[str] = None
    members: List[Class | Function | Variable] = field(default_factory=list)

    @classmethod
    def from_object(cls, obj: type, name: str = None) -> Self:
        if name is None:
            name = obj.__name__

        try:
            parent = obj.mro()[1].__name__
        except:
            parent = None

        skip = ["__class__"]

        members = []
        for member_name, member in inspect.getmembers(obj):
            if member_name in skip:
                continue

            if inspect.isclass(member):
                members.append(Class.from_object(member))
            elif callable(member):
                method = Function.from_object(member, member_name, FunctionType.method)
                members.append(method)
            elif inspect.isgetsetdescriptor(member):
                getter = Function.from_object(member, member_name, FunctionType.getter)
                setter = Function.from_object(member, member_name, FunctionType.setter)
                members.append(getter)
                members.append(setter)
            else:
                members.append(
                    Variable(member_name, type(member), member, is_argument=True)
                )

        return cls(name, parent, members)

    @property
    def stub(self):
        stub = f"class {self.name}"

        if self.parent:
            stub += f"({self.parent})"

        stub += ":\n"

        for member in self.members:
            stub += indent(member.stub, TAB)
            stub += "\n"

        return stub


@dataclass
class Variable(StubItem):
    name: str
    type: Type = Any
    value: Any = MISSING
    is_argument: bool = False

    def __post_init__(self):
        if self.name == "self":
            self.type = Self

    @classmethod
    def from_object(cls, obj: type, name: Optional[str] = None) -> Self:
        raise NotImplementedError

    @property
    def type_str(self) -> str:
        try:
            return self.type.__name__
        except:
            return str(self.type).replace("typing.", "")

    @property
    def stub(self) -> str:

        res = self.name

        if self.type:
            res += f": {self.type_str}"

        if self.value is not MISSING:
            if self.is_argument:
                res += " = ..."
            # else:
            #     res += f" = {self.value}"

        return res


@dataclass
class Function:
    name: str
    arguments: List[Variable] = field(default_factory=list)
    docstring: Optional[str] = None
    return_type: Type = Any
    function_type: FunctionType = FunctionType.function

    def __post_init__(self):
        self.docstring = self._process_docstring(self.docstring)
        if self.function_type is FunctionType.method:
            if len(self.arguments) == 0 or self.arguments[0].name != "self":
                self.arguments.insert(0, Variable("self", Self, is_argument=True))

    @classmethod
    def from_object(
        cls,
        obj: type,
        name: Optional[str] = None,
        function_type=FunctionType.function,
    ) -> Self:
        if name is None:
            name = obj.__name__

        try:
            signature = inspect.signature(obj)
        except:
            arguments = [Variable("*args"), Variable("**kwargs")]
            return_type = Any
        else:
            arguments = []
            for arg_name, parameter in signature.parameters.items():
                annotation = (
                    parameter.annotation
                    if parameter.annotation is not parameter.empty
                    else Any
                )
                value = (
                    parameter.default
                    if parameter.default is not parameter.empty
                    else MISSING
                )
                arg = Variable(arg_name, annotation, value, is_argument=True)
                arguments.append(arg)
            return_type = (
                signature.return_annotation
                if signature.return_annotation is not signature.empty
                else Any
            )
        docstring = obj.__doc__

        return Function(name, arguments, docstring, return_type, function_type)

    @property
    def stub(self):
        stub = self.signature
        stub += " ..."

        return stub

    @staticmethod
    def _process_docstring(docstring: Optional[str]) -> str:
        if docstring is None:
            return None

        docstring = docstring.strip()

        lines = docstring.splitlines()

        if len(lines) == 0:
            return None
        elif len(lines) == 1:
            docstring = f'"""{docstring}"""'
        else:
            docstring = f'"""{docstring}\n"""'

        docstring = indent(docstring, TAB)

        return docstring

    @property
    def arguments_str(self) -> str:
        return ", ".join(map(str, self.arguments))

    @property
    def return_type_str(self):
        return str(self.return_type).replace("typing.", "")

    @property
    def signature(self):
        if self.function_type not in [FunctionType.function, FunctionType.method]:
            signature = f"@{self.function_type.value.format(name=self.name)}\n"
        else:
            signature = ""

        signature += f"def {self.name}({self.arguments_str})"

        if self.return_type:
            signature += f" -> {self.return_type_str}"

        signature += ":"

        return signature
