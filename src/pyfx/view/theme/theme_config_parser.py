import pathlib

import dacite
from overrides import overrides

from ...config.config_error import ConfigurationError
from ...config.config_transformer import AbstractConfigurationTransformer

from .theme import Theme


def create_palette(theme):
    try:
        return ThemeConfigurationTransformer.transform(theme)
    except Exception:
        raise ConfigurationError(
            f"Failed to load color scheme from theme name {theme}."
            f"Please consider create an issue at "
            f"https://github.com/cielong/pyfx/issues."
        )


class ThemeConfigurationTransformer(AbstractConfigurationTransformer):
    """ Configuration parser that create keymappers from configuration """

    __HERE = pathlib.Path(__file__).parent.resolve()
    THEMES = {
        "basic": None,
    }

    @classmethod
    @overrides(check_signature=False)
    def transform(cls, theme, *args, **kwargs):
        config_file = cls.THEMES[theme]
        if config_file is None:
            return Theme().palette()

        return dacite.from_dict(
            data_class=Theme, data=cls.load_yaml(theme)).palette()
