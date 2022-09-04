from overrides import overrides

from .base import PrimitiveWidget
from ..json_node_creator import JSONNodeCreator
from ..json_simple_node import JSONSimpleNode


class NullNodeCreator(JSONNodeCreator):
    """
    A factory to create `NullNode`.
    """
    @overrides
    def create_node(self, key, value, **kwargs):
        if value is None:
            return NullNode(key, value, **kwargs)
        return None


class NullNode(JSONSimpleNode):
    """
    Implementation of JSON `null` type node.
    """

    def load_widget(self):
        return NullWidget(self, self.is_display_key())


class NullWidget(PrimitiveWidget):
    """
    a widget to display JSON `null` type
    """

    @overrides
    def load_value_markup(self):
        return [('json.null', "null")]
