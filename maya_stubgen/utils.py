import logging
import os
from contextlib import contextmanager
from pathlib import Path
from typing import *

logger = logging.getLogger(__name__)


def initialize_maya():
    logger.info("Initializing Maya Standalone")

    temp_maya_app_dir = Path() / "temp" / "maya_app_dir"
    temp_maya_app_dir.mkdir(parents=True, exist_ok=True)

    os.environ["MAYA_APP_DIR"] = str(temp_maya_app_dir)
    os.environ["MAYA_MODULE_PATH"] = ""

    try:
        import maya.standalone

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
