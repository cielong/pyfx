from overrides import overrides

from .array_end_widget import ArrayEndWidget
from ..json_composite_end_node import JSONCompositeEndNode


class ArrayEndNode(JSONCompositeEndNode):
    """
    a widget to display JSON `array` type node
    """

    def __init__(self,
                 start_node: "ArrayNode"
                 ):
        super().__init__(start_node)

    @overrides
    def load_widget(self):
        return ArrayEndWidget(self)
