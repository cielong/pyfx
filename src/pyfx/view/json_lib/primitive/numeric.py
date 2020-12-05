from overrides import overrides

from .base import PrimitiveWidget
from ..json_simple_node import JSONSimpleNode


class NumericNode(JSONSimpleNode):
    """
    implementation of JSON `string` type node
    """

    def load_widget(self):
        return NumericWidget(self, self.is_display_key())


class NumericWidget(PrimitiveWidget):
    """
    a widget to display JSON `string` type
    """

    @overrides
    def load_value_markup(self):
        return [('json.numeric', str(self.get_node().get_value()))]
