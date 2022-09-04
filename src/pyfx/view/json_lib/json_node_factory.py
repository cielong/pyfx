from numbers import Number

from loguru import logger

from pyfx.view.json_lib.array import ArrayNode
from pyfx.view.json_lib.json_composite_node import JSONCompositeNode
from pyfx.view.json_lib.object import ObjectNode
from pyfx.view.json_lib.primitive import BooleanNode
from pyfx.view.json_lib.primitive import IntegerNode
from pyfx.view.json_lib.primitive import NullNode
from pyfx.view.json_lib.primitive import NumericNode
from pyfx.view.json_lib.primitive import StringNode


class JSONNodeFactory:
    """
    Factory to create
    :py:class:`pyfx.view.json_lib.json_simple_node.JSONSimpleNode`.
    """

    def __init__(self):
        self._object_hook = None

    def register(self, object_hook):
        """
        Register a callable to override a `JSONSimpleNode` implementation for
        a type.

        `object_hook`: a callable from a value to `JSONSimpleNode`
        implementation.
        """
        logger.info(f"Register {object_hook} in JSON node factory")
        self._object_hook = object_hook

    def create_root_node(self, value):
        """
        Create root node.
        """
        return self.create_node("", value, display_key=False)

    def create_node(self, key, value, **kwargs):
        """
        Create JSON node based on the type of the value.
        """
        node_impl = self.__find_impl(value)

        if issubclass(node_impl, JSONCompositeNode):
            # a complex object should inherited JSONCompositeNode
            return node_impl(key, value, self, **kwargs)
        return node_impl(key, value, **kwargs)

    def __find_impl(self, value):
        """
        Find the real `JSONSimpleNode` implementation based on the value.
        """
        if value is None:
            return NullNode

        impl = None if self._object_hook is None else self._object_hook(value)
        if impl is not None:
            # If the rendering widget is provided/override.
            return impl

        # noinspection PyBroadException
        try:
            if isinstance(value, bool):
                return BooleanNode
            elif isinstance(value, int):
                return IntegerNode
            elif isinstance(value, Number):
                return NumericNode
            elif isinstance(value, str):
                return StringNode
            elif isinstance(value, dict):
                return ObjectNode
            elif isinstance(value, list):
                return ArrayNode
            else:
                raise ValueError(f"Unrecognized type for {value}.")
        except Exception as e:
            logger.opt(exception=e)\
                .warning("Failed to find JSON node implementation for "
                         f"{value}. Use StringNode by default.")
            return StringNode
