from overrides import overrides

from .base import PrimitiveWidget
from ..json_node_creator import JSONNodeCreator
from ..json_simple_node import JSONSimpleNode


class IntegerNodeCreator(JSONNodeCreator):
    """
    A factory to create `IntegerNode`.
    """
    @overrides
    def create_node(self, key, value, **kwargs):
        if isinstance(value, int):
            return IntegerNode(key, value, **kwargs)
        return None


class IntegerNode(JSONSimpleNode):
    """
    Implementation of JSON `integer` type node.
    """

    def load_widget(self):
        return IntegerWidget(self, self.is_display_key())


class IntegerWidget(PrimitiveWidget):
    """
    A widget to display JSON `integer` type.
    """

    @overrides
    def load_value_markup(self):
        return [('json.integer', str(self.get_node().get_value()))]
