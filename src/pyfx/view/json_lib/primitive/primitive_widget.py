#! /usr/bin/env python3

from overrides import overrides

from ..json_widget import JSONWidget


class PrimitiveWidget(JSONWidget):
    """
    a widget to display JSON `string`, `integer`, `number`, `boolean`, `null` type
    """

    def __init__(self,
                 node,
                 display_key
                 ):
        super().__init__(node, False, display_key)

    @overrides
    def get_display_text(self):
        key = self.get_node().get_key()
        value = self.get_node().get_value()
        if not self.is_display_key():
            return f"{'null' if value is None else value}"
        return f"{key}: {'null' if value is None else value}"
