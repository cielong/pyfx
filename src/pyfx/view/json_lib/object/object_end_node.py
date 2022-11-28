from overrides import overrides

from .object_end_widget import ObjectEndWidget
from ..json_composite_end_node import JSONCompositeEndNode


class ObjectEndNode(JSONCompositeEndNode):
    """Represents the ending edge of an `object` node in the JSON tree.

    For data modeling details, see :class:`..JSONCompositeNode`.
    """

    def __init__(self, start_node):
        super().__init__(start_node)

    @overrides
    def load_widget(self):
        return ObjectEndWidget(self)
