import re

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from loguru import logger
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
        self.recover_methods = {
            (JSONPathParser.SingleDotExpressionContext, '.'): self.complete_single_dot_field_access,
            (JSONPathParser.SingleDotExpressionContext, '['): self.complete_bracket_field_access,
            (JSONPathParser.SingleDotExpressionContext, '[?('): self.complete_filter,
            (JSONPathParser.SingleDotExpressionContext, '[('): self.complete_length
        }

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
        key = (type(recognizer._ctx), tokens[-2].text)
        try:
            # noinspection PyArgumentList
            self.recover_methods[key](tokens)
        except KeyError as e:
            logger.opt(exception=True) \
                  .warning(f"{key} not defined in JSONPathAutoCompleteListener.recover_methods")
            self._options.clear()

    def enterDoubleDotExpression(self, ctx: JSONPathParser.DoubleDotExpressionContext):
        print("enter recursive child")

    def enterFieldAccessor(self, ctx: JSONPathParser.FieldAccessorContext):
        print("enter field accessor")

    def exitFieldAccessor(self, ctx: JSONPathParser.FieldAccessorContext):
        tokens = ctx.parser.getTokenStream().tokens
        if tokens[-2].text == ']':
            # bypass bracket field, since it's always complete
            self._options = [".", "["]
            return

        last_valid_query = self.find_last_valid_query(tokens)
        current_parent = self._query(last_valid_query)
        options = self.find_options(current_parent, prefix=tokens[-2].text)

        if len(options) == 1 and options[0] == tokens[-2].text:
            # the only current options is complete, suggest the next token
            self._options = [".", "["]
            return

        self._options = options

    def complete_single_dot_field_access(self, tokens):
        last_valid_query = self.find_last_valid_query(tokens, optional_single_dot=False)
        current_parent = self._query(last_valid_query)
        self._options = self.find_options(current_parent)

    def complete_bracket_field_access(self, tokens):
        # bracket field or array index
        last_valid_query = self.find_last_valid_query(tokens)
        current_parent = self._query(last_valid_query)
        self._options = self.find_options(current_parent, '[')

    def complete_filter(self, tokens):
        last_valid_query = self.find_last_valid_query(tokens)
        current_parent = self._query(last_valid_query)
        self._options = [f"@.{o}" for o in self.find_options(current_parent, include_wildcard=False)]

    def complete_length(self, tokens):
        last_valid_query = self.find_last_valid_query(tokens)
        current_parent = self._query(last_valid_query)
        if isinstance(current_parent, list):
            # only if last query return list and length
            self._options = [f"@.length - {i}" for i in range(1, len(current_parent) + 1)]

    @staticmethod
    def find_last_valid_query(tokens, optional_single_dot=True):
        # last token will always be EOF
        if optional_single_dot and tokens[-3].text == '.':
            return ''.join([t.text for t in tokens[:-3]])
        return ''.join([t.text for t in tokens[:-2]])

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
