import importlib.resources
import pathlib

import dacite
import yamale
from first import first
from yamale import YamaleError
from yamale.validators import DefaultValidators

from ..error import PyfxException
from .validators import Options
from .config import Configuration


def parse(config_file=None):
    try:
        return ConfigurationParser().parse(config_file)
    except YamaleError as e:
        # catch and raise a more user-friendly error
        message = '\n'.join(e.message.split('\n')[1:]).strip()
        raise PyfxException(f"Configuration Error: {message}.")


class ConfigurationParser:
    __CONFIG_PATHS = [
        pathlib.Path.home() / ".config" / "pyfx" / "config.yml",
    ]

    def __init__(self):
        self._schema = self.__load_schema()

    def parse(self, config_file=None):
        config = self.__load_config(config_file)
        yamale.validate(self._schema, config)
        # config is composed as [(config, path)...]
        return dacite.from_dict(data_class=Configuration, data=config[0][0])

    @staticmethod
    def __load_schema():
        validators = DefaultValidators.copy()
        validators[Options.tag] = Options

        contents = importlib.resources.read_text("pyfx.config", "schema.yml")
        return yamale.make_schema(validators=validators, content=contents)

    # noinspection PyBroadException
    @staticmethod
    def __load_config(config_file):
        if config_file is None:
            config_file = first(
                ConfigurationParser.__CONFIG_PATHS,
                key=lambda path: path.exists()
            )
        if config_file is not None:
            return yamale.make_data(path=config_file)

        # use default config
        contents = importlib.resources.read_text("pyfx.config", "config.yml")
        return yamale.make_data(content=contents)
