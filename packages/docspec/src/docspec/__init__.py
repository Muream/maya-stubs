from __future__ import annotations

from typing import Union

from dataclasses import dataclass, field
from enum import Enum


@dataclass
class Docstring:
    #: The content of the docstring. While the #Docstring class is a subclass of `str` and holds
    #: the same value as *content*, using the #content property should be preferred as the inheritance
    #: from the `str` class may be removed in future versions.
    content: str


@dataclass
class Decoration:
    """
    Represents a decorator on a #Class or #Function.
    """

    #: The name of the decorator (i.e. the text between the `@` and `(`). In languages that support it,
    #: this may be a piece of code.
    name: str

    #: Decorator arguments as plain code (including the leading and trailing parentheses). This is
    #: `None` when the decorator does not have call arguments. This is deprecated in favor of #arglist.
    #: For backwards compatibility, loaders may populate both the #args and #arglist fields.
    args: str | None = None

    #: Decorator arguments, one item per argument. For keyword arguments, the keyword name and equals
    #: sign preceed the argument value expression code.
    arglist: list[str] | None = None


class VariableSemantic(Enum):
    """
    A list of well-known properties and behaviour that can be attributed to a variable/constant.
    """

    #: The #Variable object is an instance variable of a class.
    INSTANCE_VARIABLE = "INSTANCE_VARIABLE"

    #: The #Variable object is a static variable of a class.
    CLASS_VARIABLE = "CLASS_VARIABLE"

    #: The #Variable object represents a constant value.
    CONSTANT = "CONSTANT"


@dataclass
class Variable:
    """
    Represents a variable assignment (e.g. for global variables (often used as constants) or class members).
    """

    name: str

    docstring: Docstring | None = None

    #: The datatype associated with the assignment as code.
    datatype: str | None = None

    #: The value of the variable as code.
    value: str | None = None

    #: A list of language-specific modifiers that were used to declare this #Variable object.
    modifiers: list[str] = field(default_factory=list)

    #: A list of hints that express semantics of this #Variable object which are not otherwise
    #: derivable from the context.
    semantic_hints: list[VariableSemantic] = field(default_factory=list)


@dataclass
class Argument:
    """
    Represents a #Function argument.
    """

    class Type(Enum):
        """
        The type of the argument. This is currently very Python-centric, however most other languages should be able
        to represent the various argument types with a subset of these types without additions (e.g. Java or TypeScript
        only support #Positional and #PositionalRemainder arguments).
        """

        #: A positional only argument. Such arguments are denoted in Python like this: `def foo(a, b, /): ...`
        POSITIONAL_ONLY = "POSITIONAL_ONLY"

        #: A positional argument, which may also be given as a keyword argument. Basically that is just a normal
        #: argument as you would see most commonly in Python function definitions.
        POSITIONAL = "POSITIONAL"

        #: An argument that denotes the capture of additional positional arguments, aka. "args" or "varags".
        POSITIONAL_REMAINDER = "POSITIONAL_REMAINDER"

        #: A keyword-only argument is denoted in Python like thisL `def foo(*, kwonly): ...`
        KEYWORD_ONLY = "KEYWORD_ONLY"

        #: An argument that captures additional keyword arguments, aka. "kwargs".
        KEYWORD_REMAINDER = "KEYWORD_REMAINDER"

    #: The name of the argument.
    name: str

    #: The argument type.
    type: Type

    #: The datatype/type annotation of this argument as a code string.
    datatype: str | None = None

    #: The default value of the argument as a code string.
    default_value: str | None = None


class FunctionSemantic(Enum):
    """
    A list of well-known properties and behaviour that can be attributed to a function.
    """

    #: The function is abstract.
    ABSTRACT = "ABSTRACT"

    #: The function is final.
    FINAL = "FINAL"

    #: The function is a coroutine.
    COROUTINE = "COROUTINE"

    #: The function does not return.
    NO_RETURN = "NO_RETURN"

    #: The function is an instance method.
    INSTANCE_METHOD = "INSTANCE_METHOD"

    #: The function is a classmethod.
    CLASS_METHOD = "CLASS_METHOD"

    #: The function is a staticmethod.
    STATIC_METHOD = "STATIC_METHOD"

    #: The function is a property getter.
    PROPERTY_GETTER = "PROPERTY_GETTER"

    #: The function is a property setter.
    PROPERTY_SETTER = "PROPERTY_SETTER"

    #: The function is a property deleter.
    PROPERTY_DELETER = "PROPERTY_DELETER"


@dataclass
class Function:
    """
    Represents a function definition. This can be in a #Module for plain functions or in a #Class for methods.
    The #decorations need to be introspected to understand if the function has a special purpose (e.g. is it a
    `@property`, `@classmethod` or `@staticmethod`?).
    """

    name: str

    docstring: Docstring | None = None

    #: A list of modifiers used in the function definition. For example, the only valid modifier in
    #: Python is "async".
    modifiers: list[str] | None = None

    #: A list of the function arguments.
    args: list[Argument] = field(default_factory=list)

    #: The return type of the function as a code string.
    return_type: str | None = None

    #: A list of decorations used on the function.
    decorations: list[Decoration] | None = None

    #: A list of hints that describe the object.
    semantic_hints: list[FunctionSemantic] = field(default_factory=list)


class ClassSemantic(Enum):
    """
    A list of well-known properties and behaviour that can be attributed to a class.
    """

    #: The class describes an interface.
    INTERFACE = "INTERFACE"

    #: The class is abstrac
    ABSTRACT = "ABSTRACT"

    #: The class is final.
    FINAL = "FINAL"

    #: The class is an enumeration.
    ENUM = "ENUM"


@dataclass
class Class:
    """
    Represents a class definition.
    """

    name: str

    docstring: Docstring | None = None

    #: The metaclass used in the class definition as a code string.
    metaclass: str | None = None

    #: The list of base classes as code strings.
    bases: list[str] | None = None

    #: A list of decorations used in the class definition.
    decorations: list[Decoration] | None = None

    #: A list of the classes members. #Function#s in a class are to be considered instance methods of
    #: that class unless some information about the #Function indicates otherwise.
    members: list[Member] = field(default_factory=list)

    #: A list of language-specific modifiers that were used to declare this #Variable objec
    modifiers: list[str] = field(default_factory=list)

    #: A list of hints that describe the objec
    semantic_hints: list[ClassSemantic] = field(default_factory=list)


@dataclass
class Module:
    """
    Represents a module, basically a named container for code/API objects. Modules may be nested in other modules.
    Be aware that for historical reasons, some loaders lile #docspec_python by default do not return nested modules,
    even if nesting would be appropriate (and instead the #Module.name simply contains the fully qualified name).
    """

    name: str

    docstring: Docstring | None = None

    #: A list of module members.
    members: list[Member] = field(default_factory=list)


Member = Union[Variable, Function, Class, Module]
ApiObject = Union[Module, Class, Function, Variable]
