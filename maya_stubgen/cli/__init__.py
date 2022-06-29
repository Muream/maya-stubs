import logging

import click

from ..utils import initialize_maya, uninitialize_maya
from .generate_stubs import generate_stubs

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


cli.add_command(generate_stubs)
