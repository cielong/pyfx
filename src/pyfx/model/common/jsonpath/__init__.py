"""
A homemade JSONPath grammar using ANTLR4.

The reason to build a separate grammar is to build auto-completion for JSONPath
and finding resources on building autocompletion on ANTLR4 is much easier :)
"""
from .JSONPathParser import JSONPathParser
from .JSONPathLexer import JSONPathLexer
from .JSONPathListener import JSONPathListener
