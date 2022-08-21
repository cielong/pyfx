from numbers import Number

from ..object import ObjectNode
from ..array import ArrayNode
from ..primitive import StringNode, IntegerNode, NumericNode, BooleanNode, NullNode, GenericNode

def hasattrs(x,*attrs):
    return all(hasattr(x,attr) for attr in attrs)

def is_numeric(x):
    return isinstance(x,Number) or isinstance(x,type) and issubclass(x,Number)

def is_dictlike(x):
    return hasattrs(x,'__getitem__','__iter__','__len__','keys')

def is_arraylike(x):
    return hasattrs(x,'__getitem__','__iter__','__len__')


class DefaultImplementationSelector:
    def __getitem__(self,key):
        if key in DEFAULT_JSON_NODE_IMPLS:
            return DEFAULT_JSON_NODE_IMPLS[key]
        if is_numeric(key):
            return NumericNode
        if is_dictlike(key):
            return ObjectNode
        if is_arraylike(key):
            return ArrayNode
        return GenericNode


DEFAULT_JSON_NODE_IMPLS = {
    list: ArrayNode,
    dict: ObjectNode,
    str: StringNode,
    int: IntegerNode,
    bool: BooleanNode,
    float: NumericNode,
    type(None): NullNode
}
