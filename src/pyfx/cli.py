import click

from .cli_utils import load_from_clipboard, parse
from .core import Controller
from .logging import setup_logger

STDIN = 'stdin'


@click.command(name="pyfx")
@click.option("-c", "--config-file", type=click.Path(exists=True),
              help="Absolute path of pyfx config file")
@click.option("-x", "--from-clipboard", is_flag=True, default=False,
              help="Read JSON from clipboard")
@click.argument("file", type=click.Path(exists=True, dir_okay=False), nargs=-1,
                help="JSON file")
def main(file, config_file, from_clipboard):
    """
    pyfx command line entry point.

    It loads data from a JSON file FILE and opens pyfx UI for browsing.
    """
    setup_logger()
    config = parse(config_file)
    if len(file) > 1:
        raise click.BadArgumentUsage("pyfx does not support multi JSON files.")

    controller = Controller(config)
    if from_clipboard:
        serialized_json = load_from_clipboard()
        controller.run_with_serialized_json(serialized_json)
    elif len(file) == 1:
        controller.run_with_file(file[0])
    else:
        text_stream = click.get_text_stream(STDIN)
        controller.run_with_text_stream(text_stream)
