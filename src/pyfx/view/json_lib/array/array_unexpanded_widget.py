from overrides import overrides

from ..json_widget import JSONWidget


class ArrayUnexpandedWidget(JSONWidget):
    """
    a widget display JSON `array` type node
    """

    def __init__(self,
                 node,
                 display_key,
                 ):
        super().__init__(node, True, display_key)

    @overrides
    def get_display_text(self):
        if self.get_node().get_depth() == 0 or (not self.is_display_key()):
            return "[\u2026]"
        else:
            return self.get_node().get_key() + ": [\u2026]"
