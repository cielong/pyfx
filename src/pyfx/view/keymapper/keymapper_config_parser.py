import importlib.resources

import dacite
from loguru import logger
from overrides import overrides

from ...config.config_transformer import AbstractConfigurationTransformer
from ...error import PyfxException

from .keymapper import KeyMapper


def create_keymapper(mode):
    try:
        return KeyMapperConfigurationParser.transform(mode)
    except Exception as e:
        logger.opt(exception=True).error(e)
        raise PyfxException(
            f"Failed to load key-mapping from mode name {mode}. "
            f"Please consider create an issue at "
            f"https://github.com/cielong/pyfx/issues."
        )


class KeyMapperConfigurationParser(AbstractConfigurationTransformer):
    """ Configuration parser that create keymappers from configuration """

    MODES = {
        "basic": None,
        "emacs": ("pyfx.view.keymapper.modes", "emacs.yml"),
        "vim": ("pyfx.view.keymapper.modes", "vim.yml")
    }

    @classmethod
    @overrides(check_signature=False)
    def transform(cls, mode, *args, **kwargs):
        mode_config = cls.MODES[mode]
        if mode_config is None:
            return KeyMapper()

        with importlib.resources.path(mode_config[0], mode_config[1]) as path:
            return dacite.from_dict(
                data_class=KeyMapper, data=cls.load_yaml(path.resolve())
            )
