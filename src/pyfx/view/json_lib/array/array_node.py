from overrides import overrides

from .array_end_node import ArrayEndNode
from .array_start_widget import ArrayStartWidget
from .array_unexpanded_widget import ArrayUnexpandedWidget
from ..json_composite_end_node import JSONCompositeEndNode
from ..json_composite_node import JSONCompositeNode
from ..json_node_creator import JSONNodeCreator


class ArrayNodeCreator(JSONNodeCreator):
    """A factory to create :class:`.ArrayNode`."""

    def __init__(self, node_factory):
        self._node_factory = node_factory

    @overrides
    def create_node(self, key, value, **kwargs):
        if isinstance(value, list):
            return ArrayNode(key, value, self._node_factory, **kwargs)
        return None


class ArrayNode(JSONCompositeNode):
    """Implementation of JSON `array` type node."""

    def __init__(self, key: str, value: list, node_factory,
                 parent=None, display_key=True):
        """
        * children_nodes: dict to store correspondent node.
            It stores list#index -> node, as each node of
            :attr:`_children_nodes` is created during runtime.
        """
        super().__init__(key, value, node_factory, parent, display_key)
        self._children_nodes = {}

    @overrides
    def collapse_all(self):
        for index, child in self._children_nodes.items():
            if isinstance(child, (JSONCompositeNode, JSONCompositeEndNode)):
                child.collapse_all()
        if self.is_expanded():
            self.toggle_expanded()

    @overrides
    def has_children(self):
        return len(self._value) != 0

    @overrides
    def get_first_child(self):
        if not self.has_children():
            return None
        return self._get_child_node(0)

    @overrides
    def get_last_child(self):
        if not self.has_children():
            return None
        return self._get_child_node(len(self._value) - 1)

    @overrides
    def prev_child(self, key):
        index = int(key)
        if index == 0:
            return None
        return self._get_child_node(index - 1)

    @overrides
    def next_child(self, key):
        index = int(key)
        if index == len(self._value) - 1:
            return None
        return self._get_child_node(index + 1)

    def _get_child_node(self, index):
        if not self.has_children():
            return None

        if index < 0 or index >= len(self._value):
            raise TypeError(f"index ${index} is out of bound "
                            f"${len(self._value)} in "
                            f"{type(self)}#get_child_node.")
        elif index not in self._children_nodes:
            self._children_nodes[index] = self._load_child_node(index)

        return self._children_nodes[index]

    def _load_child_node(self, index):
        value = self.get_value()[index]
        return self._node_factory.create_node(str(index), value, parent=self,
                                              display_key=False)

    @overrides
    def load_start_widget(self):
        return ArrayStartWidget(self, self.is_display_key())

    @overrides
    def load_unexpanded_widget(self):
        return ArrayUnexpandedWidget(self, self.is_display_key())

    @overrides
    def load_end_node(self):
        return ArrayEndNode(self)
