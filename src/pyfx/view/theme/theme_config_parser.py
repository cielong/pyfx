import pathlib

import dacite
import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from .theme import Theme


def create_palette(config):
    return ThemeConfigurationParser.create_palette(config)


class ThemeConfigurationParser:
    """ Configuration parser that create keymappers from configuration """

    __HERE = pathlib.Path(__file__).parent.resolve()
    MODES = {
        "basic": None,
    }

    @staticmethod
    def create_palette(config):
        mode_config = ThemeConfigurationParser.MODES[config.theme]
        if mode_config is None:
            return Theme().palette()

        keymapper = ThemeConfigurationParser._load_yaml(mode_config)
        return dacite.from_dict(data_class=Theme, data=keymapper).palette()

    @staticmethod
    def _load_yaml(mode_config):
        with mode_config.open() as f:
            return yaml.load(f, Loader=Loader)

