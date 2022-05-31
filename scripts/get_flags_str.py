"""This retrieves the flags definition strings from cmds.help("command")"""
import inspect
import logging
import sys
from typing import *

logger = logging.Logger(__name__)


def cmds_functions() -> List[Callable]:
    from maya import cmds

    return inspect.getmembers(cmds, callable)


def get_flags_strings():
    from maya import cmds

    lines = []
    for func, _ in cmds_functions():
        try:
            doc = cmds.help(func)
        except RuntimeError:
            pass
        else:
            include_func = True
            for line in doc.splitlines():
                line = line.strip()
                if line.startswith("-"):
                    if include_func:
                        lines.append("")
                        lines.append(func)
                        include_func = False

                    lines.append(line)

    return "\n".join(lines)


def main():
    try:
        import maya.standalone

        maya.standalone.initialize()
    except BaseException:
        pass
    else:
        logger.info("Maya Standalone Initialized succesfully")

    flags_strings = get_flags_strings()
    try:
        out_file = sys.argv[1]
    except IndexError:
        print(flags_strings)
    else:
        with open(out_file, "w") as f:
            f.write(flags_strings)


if __name__ == "__main__":
    main()
