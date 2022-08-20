from overrides import overrides

from .base import PrimitiveWidget
from ..json_simple_node import JSONSimpleNode


class GenericNode(JSONSimpleNode):
    """
    implementation of non-JSON `generic` type node
    """

    def load_widget(self):
        return GenericWidget(self, self.is_display_key())


class GenericWidget(PrimitiveWidget):
    """
    a widget to display generic Python objects
    """

    @overrides
    def load_value_markup(self):
        return [('json.string', str(self.get_node().get_value()))]
