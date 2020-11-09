import pathlib

import dacite
import yamale

from .config import Configuration


class ConfigurationParser:

    __HERE = pathlib.Path(__file__).parent.resolve()
    __SCHEMA_PATH = (__HERE / "schema.yml").resolve()
    __CONFIG_PATH = (__HERE / "config.yml").resolve()

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

    @staticmethod
    def __load_config(config_file):
        if config_file is None:
            config_file = ConfigurationParser.__CONFIG_PATH
        return yamale.make_data(config_file)
