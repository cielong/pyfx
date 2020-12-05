from overrides import overrides

from .base import PrimitiveWidget
from ..json_simple_node import JSONSimpleNode


class NullNode(JSONSimpleNode):
    """
    implementation of JSON `string` type node
    """

    def load_widget(self):
        return NullWidget(self, self.is_display_key())


class NullWidget(PrimitiveWidget):
    """
    a widget to display JSON `string` type
    """

    @overrides
    def load_value_markup(self):
        return [('json.null', "null")]
