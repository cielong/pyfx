from overrides import overrides

from pyfx.ui.models import object_node  # to avoid circular dependency
from pyfx.ui.models.atomic_node import AtomicNode
from pyfx.ui.models.json_composite_node import JSONCompositeNode
from pyfx.ui.widgets.array_widget import ArrayWidget

from typing import Union


class ArrayNode(JSONCompositeNode):
    """
    implementation of JSON `array` type node
    aside from fields in :ref:`JSONSimpleNode`, it contains the following elements:
    * value: list
    * size: length of the current array
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

    def get_child_node(self, index: int):
        if not self.has_children():
            return None
        elif index not in self._children:
            self._children[index] = self.load_child_node(index)

        return self._children[index]

    def load_child_node(self, index: int):
        value = self.get_value()[index]
        if isinstance(value, list):
            return ArrayNode(str(index), value, self, False)
        elif isinstance(value, dict):
            return object_node.ObjectNode(str(index), value, self, False)
        else:
            return AtomicNode(str(index), value, self, False)

    @overrides
    def get_first_child(self) -> Union["JSONSimpleNode", None]:
        if not self.has_children():
            return None
        return self.get_child_node(0)

    @overrides
    def get_last_child(self) -> Union["JSONSimpleNode", None]:
        if not self.has_children():
            return None
        return self.get_child_node(self._size - 1)

    def prev_child(self, key: str) -> Union["JSONSimpleNode", None]:
        index = int(key)
        if index == 0:
            return None
        return self.get_child_node(index - 1)

    def next_child(self, key: str) -> Union["JSONSimpleNode", None]:
        index = int(key)
        if index == self._size - 1:
            return None
        return self.get_child_node(index + 1)

    # =================================================================================== #
    # ui                                                                                  #
    # =================================================================================== #

    @overrides
    def load_widget(self) -> ArrayWidget:
        return ArrayWidget(self, self.is_display_key())
