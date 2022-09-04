from numbers import Number

from overrides import overrides

from .base import PrimitiveWidget
from ..json_node_creator import JSONNodeCreator
from ..json_simple_node import JSONSimpleNode


class NumericNodeCreator(JSONNodeCreator):
    """
    A factory to create `NumericNode`.
    """
    @overrides
    def create_node(self, key, value, **kwargs):
        if isinstance(value, Number):
            return NumericNode(key, value, **kwargs)
        return None


class NumericNode(JSONSimpleNode):
    """
    Implementation of JSON `numeric` type node
    """

    def load_widget(self):
        return NumericWidget(self, self.is_display_key())


class NumericWidget(PrimitiveWidget):
    """
    A widget to display JSON `numeric` type.
    """

    @overrides
    def load_value_markup(self):
        return [('json.numeric', str(self.get_node().get_value()))]
