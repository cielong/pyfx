import click
from pyfx.browser import Browser


@click.command(name="pyfx")
@click.argument("file")
def main(file: str):
    Browser(file).main()
