"""
A homemade JSONPath grammar using ANTLR4.

The reason to build a separate grammar is to build auto-completion for JSONPath,
and the internal lexer for :mod:`jsonpath-ng` seems not able to extend it to
add error recovery methods.
"""
from .JSONPathParser import JSONPathParser
from .JSONPathLexer import JSONPathLexer
from .JSONPathListener import JSONPathListener
