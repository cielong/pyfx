"""
Utility libraries for CLI.
"""
import functools

import click
from loguru import logger


def exit_on_exception(func):
    """
    A decorator which exit the current click application when there's
    unexpected error and print the error message to the stderr.
    """
    # noinspection PyBroadException
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if not isinstance(e.__str__(), str):
                e = Exception(
                    f"Unknown error {type(e)}. Please consider create an issue "
                    f"at https://github.com/cielong/pyfx/issues."
                )
            logger.opt(exception=True).\
                error(e)
            raise click.ClickException(e.__str__())
    return wrapper
