"""
ANTLR4 based JSONPath Auto-Completion Module.

The auto-completion is achieved by implementing an AutoCompleteListener which extends ErrorListener
and ParseListener based on syntax defined in JSONPath.g4_ which is based on JSONPath_ and jsonpath_ng_.

.. _JSONPath.g4: https://github.com/cielong/pyfx/blob/doc/src/pyfx/model/common/jsonpath/JSONPath.g4
.. _JSONPath: https://goessner.net/articles/JsonPath/
.. _jsonpath_ng: https://github.com/h2non/jsonpath-ng
"""
from .autocomplete_listener import autocomplete
