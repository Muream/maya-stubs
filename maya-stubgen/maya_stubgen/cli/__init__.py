import cProfile
import logging
import pstats
from pathlib import Path
from typing import List, Optional

import click

from .generate_stubs import build_docs, build_stubs, dump_docspec

logger = logging.getLogger("maya_stubgen")


@click.group
def cli():
    pass


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
@click.option("-m", "--module", type=str, multiple=True)
@click.option("--members", type=str, default=None)
def generate_docspec(
    profile: bool, module: Optional[List[str]], members: Optional[str]
) -> None:
    if profile:
        profiler = cProfile.Profile()
        profiler.enable()

        dump_docspec(module, member_pattern=members)

        profiler.disable()

        stats = pstats.Stats(profiler)
        prof_file = (Path() / "temp" / "dump_docspec.prof").resolve()
        prof_file.parent.mkdir(exist_ok=True)
        stats.dump_stats(str(prof_file))
    else:
        dump_docspec(module, member_pattern=members)


@cli.command()
@click.argument(
    "path",
    type=click.Path(
        exists=False,
        dir_okay=True,
        file_okay=False,
        resolve_path=True,
        path_type=Path,
    ),
)
@click.option("-p", "--profile", is_flag=True)
@click.option("-rc", "--reuse-cache", is_flag=True)
@click.option("-m", "--module", type=str, multiple=True)
@click.option("--members", type=str, default=None)
def generate_stubs(
    path: Path,
    profile: bool,
    reuse_cache: bool,
    module: Optional[List[str]],
    members: Optional[str],
) -> None:
    logger.info("Generating Stubs")

    path.mkdir(parents=True, exist_ok=True)

    if profile:
        profiler = cProfile.Profile()
        profiler.enable()

        build_stubs(path, reuse_cache, whitelist=module, member_pattern=members)

        profiler.disable()

        stats = pstats.Stats(profiler)
        prof_file = (Path() / "temp" / "generate_stubs.prof").resolve()
        prof_file.parent.mkdir(exist_ok=True)
        stats.dump_stats(str(prof_file))
    else:
        build_stubs(path, reuse_cache, whitelist=module, member_pattern=members)


@cli.command()
@click.argument(
    "path",
    type=click.Path(
        exists=True,
        dir_okay=True,
        file_okay=False,
        resolve_path=True,
        path_type=Path,
    ),
)
@click.option("-p", "--profile", is_flag=True)
@click.option("-rc", "--reuse-cache", is_flag=True)
def generate_docs(path: Path, profile: bool, reuse_cache: bool) -> None:
    logger.info("Generating Docs")

    if profile:
        profiler = cProfile.Profile()
        profiler.enable()

        build_docs(path, reuse_cache)

        profiler.disable()

        stats = pstats.Stats(profiler)
        prof_file = (Path() / "temp" / "generate_docs.prof").resolve()
        prof_file.parent.mkdir(exist_ok=True)
        stats.dump_stats(str(prof_file))
    else:
        build_docs(path, reuse_cache)
