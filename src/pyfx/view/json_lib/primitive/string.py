from overrides import overrides

from .base import PrimitiveWidget
from ..json_node_creator import JSONNodeCreator
from ..json_simple_node import JSONSimpleNode


class StringNodeCreator(JSONNodeCreator):
    """
    A factory to create `StringNode`.
    """
    @overrides
    def create_node(self, key, value, **kwargs):
        if isinstance(value, str):
            return StringNode(key, value, **kwargs)
        return None


class StringNode(JSONSimpleNode):
    """
    implementation of JSON `string` type node
    """

    def load_widget(self):
        return StringWidget(self, self.is_display_key())


class StringWidget(PrimitiveWidget):
    """
    a widget to display JSON `string` type
    """

    @overrides
    def load_value_markup(self):
        return [('json.string', '"' + str(self.get_node().get_value()) + '"')]
