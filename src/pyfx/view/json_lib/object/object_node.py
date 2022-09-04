from overrides import overrides

from .object_end_node import ObjectEndNode
from .object_start_widget import ObjectStartWidget
from .object_unexpanded_widget import ObjectUnexpandedWidget
from ..json_composite_end_node import JSONCompositeEndNode
from ..json_composite_node import JSONCompositeNode
from ..json_node_creator import JSONNodeCreator


class ObjectNodeCreator(JSONNodeCreator):
    """
    A factory to create `ObjectNode`.
    """

    def __init__(self, node_factory):
        self._node_factory = node_factory

    @overrides
    def create_node(self, key, value, **kwargs):
        if isinstance(value, dict):
            return ObjectNode(key, value, self._node_factory, **kwargs)
        elif hasattr(value, "__dict__"):
            return ObjectNode(key, value.__dict__, self._node_factory, **kwargs)
        return None


class ObjectNode(JSONCompositeNode):
    """
    Implementation of JSON `object` type node.
    Aside from fields in a JSONNode, it contains the following elements:

    * children_nodes: dict to store correspondent node, note this may not have
                      the same order as `children_key_list`, as each node of
                      `children_nodes` is created during runtime.
    * children_key_list: internal type to keep track of the insertion ordered
                         key list. Thus keep track of the next, previous node
                         of each child.
    """

    def __init__(self, key: str, value: dict, node_factory,
                 parent=None, display_key=True):
        super().__init__(key, value, node_factory, parent, display_key)
        self._children_nodes = dict()
        # Starting from Python 3.7, dict maintains insertion order. Thus, we
        # don't need to sort the keys to maintain a sorted list.
        self._children_key_list = list(value.keys())

    @overrides
    def collapse_all(self):
        for key, child in self._children_nodes.items():
            if isinstance(child, (JSONCompositeNode, JSONCompositeEndNode)):
                child.collapse_all()
        self.toggle_expanded()

    @overrides
    def has_children(self):
        return len(self._value) != 0

    @overrides
    def get_first_child(self):
        if not self.has_children():
            return None
        return self._get_child_node(self._children_key_list[0])

    @overrides
    def get_last_child(self):
        if not self.has_children():
            return None
        return self._get_child_node(self._children_key_list[-1])

    @overrides
    def prev_child(self, key):
        index = self._children_key_list.index(key)
        if index == 0:
            return None
        return self._get_child_node(self._children_key_list[index - 1])

    @overrides
    def next_child(self, key):
        index = self._children_key_list.index(key)
        if index == len(self._children_key_list) - 1:
            return None
        return self._get_child_node(self._children_key_list[index + 1])

    def _get_child_node(self, key):
        if not self.has_children():
            return None
        elif key not in self._children_nodes:
            self._children_nodes[key] = self._load_child_node(key)
        return self._children_nodes[key]

    def _load_child_node(self, key):
        value = self.get_value()[key]
        return self._node_factory.create_node(key, value, parent=self,
                                              display_key=True)

    @overrides
    def load_unexpanded_widget(self):
        return ObjectUnexpandedWidget(self, self.is_display_key())

    @overrides
    def load_start_widget(self):
        return ObjectStartWidget(self, self.is_display_key())

    @overrides
    def load_end_node(self):
        return ObjectEndNode(self)
