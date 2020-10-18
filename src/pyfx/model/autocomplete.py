"""
Auto-completion module for JSONPath query.
"""

from jsonpath_ng import parse
from loguru import logger


class JSONPathAutoComplete:
    """
    Utility library that performs auto-completion on the given potentially incomplete query.

    :py:meth:`complete` is the single entry point of this class which returns Tuple.of(the incomplete
    prefix, potential completes)
    """

    @staticmethod
    def complete(data, query):
        """
        Complete the given query with potential options in the given data.

        :param data: the data
        :type data: dict, list, int, float, str, bool, None
        :param query: the query
        :type query: str
        :return: (option_prefix, options)
        """
        if len(query) == 0:
            # boundary condition
            # return root if empty
            return '', ['$']
        elif query == '$':
            # this query contains valid autocompletes with brackets style
            # but we currently ignore it.
            return '', []

        # 1. tokenize the query to get valid segments of query
        tokens = JSONPathAutoComplete._tokenize(query)

        # 2. execute last valid query
        jsonpath_exp = JSONPathAutoComplete._parse(query, tokens)

        if jsonpath_exp is None:
            # something wrong inside `_parse`
            # return nothing here and the error is logger inside _parse
            return '', []

        current_data = [match.value for match in jsonpath_exp.find(data)]

        # 3. list valid options on the current node
        options = JSONPathAutoComplete._list_options(current_data)

        # 4. filter options based on the current incomplete prefix
        options = JSONPathAutoComplete._filter_options(options, tokens[-1])

        return tokens[-1], options

    @staticmethod
    def _tokenize(query):
        """
        Parse the query into list of valid tokens.

        Each token is a valid segment in the JSONPath, with the last one possibly be
        empty or incomplete segments.

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
                    # last index is the end of a token
                    tokens.append(query[pre + 1: cur])
                    if cur < len(query) - 1 and query[cur + 1] == '.':
                        # bypass `..` query
                        cur += 1
                    pre = cur
                elif ch == '[':
                    if cur > 0:
                        tokens.append(query[pre + 1: cur])
                    open_brace += 1
                    pre = cur - 1
                elif ch == ']':
                    # even with array ']' seems a valid end token sign
                    tokens.append(query[pre + 1: cur + 1])
                    open_brace -= 1
                    pre = cur
            else:
                if ch == ']':
                    # current index is the end of a token
                    open_brace -= 1
                elif ch == '[':
                    open_brace += 1
                if open_brace == 0:
                    tokens.append(query[pre + 1: cur + 1])
                    pre = cur
            cur += 1
        # add the last token
        tokens.append(query[pre + 1: cur])
        return tokens

    # noinspection PyBroadException
    @staticmethod
    def _parse(query, tokens):
        """
        Parse the query with the help of tokens.

        :param query: the original query
        :type query: str
        :param tokens: the parsed tokens
        :type tokens: list
        :return: a parser, or None if the query is invalid
        """
        jsonpath_exp = None
        try:
            if tokens[-1] == '':
                # the input query is a valid JSONPath query or ends with '.'
                if query.endswith('..'):
                    jsonpath_exp = parse(query[:-2])
                elif query.endswith('.'):
                    jsonpath_exp = parse(query[:-1])
                else:
                    jsonpath_exp = parse(query)
            else:
                # the input query is incomplete
                last_complete_query = query[:-len(tokens[-1])]
                if last_complete_query.endswith('..'):
                    last_complete_query = last_complete_query[:-2]
                elif last_complete_query.endswith('.'):
                    last_complete_query = last_complete_query[:-1]
                jsonpath_exp = parse(last_complete_query)
        except Exception as e:
            # swallow this error but this should be something to fix
            logger.opt(exception=True) \
                .warning("Invalid query {} with parsed tokens {}", query, tokens)
        return jsonpath_exp

    @staticmethod
    def _list_options(data):
        """
        List all possible next values with the query result from last valid JSONPath query.

        :param data: the current query result
        :type data: dict, list, int, float, str, bool, None
        :return: potential options, return empty if `data` is not a composite JSON node
        """
        if len(data) > 1:
            return JSONPathAutoComplete._generate_list_completes(len(data))
        # extract the current node
        cur = data[0]
        if isinstance(cur, list):
            return JSONPathAutoComplete._generate_list_completes(len(cur))
        elif isinstance(cur, dict):
            return [key for key in cur.keys()]
        return []

    @staticmethod
    def _generate_list_completes(length):
        """
        Generates completes for an array, use its length also add `*` to represent
        everything.

        :param length: the list length
        :type length: int
        :return: completes for current length.
        """
        options = ['*']
        options.extend([str(index) for index in range(length)])
        return options

    @staticmethod
    def _filter_options(options, prefix):
        """
        Filters options based on a given prefix.

        :param options: list of valid options
        :type options: list
        :param prefix: current query prefix
        :type prefix: str
        :return:
        """
        if prefix == '' or (prefix.startswith('[') and len(prefix) <= 2):
            return options

        actual_prefix = prefix
        if prefix.startswith('['):
            # bracket style, needs to use the third char as prefix
            actual_prefix = prefix[2:]
        return list(filter(lambda option: option.startswith(actual_prefix), options))
