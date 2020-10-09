from ..json_widget import JSONWidget


class ObjectEndWidget(JSONWidget):
    """
    a widget to display the end symbol for JSON `object` type nodes
    """

    def __init__(self,
                 node: "ObjectEndNode"
                 ):
        super().__init__(node, True, False)

    def get_display_text(self):
        return "}"
