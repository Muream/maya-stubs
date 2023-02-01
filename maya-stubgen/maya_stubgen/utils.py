import logging
import shutil
import sys
import time
from contextlib import contextmanager
from pathlib import Path
from typing import *

logger = logging.getLogger(__name__)

try:
    import maya
except:
    HAS_MAYA = False
else:
    HAS_MAYA = True

# List of plugins that contain commands that should have generated stubs
PLUGINS = ["invertShape.mll", "poseInterpolator.mll"]


def initialize_maya():
    if not HAS_MAYA:
        return

    logger.info("Initializing Maya Standalone")

    try:
        import maya.standalone

        maya.standalone.initialize()
    except BaseException:
        logger.error("Failed to initialize Maya Standalone")
    else:

        for plugin in PLUGINS:
            try:
                maya.cmds.loadPlugin(plugin)
            except BaseException:
                logger.warning("Couldn't load %s", plugin)

        # remove maya's handler
        logging.getLogger().handlers.pop()
        logger.success("Maya Standalone Initialized")


def uninitialize_maya():
    if not HAS_MAYA:
        return

    logger.info("Uninitializing Maya Standalone")
    try:
        import maya.standalone

        maya.standalone.uninitialize()
    except BaseException:
        logger.error("Failed to uninitialize Maya Standalone")
    else:
        logger.success("Maya Standalone Uninitialized")
    finally:
        temp_maya_app_dir = Path() / "temp" / "maya_app_dir"

        shutil.rmtree(temp_maya_app_dir, ignore_errors=True)


@contextmanager
def maya_standalone():
    initialize_maya()
    yield
    uninitialize_maya()


def timed(func):
    def wrap_func(*args, **kwargs):
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter()
        logger.info("Function %s executed in %ss", func.__name__, t2 - t1)
        return result

    return wrap_func
