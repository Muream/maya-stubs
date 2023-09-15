from __future__ import annotations

import concurrent.futures
from collections.abc import Iterable, Iterator, Callable
from abc import ABC, abstractmethod
from typing import Any, Optional, TypeVar

import docspec
from attrs import define, field

__all__ = [
    "NULL_LOCATION",
]


NULL_LOCATION = docspec.Location("", 0)

T = TypeVar("T")
V = TypeVar("V")


@define
class Parser(ABC):
    executor: Optional[concurrent.futures.Executor] = None

    _members: dict[str, Any] = field(init=False, factory=dict)

    def add_member(self, name: str, member: Any) -> None:
        self._members[name] = member

    def map(self, f: Callable[[T], V], items: Iterable[T]) -> Iterator[V]:
        if self.executor is not None:
            return self.executor.map(f, items)
        return map(f, items)

    @abstractmethod
    def parse_package(self, name: str) -> list[docspec.Module]:
        ...

    @abstractmethod
    def parse_module(self, name: str) -> docspec.Module:
        ...

    @abstractmethod
    def parse_class(self, name: str) -> docspec.Class:
        ...

    @abstractmethod
    def parse_function(self, name: str) -> docspec.Function:
        ...

    @abstractmethod
    def parse_variable(self, name: str) -> docspec.Variable:
        ...


def degraded_function(name: str) -> docspec.Function:
    return docspec.Function(
        location=NULL_LOCATION,
        name=name,
        docstring=None,
        modifiers=None,
        args=[
            docspec.Argument(
                NULL_LOCATION,
                "*args",
                docspec.Argument.Type.POSITIONAL_REMAINDER,
                decorations=None,
                datatype="Any",
                default_value=None,
            ),
            docspec.Argument(
                NULL_LOCATION,
                "**kwargs",
                docspec.Argument.Type.KEYWORD_REMAINDER,
                decorations=None,
                datatype="Any",
                default_value=None,
            ),
        ],
        return_type="Any",
        decorations=None,
        semantic_hints=[],
    )
