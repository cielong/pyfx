from pyfx.view.json_lib.json_widget import JSONWidget


class ObjectEndWidget(JSONWidget):
    """ display widget for JSON `object` type nodes """

    def __init__(self,
                 node: "ObjectEndNode"
                 ):
        super().__init__(node, True, False)

    def get_display_text(self):
        return "}"
