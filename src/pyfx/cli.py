import json
import os
import sys

import click
import pyperclip

from .__version__ import __version__
from .app import PyfxApp
from .cli_utils import exit_on_exception
from .cli_utils import is_stdin_readable
from .error import PyfxException


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
    print("Loading data.", file=sys.stdout, flush=True)
    if from_clipboard:
        data = json.loads(pyperclip.paste().strip())
    elif is_stdin_readable():
        # sys.stdin is immediately readable
        data = json.loads('\n'.join(click.get_text_stream('stdin').readlines()))
        # Replace sys.stdin at the top of the cli, to improve
        # system testability.
        # close the current stdin (pipe)
        sys.stdin.close()
        # replace stdin with a new one
        sys.stdin = open(os.ctermid())
    elif len(file) == 1:
        with open(file[0], 'r') as f:
            data = json.load(f)
    else:
        raise PyfxException("Failed to read JSON data. "
                            "Notice Pyfx only support reading single file.")

    print("Starting Pyfx UI.", file=sys.stdout, flush=True)
    # Init Pyfx and start the UI
    PyfxApp(data=data, config=config_file, debug_mode=debug).run()
    print("Exited Pyfx.", file=sys.stdout, flush=True)
