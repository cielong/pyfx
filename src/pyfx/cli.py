import json

import click
from .logging import log_config

from .core import Controller

STDIN = 'stdin'


@click.command(name="pyfx")
@click.argument("file", type=click.Path(exists=True), nargs=-1)
def main(file):
    """
    pyfx command line entry point.

    It loads data from a JSON file FILE and opens pyfx UI for browsing.
    """
    log_config()
    if len(file) > 1:
        raise ValueError("pyfx does not support multi JSON files.")

    if len(file) == 1:
        Controller().run_with_file(file[0])
    else:
        text_stream = click.get_text_stream(STDIN)
        Controller().run_with_text_stream(text_stream)
