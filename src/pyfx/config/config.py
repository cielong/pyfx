from dataclasses import dataclass

from ..view.view_config import ViewConfiguration


@dataclass
class Configuration:
    view: ViewConfiguration = ViewConfiguration()
