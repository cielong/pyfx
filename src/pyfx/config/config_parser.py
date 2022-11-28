import pathlib

import dacite
import yamale
from first import first
from loguru import logger
from yamale import YamaleError

from pyfx.error import PyfxException
from pyfx.config import PyfxConfiguration
from pyfx.config.yaml import yaml_path


def load(data_file, data_class):
    """Loads a configuration into a dataclass."""

    try:
        data = yamale.make_data(data_file.absolute())
        # Result of `yamale#make_data` is composed as [(config, path)...]
        return dacite.from_dict(data=data[0][0], data_class=data_class)
    except Exception as e:
        logger.opt(exception=True).error(e)
        raise PyfxException(f"Load {data_file} into {data_class} failed with "
                            "unknown error.", e)


def parse(config_file=None):
    """Parses and validates the configuration file."""

    try:
        schema_file = yaml_path / "config_schema.yml"
        schema = yamale.make_schema(schema_file.absolute())

        config_file = first([
            # user provided config file
            pathlib.Path(config_file) if config_file is not None else None,
            # ~/.config/pyfx/config.yml
            pathlib.Path.home() / ".config" / "pyfx" / "config.yml",
            # ./yaml/config.yml
            yaml_path / "config.yml"
        ], key=lambda p: p is not None and p.exists() and p.is_file())
        config = yamale.make_data(config_file.absolute())

        # Validates the configuration file
        yamale.validate(schema, config)

        # Result of `yamale#make_data` is composed as [(config, path)...]
        return dacite.from_dict(data=config[0][0], data_class=PyfxConfiguration)
    except YamaleError as e:
        # Catches and raises an error with a more user-friendly error message
        message = '\n'.join(e.message.split('\n')[1:]).strip()
        raise PyfxException(f"Parse and validate Pyfx configuration file "
                            f"failed with error: {message}.")
    except Exception as e:
        logger.opt(exception=True).error(e)
        raise PyfxException("Parse Pyfx configuration file failed with unkown "
                            "error.", e)
