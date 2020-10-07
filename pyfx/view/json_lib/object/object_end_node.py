from overrides import overrides

from pyfx.view.json_lib.object.object_end_widget import ObjectEndWidget
from pyfx.view.json_lib.json_composite_end_node import JSONCompositeEndNode


class ObjectEndNode(JSONCompositeEndNode):
    """ display widget for JSON `array` type node """

    def __init__(self,
                 start_node: "ArrayNode"
                 ):
        super().__init__(start_node)

    @overrides
    def load_widget(self):
        return ObjectEndWidget(self)