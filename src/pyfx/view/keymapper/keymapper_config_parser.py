import pathlib

import dacite
import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from .keymapper import KeyMapper


def create_keymapper(config):
    return KeyMapperConfigurationParser.create_keymapper(config)


class KeyMapperConfigurationParser:
    """ Configuration parser that create keymappers from configuration """

    __HERE = pathlib.Path(__file__).parent.resolve()
    MODES = {
        "basic": None,
        "emacs": __HERE / "modes" / "emacs.yml",
        "vim": __HERE / "modes" / "vim.yml"
    }

    @staticmethod
    def create_keymapper(config):
        mode_config = KeyMapperConfigurationParser.MODES[config.mode]
        if mode_config is None:
            return KeyMapper()

        keymapper = KeyMapperConfigurationParser._load_yaml(mode_config)
        return dacite.from_dict(data_class=KeyMapper, data=keymapper)

    @staticmethod
    def _load_yaml(mode_config):
        with mode_config.open() as f:
            return yaml.load(f, Loader=Loader)

