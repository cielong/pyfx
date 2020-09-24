from abc import abstractmethod

from pyfx.ui.models.json_simple_node import JSONSimpleNode

from typing import Union


class JSONCompositeNode(JSONSimpleNode):

    @abstractmethod
    def has_children(self) -> bool:
        pass

    @abstractmethod
    def get_first_child(self) -> Union["JSONSimpleNode", None]:
        pass

    @abstractmethod
    def get_last_child(self) -> Union["JSONSimpleNode", None]:
        pass
