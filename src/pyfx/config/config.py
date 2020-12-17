from dataclasses import dataclass

from ..view import ViewConfiguration


@dataclass
class Configuration:
    view: ViewConfiguration = ViewConfiguration()
