import click

from .core import Controller


@click.command(name="pyfx")
@click.argument("file")
def main(file: str):
    """
    pyfx main entry point.

    It loads data from a JSON file FILE and use :py:mod:`pyfx.view.view` to
    display the content.
    """
    Controller().main(file)
