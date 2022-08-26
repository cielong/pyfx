import sys

import click
import os

import pyperclip

from .__version__ import __version__
from .cli_utils import exit_on_exception
from .config import parse
from .app import PyfxApp
from .logging import setup_logger
from .model import DataSourceType


@click.command(name="pyfx")
@click.help_option()
@click.version_option(__version__)
@click.option("--debug", is_flag=True, default=False,
              help="Enable debug level logging.")
@click.option("-c", "--config-file", type=click.Path(exists=True),
              help="Absolute path of pyfx config file")
@click.option("-x", "--from-clipboard", is_flag=True, default=False,
              help="Read JSON from clipboard")
@click.argument("file", type=click.Path(exists=True, dir_okay=False), nargs=-1)
@exit_on_exception
def main(file, config_file, from_clipboard, debug):
    """
    pyfx command line entry point.

    It loads JSON from various sources and opens Pyfx's UI for browsing.

    Examples
    --------

    1. load JSON from clipboard

         pyfx -x | --from-clipboard

    2. load JSON from file

         pyfx data.json

    3. load JSON from pipe

         cat data.json | pyfx
    """
    setup_logger(debug)
    config = parse(config_file)
    app = PyfxApp(config)
    if from_clipboard:
        serialized_json = pyperclip.paste().strip()
        app.run(DataSourceType.STRING, serialized_json)
    elif len(file) == 1:
        app.run(DataSourceType.FILE, file[0])
    else:
        serialized_json = '\n'.join(click.get_text_stream('stdin').readlines())
        with open(os.ctermid()) as f:
            # We replace sys.stdin at the top of the cli, to improve
            # system testability.
            # close the current stdin (pipe)
            sys.stdin.close()
            # replace stdin with the new one
            sys.stdin = f
            app.run(DataSourceType.STRING, serialized_json)
