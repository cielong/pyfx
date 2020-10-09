from typing import Union

from overrides import overrides

from .array_end_node import ArrayEndNode
from .array_start_widget import ArrayStartWidget
from .array_unexpanded_widget import ArrayUnexpandedWidget
from .. import node_factory
from ..json_composite_node import JSONCompositeNode


class ArrayNode(JSONCompositeNode):
    """
    implementation of JSON `array` type node
    """

    def __init__(self,
                 key: str,
                 value: list,
                 parent: Union["object_node", "ArrayNode", None] = None,
                 display_key: bool = True
                 ):
        super().__init__(key, value, parent, display_key)
        self._children = {}
        self._size = len(value)

    @overrides
    def has_children(self) -> bool:
        return self._size != 0

    @overrides
    def get_first_child(self) -> Union["JSONSimpleNode", None]:
        if not self.has_children():
            return None
        return self._get_child_node(0)

    @overrides
    def get_last_child(self) -> Union["JSONSimpleNode", None]:
        if not self.has_children():
            return None
        return self._get_child_node(self._size - 1)

    @overrides
    def prev_child(self, key: str) -> Union["JSONSimpleNode", None]:
        index = int(key)
        if index == 0:
            return None
        return self._get_child_node(index - 1)

    @overrides
    def next_child(self, key: str) -> Union["JSONSimpleNode", None]:
        index = int(key)
        if index == self._size - 1:
            return None
        return self._get_child_node(index + 1)

    def _get_child_node(self, index: int):
        if not self.has_children():
            return None

        if index < 0 or index >= self._size:
            raise TypeError(
                f"index ${index} is out of bound ${self._size}in {type(self)}#get_child_node."
            )
        elif index not in self._children:
            self._children[index] = self._load_child_node(index)

        return self._children[index]

    def _load_child_node(self, index: int):
        value = self.get_value()[index]
        return node_factory.NodeFactory.create_node(str(index), value, self, False)

    # =================================================================================== #
    # ui                                                                                  #
    # =================================================================================== #

    @overrides
    def load_start_widget(self):
        return ArrayStartWidget(self, self.is_display_key())

    @overrides
    def load_unexpanded_widget(self):
        return ArrayUnexpandedWidget(self, self.is_display_key())

    @overrides
    def load_end_node(self):
        return ArrayEndNode(self)
