import click

from .config.config_parser import parse
from .core import Controller
from .logging import setup_logger

STDIN = 'stdin'


@click.command(name="pyfx")
@click.option("-c", "--config-file", type=click.Path(exists=True))
@click.argument("file", type=click.Path(exists=True), nargs=-1)
def main(file, config_file):
    """
    pyfx command line entry point.

    It loads data from a JSON file FILE and opens pyfx UI for browsing.
    """
    setup_logger()
    config = parse(config_file)
    if len(file) > 1:
        raise click.BadArgumentUsage("pyfx does not support multi JSON files.")

    controller = Controller(config)
    if len(file) == 1:
        controller.run_with_file(file[0])
    else:
        text_stream = click.get_text_stream(STDIN)
        controller.run_with_text_stream(text_stream)
