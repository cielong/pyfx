from .array import array_node
from .primitive import primitive_node
from .object import object_node


class NodeFactory:
    """
    factory of creating nodes
    """

    @staticmethod
    def create_node(key, value, parent=None, display_key=False):
        if isinstance(value, list):
            return array_node.ArrayNode(key, value, parent=parent, display_key=display_key)
        elif isinstance(value, dict):
            return object_node.ObjectNode(key, value, parent=parent, display_key=display_key)
        else:
            return primitive_node.PrimitiveNode(key, value, parent=parent, display_key=display_key)
