"""
A public interface used to create a subclass of `JSONSimpleNode`.
"""
from abc import ABC
from abc import abstractmethod


class JSONNodeCreator(ABC):
    """
    An interface to create a specific `JSONSimpleNode` implementation.
    """
    @abstractmethod
    def create_node(self, key, value, **kwargs):
        """Creates a node based on the type of the value.

        Subclass must override this method to provide a valid `JSONSimpleNode`
        implementation.

        Arguments:
            key: the key which its parent node use to retrieve this node.
            value: the actual value that will be represented by the node.
            **kwargs: all the extra arguments passed into JSONSimpleNode
                      implementation.

        Returns:
            When the type of the value matches the expected value,
            it returns the actual implementation instance.
            Otherwise, it returns None.
        """
        raise NotImplementedError("#creat_node is not implemented.")
