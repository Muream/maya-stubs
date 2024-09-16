"""Abstract parser defining the interface used by all the different parsers"""

from abc import ABC, abstractmethod
from collections.abc import Callable, Iterable, Iterator
from typing import Any, TypeVar

import docspec
from attrs import define, field

T = TypeVar("T")
V = TypeVar("V")

__all__ = [
    "Parser",
]


@define
class Parser(ABC):
    _members: dict[str, Any] = field(init=False, factory=dict)

    def add_member(self, name: str, member: Any) -> None:
        self._members[name] = member

    def map(self, f: Callable[[T], V], items: Iterable[T]) -> Iterator[V]:
        return map(f, items)

    @abstractmethod
    def parse_package(self, name: str) -> list[docspec.Module]: ...

    @abstractmethod
    def parse_module(self, name: str) -> docspec.Module: ...

    @abstractmethod
    def parse_class(self, module_name: str, name: str) -> docspec.Class: ...

    @abstractmethod
    def parse_function(self, module_name: str, name: str) -> docspec.Function: ...

    @abstractmethod
    def parse_variable(self, module_name: str, name: str) -> docspec.Variable: ...
