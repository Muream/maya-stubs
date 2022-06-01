import inspect
import logging
from enum import Enum
from pathlib import Path
from typing import *

import click
from maya import cmds

logger = logging.Logger(__name__)


class SynopsisType(Enum):
    all = "all"
    synopsis = "synopsis"
    flags = "flags"

    def __str__(self) -> str:
        return self.value


def cmds_functions() -> List[Callable]:
    return inspect.getmembers(cmds, callable)


def synopsis_for_type(type: SynopsisType):
    logger.info("Generating Synopsis for type : %s", type)
    all_lines = []

    include_synopsis = type is type is SynopsisType.all or type is SynopsisType.synopsis
    include_flags = type is type is SynopsisType.all or type is SynopsisType.flags

    for func, _ in cmds_functions():
        try:
            doc = cmds.help(func)
        except RuntimeError:
            pass
        else:
            lines = []

            synopsis = f"Synopsis: {func}"

            for line in doc.splitlines():
                line = line.strip()

                if "Synopsis" in line:
                    synopsis = line

                if line.startswith("-"):
                    if include_flags:
                        lines.append(line)

            if type is SynopsisType.all:
                synopsis = f"\n{synopsis}"

            if include_synopsis:
                lines.insert(0, synopsis)

        all_lines.extend(lines)

    return "\n".join(all_lines).strip()


@click.command
@click.option(
    "--type",
    default=SynopsisType.all.value,
    type=click.Choice(SynopsisType.__members__),
)
def get_cmds_synopsis(type):

    type = SynopsisType(type)
    cmds_synopsis = synopsis_for_type(type)

    out_file = Path() / "temp" / "synopsis" / f"{type}.txt"
    out_file.parent.mkdir(parents=True, exist_ok=True)

    with open(out_file, "w") as f:
        f.write(cmds_synopsis)

    logger.success("Generated synopsis: %s", out_file)
