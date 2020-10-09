from ..json_widget import JSONWidget


class ObjectUnexpandedWidget(JSONWidget):
    """
    a widget to display unexpanded text for JSON `object` type nodes
    """

    def __init__(self,
                 node,
                 display_key,
                 ):
        super().__init__(node, True, display_key)

    def get_display_text(self):
        if self.get_node().get_depth() == 0 or (not self.is_display_key()):
            return "{\u2026}"
        else:
            return self.get_node().get_key() + ": {\u2026}"
