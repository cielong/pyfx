from overrides import overrides

from pyfx.view.json_lib.json_widget import JSONWidget


class ArrayEndWidget(JSONWidget):
    """ display widget for JSON `array` type node """

    def __init__(self,
                 node: "ArrayEndNode"
                 ):
        # display_key is not important for end widget
        super().__init__(node, True, False)

    @overrides
    def get_display_text(self):
        return "]"
