import json
from abc import ABC, abstractmethod
from enum import Enum
from json import JSONDecodeError

from loguru import logger
from overrides import overrides


class DataSourceType(Enum):
    FILE = 1
    STREAM = 2
    STRING = 3
    VARIABLE = 4


class DataSource(ABC):
    """
    Abstract class that represents a JSON datasource
    """
    @abstractmethod
    def read_json(self):
        raise NotImplementedError("Loading JSON results in undefined actions.")


class FileDataSource(DataSource):
    """
    Reading JSON from a file.
    """

    def __init__(self, file_name):
        self._file_name = file_name

    @overrides
    def read_json(self):
        try:
            with open(self._file_name, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.opt(exception=True) \
                .error("Load JSON file {} failed with: {}", self._file_name, e)
            raise e


class TextStreamDataSource(DataSource):
    """
    Load JSON from a text stream
    """

    def __init__(self, text_stream):
        self._text_stream = text_stream

    def read_json(self):
        try:
            return json.load(self._text_stream)
        except Exception as e:
            logger.opt(exception=True) \
                .error("Load JSON data from text stream {} failed with: {}",
                       self._text_stream, e)
            raise e
        finally:
            self._text_stream.close()


class StringDataSource(DataSource):
    """
    Load JSON from its serialized string
    """

    def __init__(self, json_str):
        self._json_str = json_str

    def read_json(self):
        try:
            return json.loads(self._json_str)
        except JSONDecodeError as e:
            raise e
        except Exception as e:
            logger.opt(exception=True).\
                error("Load JSON data from serialized json {} failed with: {}",
                      self._json_str, e)
            raise e


class InMemoryDataSource(DataSource):
    """
    Load JSON from a variable
    """

    def __init__(self, var):
        self._var = var

    def read_json(self):
        return self._var


DATA_SOURCES = {
    DataSourceType.FILE: FileDataSource,
    DataSourceType.STREAM: TextStreamDataSource,
    DataSourceType.STRING: StringDataSource,
    DataSourceType.VARIABLE: InMemoryDataSource
}


def create_data_source(type):
    datasource = DATA_SOURCES.get(type)
    if datasource is None:
        raise ValueError(f"Cannot find data source type {type}")
    return datasource
