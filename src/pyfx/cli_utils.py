import functools

import click
import pyperclip

from pyfx import config


def exit_on_exception(func):
    """
    A decorator which exit the current click application when there's unexpected error
    and print the error message to the stderr.
    """
    # noinspection PyBroadException
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if not isinstance(e.__str__(), str):
                e = Exception(f"Unknown error {type(e)}. Please consider create an issue at "
                              "https://github.com/cielong/pyfx/issues.")
            raise click.ClickException(e)
    return wrapper


@exit_on_exception
def load_from_clipboard():
    return pyperclip.paste().strip()


@exit_on_exception
def parse(*args, **kwargs):
    return config.parse(*args, **kwargs)
