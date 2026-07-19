"""
Logging-System
"""

import logging
from logging.handlers import RotatingFileHandler
from config.constants import LOG_DIR

def create_logger():

    logger = logging.getLogger("NeonDJ")

    logger.setLevel(logging.DEBUG)

    if logger.handlers:

        return logger
    
    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = RotatingFileHandler(

        LOG_DIR / "application.log",

        maxBytes= 2_000_000,

        backupCount=5,

        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    console = logging.StreamHandler()

    console.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.addHandler(console)

    return logger