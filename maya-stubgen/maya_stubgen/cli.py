import cProfile
import logging
import pstats
from pathlib import Path
from typing import Optional

import click

from .stubgen import build_docs, build_stubs, get_modules


logger = logging.getLogger("maya_stubgen")


@click.group
def cli() -> None:
    pass


@cli.command()
@click.option(
    "-p",
    "--profile",
    is_flag=True,
    help="Whether to profile the code using cProfile. "
    "The profile file can be found in temp/generate_stubs.prof",
)
@click.option(
    "-m",
    "--module",
    type=str,
    multiple=True,
    help="Modules to generate docspec files for. Can be specified multiple times. "
    "By default, docspec files are generated for all modules.",
)
@click.option(
    "--members",
    type=str,
    default=None,
    help="If specified, docspec files will only be generated for members matching this regex.",
)
def generate_docspec(
    profile: bool,
    module: Optional[list[str]],
    members: Optional[str],
) -> None:
    if profile:
        profiler = cProfile.Profile()
        profiler.enable()

        get_modules(module, member_pattern=members)

        profiler.disable()

        stats = pstats.Stats(profiler)
        prof_file = (Path() / "temp" / "dump_docspec.prof").resolve()
        prof_file.parent.mkdir(exist_ok=True)
        stats.dump_stats(str(prof_file))
    else:
        get_modules(module, member_pattern=members)


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
@click.option(
    "-p",
    "--profile",
    is_flag=True,
    help="Whether to profile the code using cProfile. "
    "The profile file can be found in temp/generate_stubs.prof",
)
@click.option(
    "-rc",
    "--reuse-cache",
    is_flag=True,
    help="whether to re-use the docspec cache from the previous run. "
    "Use this if you are only making changes to the stub generation side of things, not the parsing.",
)
@click.option(
    "-m",
    "--module",
    type=str,
    multiple=True,
    help="Modules to generate stubs for. Can be specified multiple times. "
    "By default, stubs are generated for all modules.",
)
@click.option(
    "--members",
    type=str,
    default=None,
    help="If specified, stubs will only be generated for members matching this regex.",
)
def generate_stubs(
    path: Path,
    profile: bool,
    reuse_cache: bool,
    module: Optional[list[str]],
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
@click.option(
    "-p",
    "--profile",
    is_flag=True,
    help="Whether to profile the code using cProfile. "
    "The profile file can be found in temp/generate_docs.prof",
)
@click.option(
    "-rc",
    "--reuse-cache",
    is_flag=True,
    help="whether to re-use the docspec cache from the previous run. "
    "Use this if you are only making changes to the docs generation side of things, not the parsing.",
)
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
