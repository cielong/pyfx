from abc import ABC

import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class AbstractConfigurationTransformer(ABC):
    """
    Read a named configuration and transform it into a separate / concrete
    configuration.
    E.g. read a predefined theme name and convert the name into its actual
    color scheme.
    """

    @classmethod
    def transform(cls, **kwargs):
        raise NotImplementedError(
            f"{type(cls)} does not override #transform method"
        )

    @staticmethod
    def load_yaml(config_file):
        with config_file.open() as f:
            return yaml.load(f, Loader=Loader)
