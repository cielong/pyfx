from overrides import overrides

from .base import PrimitiveWidget
from ..json_simple_node import JSONSimpleNode


class IntegerNode(JSONSimpleNode):
    """
    implementation of JSON `string` type node
    """

    def load_widget(self):
        return IntegerWidget(self, self.is_display_key())


class IntegerWidget(PrimitiveWidget):
    """
    a widget to display JSON `string` type
    """

    @overrides
    def load_value_markup(self):
        return [('json.integer', str(self.get_node().get_value()))]
