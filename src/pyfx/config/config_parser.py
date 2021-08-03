import pathlib

import dacite
import yamale
from first import first
from yamale import YamaleError
from yamale.validators import DefaultValidators

from .config_error import ConfigurationError
from .validators import Options
from .config import Configuration


def parse(config_file=None):
    try:
        return ConfigurationParser().parse(config_file)
    except YamaleError as e:
        # catch and raise a more user-friendly error
        message = '\n'.join(e.message.split('\n')[1:]).strip()
        raise ConfigurationError(message)


class ConfigurationParser:

    __CLASS_DIR = pathlib.Path(__file__).parent.resolve()
    __SCHEMA_PATH = __CLASS_DIR / "schema.yml"

    __CONFIG_PATHS = [
        pathlib.Path.home() / ".config" / "pyfx" / "config.yml",
        __CLASS_DIR / "config.yml"
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
        return yamale.make_schema(
            ConfigurationParser.__SCHEMA_PATH, validators=validators
        )

    # noinspection PyBroadException
    @staticmethod
    def __load_config(config_file):
        if config_file is None:
            config_file = first(
                ConfigurationParser.__CONFIG_PATHS,
                key=lambda path: path.exists()
            )
        return yamale.make_data(config_file)
