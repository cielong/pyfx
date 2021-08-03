import re

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from loguru import logger
from overrides import overrides

from ..common.jsonpath import JSONPathLexer, JSONPathParser, JSONPathListener


def autocomplete(current_input, query):
    """
    Use :class:`.JSONPathAutoCompleteListener`
    to parse the query and give auto-completion suggestions.

    :param current_input: the current query input
    :type current_input: str
    :param query: the query callback which can be used to get data.
    :type query: callback
    """
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

    return listener.is_partial_complete, listener.prefix, listener.options


class JSONPathAutoCompleteListener(JSONPathListener, ErrorListener):
    """
    Both an ErrorListener and JSONPathListener.

    Based on the syntax error ANTLR4 returned to find the possible completions.
    """

    IDENTIFIED_TOKENS = frozenset(['.', '[', '?', '..'])

    def __init__(self, query):
        super().__init__()
        self._query = query
        self._options = list()
        self._prefix = ""
        # flag indicate whether autocomplete only partially complete the query
        self._partial_complete = False
        self._recover_methods = {
            (JSONPathParser.DoubleDotExpressionContext, '..'):
                self.complete_double_dot_field_access,
            (JSONPathParser.SingleDotExpressionContext, '.'):
                self.complete_single_dot_field_access,
            (JSONPathParser.SingleDotExpressionContext, '['):
                self.complete_bracket_field_access,
            (JSONPathParser.FiltersContext, '?'): self.complete_filters,
            (JSONPathParser.UnionContext, '['): self.complete_union
        }

    def reset(self):
        """ reset the current result, #exitFieldAccessor or else may lead to in
        correct conclusion
        """
        self._options = []
        self._prefix = ""
        self._partial_complete = False

    @property
    def options(self):
        return self._options.copy()

    @property
    def prefix(self):
        return self._prefix

    @property
    def is_partial_complete(self):
        return self._partial_complete

    @overrides(check_signature=False)
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

        self.reset()
        last_token_index = len(tokens) - 2
        identified_token = tokens[last_token_index].text
        while last_token_index >= 0 and \
                identified_token not in self.IDENTIFIED_TOKENS:
            last_token_index -= 1
            identified_token = tokens[last_token_index].text

        key = (type(recognizer._ctx), identified_token)
        try:
            # noinspection PyArgumentList
            self._recover_methods[key](tokens)
        except KeyError:
            logger.opt(exception=True).warning(
                f"{key} not defined in JSONPathAutoCompleteListener.recover_"
                f"methods"
            )
            self._options.clear()

    @overrides
    def exitFieldAccessor(self, ctx: JSONPathParser.FieldAccessorContext):
        self.reset()

        params = dict()
        tokens = ctx.parser.getTokenStream().tokens
        if tokens[-2].text == ']':
            # bypass bracket field, since it's always complete
            self._options = [".", "["]
            self._prefix = ""
            self._partial_complete = True
            return

        last_valid_query = self.find_last_valid_query(tokens)
        current_parent = self._query(last_valid_query)

        if tokens[-4].text == '[*]':
            # this only happens when current parent is list
            current_parent = current_parent[0]
            params["include_wildcard"] = False
        params["parent"] = current_parent
        params["prefix"] = tokens[-2].text

        options = self.find_options(**params)

        if len(options) == 1 and options[0] == tokens[-2].text:
            # the only current options is complete, suggest the next token
            self._options = [".", "["]
            self._prefix = ""
            self._partial_complete = True
            return

        self._options = options
        self._prefix = tokens[-2].text

    def complete_double_dot_field_access(self, tokens):
        pass

    def complete_single_dot_field_access(self, tokens):
        params = dict()

        last_valid_query = self.find_last_valid_query(
            tokens, optional_single_dot=False
        )
        current_parent = self._query(last_valid_query)

        if tokens[-3].text == '[*]':
            # this only happens when current parent is list
            current_parent = current_parent[0]
            params["include_wildcard"] = False

        params["parent"] = current_parent
        self._options = self.find_options(**params)
        self._prefix = ""

    def complete_bracket_field_access(self, tokens):
        params = dict()
        # bracket field or array index
        if tokens[-2].text != '[':
            last_valid_query_end = -3
        else:
            last_valid_query_end = -2
        last_valid_query = self.find_last_valid_query(
            tokens, last_valid_query_end=last_valid_query_end
        )
        current_parent = self._query(last_valid_query)

        if tokens[last_valid_query_end - 1].text == '[*]' or \
                (tokens[last_valid_query_end - 1].text == '.' and
                 tokens[last_valid_query_end - 2].text == '[*]'):
            # this only happens when current parent is list
            current_parent = current_parent[0]
            params["include_wildcard"] = False

        params["parent"] = current_parent
        params["prefix"] = ''.join(
            [t.text for t in tokens[last_valid_query_end:-1]]
        )
        self._options = self.find_options(**params)
        self._prefix = params["prefix"]

    def complete_filters(self, tokens):
        params = {
            "include_wildcard": False
        }
        contains_braces = False
        question_mark_index = len(tokens) - 2
        while question_mark_index >= 0 and \
                tokens[question_mark_index].text != '?':
            contains_braces = tokens[question_mark_index].text == '('
            question_mark_index -= 1

        if not contains_braces:
            self._options = ['(']
            self._prefix = ""
            self._partial_complete = True
            return

        last_valid_query = self.find_last_valid_query(
            tokens, last_valid_query_end=question_mark_index - 1
        )
        current_parent = self._query(last_valid_query)

        if tokens[question_mark_index - 2].text == '[*]' or \
                (tokens[question_mark_index - 2].text == '.' and
                 tokens[question_mark_index - 3].text == '[*]'):
            # this only happens when current parent is list
            current_parent = current_parent[0]
            params["include_wildcard"] = False

        params["parent"] = current_parent
        self._options = [f"@.{o}" for o in self.find_options(**params)]
        self._prefix = ""
        self._partial_complete = True

    def complete_union(self, tokens):
        params = {
            "include_wildcard": False,
            "is_union": True
        }
        existed_keys = set()
        last_valid_query_end = len(tokens) - 2
        while last_valid_query_end >= 0 and \
                tokens[last_valid_query_end].text != '[':
            last_valid_query_end -= 1
            if re.match(r"^'.*'$", tokens[last_valid_query_end].text):
                existed_keys.add(tokens[last_valid_query_end].text)
        last_valid_query = self.find_last_valid_query(
            tokens, last_valid_query_end=last_valid_query_end
        )
        current_parent = self._query(last_valid_query)

        if tokens[last_valid_query_end -
                  1].text == '[*]' or (tokens[last_valid_query_end -
                                              1].text == '.' and tokens[
                      last_valid_query_end -
                      2].text == '[*]'):
            # this only happens when current parent is list
            current_parent = current_parent[0]
            params["include_wildcard"] = False

        params["parent"] = current_parent
        params["prefix"] = tokens[-2].text if tokens[-2].text != ',' else ""
        options = self.find_options(**params)
        self._options = list(filter(lambda o: o not in existed_keys, options))
        self._prefix = params["prefix"]
        self._partial_complete = True

    @staticmethod
    def find_last_valid_query(
            tokens, last_valid_query_end=-2, optional_single_dot=True):
        # last token will always be EOF
        if optional_single_dot and tokens[last_valid_query_end - 1].text == '.':
            return ''.join([t.text for t in tokens[:last_valid_query_end - 1]])
        return ''.join([t.text for t in tokens[:last_valid_query_end]])

    @staticmethod
    def find_options(parent, prefix="", include_wildcard=True, is_union=False):
        options = []
        if isinstance(parent, list):
            # current parent is a list
            if include_wildcard and not is_union:
                options.append('[*]')
            options.extend(
                JSONPathAutoCompleteListener._generate_list_completes(
                    len(parent), prefix, is_union
                )
            )
        elif isinstance(parent, dict):
            if include_wildcard and not is_union:
                if prefix.startswith('['):
                    options.append('[*]')
                else:
                    options.append('*')
            for key in parent.keys():
                if is_union:
                    options.append(f"'{key}'")
                elif (not re.match(r'\w+', key)) or prefix.startswith('['):
                    options.append("['" + key + "']")
                else:
                    options.append(key)
            options = list(filter(lambda k: k.startswith(prefix), options))
        return options

    @staticmethod
    def _generate_list_completes(length, prefix="", is_union=False):
        """
        Generates completes for an array, use its length also add `*` to represent
        everything.

        :param length: the list length
        :type length: int
        :param prefix: the current prefix
        :type prefix: str
        :param is_union: whether the complete method is a union method
        :type is_union: bool
        :return: completes for current length.
        """
        if is_union:
            options = [str(index) for index in range(length)]
        else:
            options = ['[' + str(index) + ']' for index in range(length)]
        return list(filter(lambda k: k.startswith(prefix), options))
