import re

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from overrides import overrides

from ..common.jsonpath.JSONPathLexer import JSONPathLexer
from ..common.jsonpath.JSONPathListener import JSONPathListener
from ..common.jsonpath.JSONPathParser import JSONPathParser


def autocomplete(current_input, query):
    input_stream = InputStream(current_input)
    lexer = JSONPathLexer(input_stream)
    lexer.removeErrorListeners()

    stream = CommonTokenStream(lexer)
    parser = JSONPathParser(stream)
    parser.removeErrorListeners()

    listener = JSONPathAutoCompleteListener(query)
    parser.addErrorListener(listener)  # listen syntax error
    parser.addParseListener(listener)  # listen incomplete field name

    # start parse
    parser.jsonpath()

    return listener.options


class JSONPathAutoCompleteListener(JSONPathListener, ErrorListener):

    def __init__(self, query):
        super().__init__()
        self._query = query
        self._options = list()

    @property
    def options(self):
        return frozenset(self._options)

    @overrides
    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        tokens = recognizer.getTokenStream().tokens
        if len(tokens) <= 1:
            # last token is always a EOF token
            self._options.append('$')
            return
        elif offending_symbol != tokens[-1]:
            # invalid query if offending symbol is not the last token
            self._options.clear()
            return

        last_token = tokens[-2]
        last_token_type = recognizer.symbolicNames[last_token.type]

        if last_token.text == '.':
            # single dot
            last_valid_query = ''.join([t.text for t in tokens[:-2]])
            current_parent = self._query(last_valid_query)
            self._options = self.find_options(current_parent)
        elif last_token.text == '[':
            # bracket field or array index
            if tokens[-3].text == '.':
                last_valid_query = ''.join([t.text for t in tokens[:-3]])
            else:
                last_valid_query = ''.join([t.text for t in tokens[:-2]])
            current_parent = self._query(last_valid_query)
            self._options = self.find_options(current_parent, '[')
        elif last_token.text == '[?(':
            # filters
            if tokens[-3].text == '.':
                last_valid_query = ''.join([t.text for t in tokens[:-3]])
            else:
                last_valid_query = ''.join([t.text for t in tokens[:-2]])
            current_parent = self._query(last_valid_query)
            self._options = [f"@.{o}" for o in self.find_options(current_parent, include_wildcard=False)]
        elif last_token.text == '[(':
            # only if last query return list and length
            if tokens[-3].text == '.':
                last_valid_query = ''.join([t.text for t in tokens[:-3]])
            else:
                last_valid_query = ''.join([t.text for t in tokens[:-2]])
            current_parent = self._query(last_valid_query)
            if isinstance(current_parent, list):
                self._options = [f"@.length - {i}" for i in range(1, len(current_parent) + 1)]

    def enterDoubleDotExpression(self, ctx: JSONPathParser.DoubleDotExpressionContext):
        print("enter recursive child")

    def enterFieldAccessor(self, ctx: JSONPathParser.FieldAccessorContext):
        print("enter field accessor")

    def exitFieldAccessor(self, ctx: JSONPathParser.FieldAccessorContext):
        tokens = ctx.parser.getTokenStream().tokens
        if tokens[-3].text == '.':
            last_valid_query = ''.join([t.text for t in tokens[:-3]])
        else:
            last_valid_query = ''.join([t.text for t in tokens[:-2]])
        current_parent = self._query(last_valid_query)
        options = self.find_options(current_parent, prefix=tokens[-2].text)

        if len(options) > 1 or (len(options) == 1 and options[0] != tokens[-2].text):
            self._options = options
        else:
            self._options = [".", "["]

    @staticmethod
    def find_options(parent, prefix="", include_wildcard=True):
        options = []
        if isinstance(parent, list):
            # current parent is a list
            if include_wildcard:
                options.append('[*]')
            options.append(JSONPathAutoCompleteListener._generate_list_completes(len(parent), prefix))
        elif isinstance(parent, dict):
            if include_wildcard:
                if prefix.startswith('['):
                    options.append('[*]')
                else:
                    options.append('*')
            for key in parent.keys():
                if (not re.match(r'\w+', key)) or prefix.startswith('['):
                    options.append("['" + key + "']")
                else:
                    options.append(key)
            options = list(filter(lambda k: k.startswith(prefix), options))
        return options

    @staticmethod
    def _generate_list_completes(length, prefix=""):
        """
        Generates completes for an array, use its length also add `*` to represent
        everything.

        :param length: the list length
        :type length: int
        :return: completes for current length.
        """
        options = ['[' + str(index) + ']' for index in range(length)]
        return list(filter(lambda k: k.startswith(prefix), options))
