import click
from loguru import logger

from .core import Controller

logger.remove()
logger.add("/tmp/pyfx.log", level='DEBUG', rotation='5MB', retention="10 days",
           format="<green>{time}</green> {module}.{function} <level>{message}</level>")


@click.command(name="pyfx")
@click.argument("file")
def main(file: str):
    """
    pyfx command line entry point.

    It loads data from a JSON file FILE and opens pyfx UI for browsing.
    """
    Controller().run_with_file(file)
