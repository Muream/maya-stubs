import logging
from contextlib import contextmanager
from typing import *

logger = logging.getLogger(__name__)


def initialize_maya():
    logger.info("Initializing Maya Standalone")
    try:
        import maya.standalone

        logging.getLogger().handlers

        maya.standalone.initialize()
    except BaseException:
        logger.error("Failed to initialize Maya Standalone")
    else:
        # remove maya's handler
        logging.getLogger().handlers.pop()
        logger.success("Maya Standalone Initialized")


def uninitialize_maya():
    logger.info("Uninitializing Maya Standalone")
    try:
        import maya.standalone

        maya.standalone.uninitialize()
    except BaseException:
        logger.error("Failed to uninitialize Maya Standalone")
    else:
        logger.success("Maya Standalone Uninitialized")


@contextmanager
def maya_standalone():
    initialize_maya()
    yield
    uninitialize_maya()
