from pathlib import Path

import docspec_python

import docspec_to_jinja


import pytest


@pytest.mark.skip()
def test_render_module():
    pass


def test_render_classes():
    classes_file_path = Path("tests/resources/classes.py")

    module = docspec_python.parse_python_module(classes_file_path)

    rendered_classes = []
    for cls in module.members:
        rendered_class = docspec_to_jinja.render_class(
            cls,
            template="pyi/class.pyi",
        )
        rendered_classes.append(rendered_class)

    content = "\n".join(rendered_classes)

    path = Path() / "tmp" / f"classes.pyi"
    path.parent.mkdir(exist_ok=True)

    with path.open("w", encoding="utf-8") as f:
        f.write(content)


def test_render_function():
    functions = Path("tests/resources/functions.py")

    module = docspec_python.parse_python_module(functions)

    rendered_functions = []
    for function in module.members:
        rendered_function = docspec_to_jinja.render_function(
            function,
            template="pyi/function.pyi",
        )
        rendered_functions.append(rendered_function)

    content = "\n".join(rendered_functions)

    path = Path() / "tmp" / f"functions.pyi"
    path.parent.mkdir(exist_ok=True)

    with path.open("w", encoding="utf-8") as f:
        f.write(content)
