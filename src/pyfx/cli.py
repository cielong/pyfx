import click

from .core import Controller


@click.command(name="pyfx")
@click.argument("file")
def main(file: str):
    Controller().main(file)
