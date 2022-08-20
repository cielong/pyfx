"""
Node implementation of primitive JSON type which represents `string`,
`integer`, `numeric`, `boolean` and `null`
"""
from .boolean import BooleanNode
from .integer import IntegerNode
from .null import NullNode
from .numeric import NumericNode
from .string import StringNode
from .generic import GenericNode
