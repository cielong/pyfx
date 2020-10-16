import click

from loguru import logger

from .core import Controller

logger.add("/tmp/pyfx.log", level='DEBUG', rotation='5MB', retention="10 days",
           format="<green>{time}</green> <level>{message}</level>")


@click.command(name="pyfx")
@click.argument("file")
def main(file: str):
    """
    pyfx main entry point.

    It loads data from a JSON file FILE and use :py:mod:`pyfx.view.view` to
    display the content.
    """
    Controller().main(file)
