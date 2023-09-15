from collections.abc import Iterator
from typing import List, Optional, Union

import docstring_parser
from docspec import (
    ApiObject,
    Class,
    Docstring,
    Function,
    Module,
    Variable,
    Argument,
    FunctionSemantic,
)
from jinja2 import Environment, PackageLoader, select_autoescape

from .docstring import process_google_docstring

__version__ = "0.1.0"

env = Environment(
    loader=PackageLoader("docspec_to_jinja"),
    autoescape=select_autoescape(),
    trim_blocks=True,
)


def render(api_object: ApiObject, template_type: str) -> str:
    if isinstance(api_object, Module):
        return render_module(api_object, template_type)

    if isinstance(api_object, Class):
        return render_class(api_object, template_type)

    if isinstance(api_object, Function):
        return render_function(api_object, template_type)

    if isinstance(api_object, Docstring):
        return render_docstring(api_object, template_type)

    if isinstance(api_object, Variable):
        return render_variable(api_object, template_type)

    raise TypeError(f"Rendering {api_object.__class__.__name__} is not supported.")


def get_imports(module: Module) -> List[str]:
    # remove type arguments
    types = (type_name.split("[", 1)[0] for type_name in _get_module_types(module))
    return sorted(
        set(type_name.rsplit(".", 1)[0] for type_name in types if "." in type_name)
    )


def _get_module_types(module: Module) -> Iterator[str]:
    for member in module.members:
        if isinstance(member, Variable):
            yield from _get_variable_types(member)
        elif isinstance(member, Function):
            yield from _get_function_types(member)
        elif isinstance(member, Class):
            yield from _get_class_types(member)


def _get_class_types(cls: Class) -> Iterator[str]:
    if cls.bases:
        yield from cls.bases

    for member in cls.members:
        if isinstance(member, Variable):
            yield from _get_variable_types(member)
        elif isinstance(member, Function):
            yield from _get_function_types(member)
        elif isinstance(member, Class):
            yield from _get_class_types(member)


def _get_function_types(func: Function) -> Iterator[str]:
    if func.return_type:
        yield func.return_type

    for arg in func.args:
        yield from _get_argument_types(arg)


def _get_argument_types(arg: Argument) -> Iterator[str]:
    if arg.datatype:
        yield arg.datatype


def _get_variable_types(var: Variable) -> Iterator[str]:
    if var.datatype:
        yield var.datatype


def render_module(module: Module, template_type: str, nested: bool = False) -> str:
    template = env.get_template(f"{template_type}/module.j2")

    return template.render(
        module=module,
        render_docstring=render_docstring,
        render_function=render_function,
        render_class=render_class,
        nested=nested,
        imports=get_imports(module),
    )


def render_class(cls: Class, template_type: str, nested: bool = False) -> str:
    template = env.get_template(f"{template_type}/class.j2")

    return template.render(
        cls=cls,
        render_docstring=render_docstring,
        render_function=render_function,
        nested=nested,
    )


def render_function(
    function: Function,
    template_type: str,
    nested: bool = False,
) -> str:
    template = env.get_template(f"{template_type}/function.j2")

    return template.render(
        function=function,
        render_docstring=render_docstring,
        nested=nested,
    )


def render_docstring(
    docstring: Docstring,
    template_type: str,
    nested: bool = False,
) -> str:
    template = env.get_template(f"{template_type}/docstring.j2")

    parsed_docstring = docstring_parser.parse(docstring.content)

    if parsed_docstring.style == docstring_parser.Style.GOOGLE:
        parsed_docstring = process_google_docstring(parsed_docstring)

    rendered_docstring = template.render(doc=parsed_docstring, nested=nested)

    return rendered_docstring


def render_variable(
    variable: Variable,
    template_type: str,
    nested: bool = False,
) -> str:
    template = env.get_template(f"{template_type}/variable.j2")

    return template.render(variable=variable, nested=nested)
