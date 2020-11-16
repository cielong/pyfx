import functools

import click


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
            raise click.ClickException(e)
    return wrapper
