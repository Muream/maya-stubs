import cProfile
import logging
import pstats
from pathlib import Path

import click

from ..utils import initialize_maya, uninitialize_maya
from .generate_stubs import generate_stubs as _generate_stubs

logger = logging.getLogger("maya_stubgen")


@click.group
def cli():
    initialize_maya()


@cli.result_callback()
def result(result):
    uninitialize_maya()


@cli.command
def test_log():
    logger.setLevel(logging.DEBUG)

    logger.debug("Debug")
    logger.info("Info")
    logger.success("Success")
    logger.warning("Warning")
    logger.error("Error")
    logger.critical("Critical")


@cli.command()
@click.option("-p", "--profile", is_flag=True)
def generate_stubs(profile: bool) -> None:
    logger.info("Generating Stubs")

    if profile:
        profiler = cProfile.Profile()
        profiler.enable()

        _generate_stubs()

        profiler.disable()

        stats = pstats.Stats(profiler)
        prof_file = (Path() / "temp" / "generate_stubs.prof").resolve()
        prof_file.parent.mkdir(exist_ok=True)
        stats.dump_stats(str(prof_file))
    else:
        _generate_stubs()
