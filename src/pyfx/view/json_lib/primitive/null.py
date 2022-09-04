from overrides import overrides

from .base import PrimitiveWidget
from ..json_simple_node import JSONSimpleNode


class NullNode(JSONSimpleNode):
    """
    implementation of JSON `null` type node
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
