"""
Separate file for logging configuration.
"""
from loguru import logger


def setup_logger(debug):
    """Set up """
    logger.remove()
    level = "DEBUG" if debug else "INFO"
    logger.add(
        "/tmp/pyfx.log",
        level=level,
        rotation='5MB',
        retention="10 days",
        format="<green>{time}</green> {module}.{function} "
               "<level>{message}</level>"
    )
