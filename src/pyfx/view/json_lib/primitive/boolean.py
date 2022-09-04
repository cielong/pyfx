from overrides import overrides

from .base import PrimitiveWidget
from ..json_simple_node import JSONSimpleNode
from ..json_node_creator import JSONNodeCreator


class BooleanNodeCreator(JSONNodeCreator):
    """
    A factory to create `BooleanNode`.
    """
    @overrides
    def create_node(self, key, value, **kwargs):
        if isinstance(value, bool):
            return BooleanNode(key, value, **kwargs)
        return None


class BooleanNode(JSONSimpleNode):
    """
    Implementation of JSON `bool` type node.
    """

    def load_widget(self):
        return BooleanWidget(self, self.is_display_key())


class BooleanWidget(PrimitiveWidget):
    """
    A widget to display JSON `bool` type.
    """

    @overrides
    def load_value_markup(self):
        return [('json.bool', str(self.get_node().get_value()).lower())]
