import cProfile
import logging
import pstats
from pathlib import Path

import click

from ..utils import initialize_maya, uninitialize_maya
from .generate_stubs import build_docs, build_stubs, dump_docspec

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
def generate_docspec(profile: bool) -> None:
    logger.info("Dumping Docspec")

    if profile:
        profiler = cProfile.Profile()
        profiler.enable()

        dump_docspec()

        profiler.disable()

        stats = pstats.Stats(profiler)
        prof_file = (Path() / "temp" / "dump_docspec.prof").resolve()
        prof_file.parent.mkdir(exist_ok=True)
        stats.dump_stats(str(prof_file))
    else:
        dump_docspec()


@cli.command()
@click.option("-p", "--profile", is_flag=True)
@click.option("-rc", "--reuse-cache", is_flag=True)
def generate_stubs(profile: bool, reuse_cache: bool) -> None:
    logger.info("Generating Stubs")

    if profile:
        profiler = cProfile.Profile()
        profiler.enable()

        build_stubs(reuse_cache)

        profiler.disable()

        stats = pstats.Stats(profiler)
        prof_file = (Path() / "temp" / "generate_stubs.prof").resolve()
        prof_file.parent.mkdir(exist_ok=True)
        stats.dump_stats(str(prof_file))
    else:
        build_stubs(reuse_cache)


@cli.command()
@click.option("-p", "--profile", is_flag=True)
@click.option("-rc", "--reuse-cache", is_flag=True)
def generate_docs(profile: bool, reuse_cache: bool) -> None:
    logger.info("Generating Docs")

    if profile:
        profiler = cProfile.Profile()
        profiler.enable()

        build_docs(reuse_cache)

        profiler.disable()

        stats = pstats.Stats(profiler)
        prof_file = (Path() / "temp" / "generate_docs.prof").resolve()
        prof_file.parent.mkdir(exist_ok=True)
        stats.dump_stats(str(prof_file))
    else:
        build_docs(reuse_cache)
