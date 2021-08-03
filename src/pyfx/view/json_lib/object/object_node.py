from overrides import overrides

from .object_end_node import ObjectEndNode
from .object_start_widget import ObjectStartWidget
from .object_unexpanded_widget import ObjectUnexpandedWidget
from ..json_composite_end_node import JSONCompositeEndNode
from ..json_composite_node import JSONCompositeNode


class ObjectNode(JSONCompositeNode):
    """
    implementation of JSON `object` type node
    aside from fields in a JSONNode, it contains the following elements:
    * value: dict
    * children: dict to store correspondent node
    * sorted_children_key_list: internal type to keep track of a sorted key list
                                and thus keep track of the next, previous node
                                of each child
    * sorted_children_key_list_size: size of key
    """

    def __init__(self, key: str, value: dict, node_factory,
                 parent=None, display_key=True):
        super().__init__(key, value, node_factory, parent, display_key)
        self._children = {}
        self._sorted_children_key_list = sorted(value.keys())
        # avoid re-calculation
        self._sorted_children_key_list_size = len(
            self._sorted_children_key_list
        )

    @overrides
    def collapse_all(self):
        for key, child in self._children.items():
            if isinstance(child, (JSONCompositeNode, JSONCompositeEndNode)):
                child.collapse_all()
        self.toggle_expanded()

    @overrides
    def has_children(self):
        return self._sorted_children_key_list_size != 0

    @overrides
    def get_first_child(self):
        if not self.has_children():
            return None
        return self._get_child_node(self._sorted_children_key_list[0])

    @overrides
    def get_last_child(self):
        if not self.has_children():
            return None
        return self._get_child_node(
            self._sorted_children_key_list[
                self._sorted_children_key_list_size - 1
            ]
        )

    @overrides
    def prev_child(self, key):
        index = self._sorted_children_key_list.index(key)
        if index == 0:
            return None
        return self._get_child_node(self._sorted_children_key_list[index - 1])

    @overrides
    def next_child(self, key):
        index = self._sorted_children_key_list.index(key)
        if index == self._sorted_children_key_list_size - 1:
            return None
        return self._get_child_node(self._sorted_children_key_list[index + 1])

    def _get_child_node(self, key):
        if not self.has_children():
            return None
        elif key not in self._children:
            self._children[key] = self._load_child_node(key)
        return self._children[key]

    def _load_child_node(self, key):
        value = self.get_value()[key]
        return self._node_factory.create_node(
            key, value, parent=self, display_key=True
        )

    # ====================================================================== #
    # ui                                                                     #
    # ====================================================================== #

    @overrides
    def load_unexpanded_widget(self):
        return ObjectUnexpandedWidget(self, self.is_display_key())

    @overrides
    def load_start_widget(self):
        return ObjectStartWidget(self, self.is_display_key())

    @overrides
    def load_end_node(self):
        return ObjectEndNode(self)
