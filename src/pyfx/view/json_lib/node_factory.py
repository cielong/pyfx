from .array import array_node
from .object import object_node
from .primitive import StringNode, IntegerNode, BooleanNode, NullNode, NumericNode
from .row_index_assigner import RowIndexAssigner


class NodeFactory:
    """
    Factory to create :py:class:`pyfx.view.json_lib.json_simple_node.JSONSimpleNode`.
    """

    node_map = {
        list: array_node.ArrayNode,
        dict: object_node.ObjectNode,
        str: StringNode,
        int: IntegerNode,
        bool: BooleanNode,
        float: NumericNode,
        type(None): NullNode
    }

    @staticmethod
    def create_root_node(value, assign_row_index=False):
        root = NodeFactory.node_map[type(value)]("", value, display_key=False)

        if assign_row_index:
            root.assign_index(RowIndexAssigner())

        return root

    @staticmethod
    def create_node(key, value, **kwargs):
        return NodeFactory.node_map[type(value)](key, value, **kwargs)
