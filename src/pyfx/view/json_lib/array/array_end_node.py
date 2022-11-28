from overrides import overrides

from .array_end_widget import ArrayEndWidget
from ..json_composite_end_node import JSONCompositeEndNode


class ArrayEndNode(JSONCompositeEndNode):
    """Represents the ending edge of an `array` node in the JSON tree.

    For data modeling details, see :class:`..JSONCompositeNode`.
    """

    def __init__(self, start_node):
        super().__init__(start_node)

    @overrides
    def load_widget(self):
        return ArrayEndWidget(self)
