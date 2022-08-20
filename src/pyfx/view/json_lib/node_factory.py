from cmath import log
from loguru import logger

from pyfx.view.json_lib.json_composite_node import JSONCompositeNode
from pyfx.view.json_lib.primitive.generic import GenericNode

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

        try:
            if issubclass(node_impl, JSONCompositeNode):
                # a complex object should inherited JSONCompositeNode
                    return node_impl(key, value, self, **kwargs)
            return node_impl(key, value, **kwargs)
        except Exception as error:
            # Some non-json datatypes can throw errors in specific situations,
            # and when this happens we should fall back to GenericNode instead of crashing.
            # One example of this being useful is when displaying torch.Tensor objects:
            # torch.Tensors have a __len__, because they can contain many numbers.
            # However, the individual numbers in these tensors are also of type torch.Tensor,
            # and torch throws an error when you try to get len(x) where x is a single number of type torch.Tensor.
            # TLDR: This fallback lets us display torch.Tensor

            #During development of pyfx, it might help to uncomment the following warning.
            #During deployment, however, it's quite annoying and best left silent.
            # logger.warning(
            #     f"Encountered an error using {node_impl},"
            #     f"falling back to GenericNode. The value is of type {type(value)}, "
            #     f"and the error was: {error}"
            # )

            return GenericNode(key, value, **kwargs)
