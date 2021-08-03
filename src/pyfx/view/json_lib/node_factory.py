from loguru import logger

from pyfx.view.json_lib.json_composite_node import JSONCompositeNode


class NodeFactory:
    """
    Factory to create :py:class:`pyfx.view.json_lib.json_simple_node.JSONSimpleNode`.
    """

    def __init__(self, impls):
        self._node_map = impls

    def register(self, impls):
        for k, v in impls.items():
            if k in self._node_map:
                logger.warning(
                    f"Overriding type {k} implementation in node factory, the"
                    f"existed one is {self._node_map[v]}"
                )
            self._node_map[k] = v

    def create_root_node(self, value):
        """
        Create root node
        """
        return self.create_node("", value, display_key=False)

    def create_node(self, key, value, **kwargs):
        """
        Create JSON node based on the type of the value.
        """
        node_impl = self._node_map[type(value)]

        if issubclass(node_impl, JSONCompositeNode):
            # a complex object should inherited JSONCompositeNode
            return node_impl(key, value, self, **kwargs)
        return node_impl(key, value, **kwargs)
