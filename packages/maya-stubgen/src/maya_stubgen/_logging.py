import logging
from typing import Any, cast

SUCCESS = logging.INFO + 5


class SuccessLogger(logging.Logger):
    def success(self, message: Any, *args: Any) -> None:
        self.log(SUCCESS, message, *args)


logging.addLevelName(SUCCESS, "SUCCESS")
logging.setLoggerClass(SuccessLogger)


def getLogger(name: str) -> SuccessLogger:
    return cast(SuccessLogger, logging.getLogger(name))


class CustomFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629"""

    grey = "\x1b[38;21m"
    blue = "\x1b[38;5;39m"
    yellow = "\x1b[38;5;226m"
    green = "\x1b[32m"
    red = "\x1b[38;5;196m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, fmt: str):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            SUCCESS: self.green + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset,
        }

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def init_logger() -> None:
    # Create custom logger logging all five levels
    root_logger = getLogger("maya_stubgen")
    root_logger.setLevel(logging.DEBUG)

    # Define format for logs
    stdout_fmt = "%(levelname)8s | %(message)s"

    # Create stdout handler for logging to the console (logs all five levels)
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(CustomFormatter(stdout_fmt))

    file_handler = logging.FileHandler("maya_stubgen.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(stdout_fmt))

    # Add both handlers to the logger
    root_logger.addHandler(stdout_handler)
    root_logger.addHandler(file_handler)


init_logger()
