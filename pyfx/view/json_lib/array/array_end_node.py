from overrides import overrides

from pyfx.view.json_lib.array.array_end_widget import ArrayEndWidget
from pyfx.view.json_lib.json_composite_end_node import JSONCompositeEndNode


class ArrayEndNode(JSONCompositeEndNode):
    """ display widget for JSON `array` type node """

    def __init__(self,
                 start_node: "ArrayNode"
                 ):
        super().__init__(start_node)

    @overrides
    def load_widget(self):
        return ArrayEndWidget(self)
