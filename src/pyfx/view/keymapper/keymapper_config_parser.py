import pathlib

import dacite
from loguru import logger
from overrides import overrides

from ...config.config_transformer import AbstractConfigurationTransformer
from ...config.config_error import ConfigurationError

from .keymapper import KeyMapper


def create_keymapper(mode):
    try:
        return KeyMapperConfigurationParser.transform(mode)
    except Exception as e:
        logger.opt(exception=True).error(e)
        raise ConfigurationError(
            f"Failed to load key-mapping from mode name {mode}."
            f"Please consider create an issue at "
            f"https://github.com/cielong/pyfx/issues."
        )


class KeyMapperConfigurationParser(AbstractConfigurationTransformer):
    """ Configuration parser that create keymappers from configuration """

    __HERE = pathlib.Path(__file__).parent.resolve()
    MODES = {
        "basic": None,
        "emacs": __HERE / "modes" / "emacs.yml",
        "vim": __HERE / "modes" / "vim.yml"
    }

    @classmethod
    @overrides(check_signature=False)
    def transform(cls, mode, *args, **kwargs):
        mode_config = cls.MODES[mode]
        if mode_config is None:
            return KeyMapper()

        return dacite.from_dict(
            data_class=KeyMapper, data=cls.load_yaml(mode_config)
        )
