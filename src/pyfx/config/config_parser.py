import pathlib

import dacite
import yamale
from first import first

from .config import Configuration
from ..cli_utils import exit_on_exception


@exit_on_exception
def parse(config_file):
    return ConfigurationParser().parse(config_file)


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
        return yamale.make_schema(ConfigurationParser.__SCHEMA_PATH)

    # noinspection PyBroadException
    @staticmethod
    def __load_config(config_file):
        if config_file is None:
            config_file = first(ConfigurationParser.__CONFIG_PATHS, key=lambda path: path.exists())
        return yamale.make_data(config_file)
