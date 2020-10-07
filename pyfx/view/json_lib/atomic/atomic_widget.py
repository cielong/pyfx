#! /usr/bin/env python3

from overrides import overrides

from pyfx.view.json_lib.json_widget import JSONWidget


class AtomicWidget(JSONWidget):
    """ display widget for JSON `string`, `integer`, `number`, `boolean`, `null` type """

    def __init__(self,
                 node: "AtomicNode",
                 display_key: bool
                 ):
        super().__init__(node, False, display_key)

    @overrides
    def get_display_text(self):
        key = self.get_node().get_key()
        value = self.get_node().get_value()
        if not self.is_display_key():
            return f"{'null' if value is None else value}"
        return f"{key}: {'null' if value is None else value}"
