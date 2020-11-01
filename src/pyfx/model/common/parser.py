import re

from jsonpath_ng import parse
from loguru import logger


class Parser:
    """
    A separated parser used to parse an incomplete query with the help of given
    tokens.
    """
    @staticmethod
    def parse(query):
        """
        Based on :func:`jsonpath_ng.parse` to parse and return the last valid
        query parse result if query is incomplete or second-last valid query parse
        result if query is complete.

        :param query: the query
        :type query: str
        """
        tokens = Parser._tokenize(query)
        if len(tokens) == 1 or re.match(r'^\.{1,2}$', tokens[-1]):
            # though we tokenize series dot as a group, but we only allow one/two dots
            prefix = ""
        else:
            prefix = tokens[-1]
        return prefix, Parser._parse(query, tokens)

    # noinspection PyBroadException
    @staticmethod
    def _parse(query, tokens):
        """
        Parse the query with the help of parsed tokens (see :med:`._tokenize`).

        :param query: the original query
        :type query: str
        :param tokens: the parsed tokens
        :type tokens: list
        :return: a parser, or None if the query is invalid
        """
        jsonpath_exp = None
        try:
            if len(tokens) <= 2:
                last_complete_query = tokens[0]
            elif re.match(r'\.+', tokens[-2]):
                # the last segment is separated with dot
                last_complete_query = ''.join(tokens[:-2])
            else:
                last_complete_query = ''.join(tokens[:-1])
            jsonpath_exp = parse(last_complete_query)
        except Exception as e:
            # swallow this error but this should be something to fix
            logger.opt(exception=True) \
                .warning("Invalid query {} with parsed tokens {}", query, tokens)
        return jsonpath_exp

    @staticmethod
    def _tokenize(query):
        """
        Parse the query into list of valid tokens.

        Each token is a valid segment in the JSONPath, with the last one possibly be
        empty or potentially incomplete segments.

        A valid segment is defined us either splitter (:code:`r'\.+'`) or brackets
        (:code:`r'\[.*\]'`) or fields (:code:`r'[$\w]'`).

        :param query: the current query
        :type query: str
        :return: JSONPath tokens
        """
        tokens = []
        pre, cur = -1, 0
        open_brace = 0  # counters to detect whether brackets is matches
        while cur < len(query):
            ch = query[cur]
            if open_brace == 0:
                if ch == '.':
                    if pre + 1 != cur:
                        # last index is the end of a token
                        tokens.append(query[pre + 1: cur])
                    pre = cur
                    while cur < len(query) and query[cur] == '.':
                        # bypass any potential continuous dot
                        cur += 1
                    if cur < len(query):
                        # cur is currently at a non-dot character
                        tokens.append(query[pre: cur])
                        pre = cur - 1
                    else:
                        # cur is currently the end of query
                        tokens.append(query[pre:])
                        pre = cur
                elif ch == '[':
                    if cur > 0:
                        tokens.append(query[pre + 1: cur])
                    open_brace += 1
                    pre = cur - 1
            else:
                if ch == ']':
                    open_brace -= 1
                elif ch == '[':
                    open_brace += 1

                if open_brace == 0:
                    tokens.append(query[pre + 1: cur + 1])
                    pre = cur
            cur += 1
        if pre + 1 != cur:
            # add the last token if non-empty
            tokens.append(query[pre + 1: cur])
        return tokens
