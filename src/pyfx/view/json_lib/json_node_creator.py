"""A public interface used to create a subclass of `JSONSimpleNode`.
E.g., see :class:`.primitive.string.StringNodeCreator`.

This class is created to hide the implementation of creating a single node and
ease the way for :class:`.JSONNodeFactory` to do type deduction.
"""
from abc import ABC
from abc import abstractmethod


class JSONNodeCreator(ABC):
    """
    An interface to create a specific :class:`.JSONSimpleNode` instance.
    """
    @abstractmethod
    def create_node(self, key, value, **kwargs):
        """Creates a node based on the type of the value.

        Subclass must override this method to provide a valid `JSONSimpleNode`
        implementation.

        Args:
            key(Any): the key which its parent node use to retrieve this node.
            value(Any): the actual value that will be represented by the node.
            **kwargs: all the extra arguments passed into JSONSimpleNode
                      implementation.

        Returns:
            When the type of the value matches the expected value,
            it returns the actual implementation instance.
            Otherwise, it returns ``None``.
        """
        raise NotImplementedError("#creat_node is not implemented.")
