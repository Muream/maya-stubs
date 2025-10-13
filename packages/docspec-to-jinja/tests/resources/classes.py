class A:
    """This is my beautiful class Docstring."""

    #: This is the docstring for attrib_1
    attrib_1: int = 2
    attrib_2: str = "Hello World"

    def __init__(self) -> None:
        pass

    def method(self) -> None:
        """This is a regular method"""

    @classmethod
    def classmethod(cls) -> None:
        """This is a class method"""

    @staticmethod
    def classmethod() -> None:
        """This is a class method"""

    @property
    def prop(self) -> str:
        """This is a property getter"""

    @prop.setter
    def prop(self) -> str:
        """This is a property setter"""

    @prop.deleter
    def prop(self) -> str:
        """This is a property deleter"""


class B(A):
    """This is my beautiful class Docstring."""
