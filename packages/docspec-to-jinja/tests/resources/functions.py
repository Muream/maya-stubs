def do_nothing():
    """This function does nothing"""


def fully_annotated(a: int, b: int) -> int:
    """Fully annotated and documented function

    Args:
        a (int): first argument
        b (int): second argument

    Returns:
        int: return description
    """


def no_return_type(a: int, b: int):
    ...


def no_annotations(a, b):
    ...


def with_positional_only(a, /, b, c):
    ...


def with_keywords_only(a, *, b, c):
    ...


@decorated
def decorated_function():
    ...


@decorated(arg1="Hello world")
def decorated_function_with_args():
    ...
