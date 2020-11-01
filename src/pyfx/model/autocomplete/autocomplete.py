"""
Auto-completion module for JSONPath query.
"""
import re

from ..common import Parser


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

        # 1. parse and find last valid query
        prefix, jsonpath_exp = Parser.parse(query)

        if jsonpath_exp is None:
            # something wrong inside `parse`
            # return nothing here and the error is logger inside Parser.parse
            return '', []

        current_data = [match.value for match in jsonpath_exp.find(data)]

        # 2. list valid options on the current node
        options = JSONPathAutoComplete._list_options(current_data, prefix)

        return prefix, options

    @staticmethod
    def _list_options(data, prefix):
        """
        List all possible next values with the query result from last valid JSONPath query with given prefix.

        :param data: the current query result
        :type data: dict, list, int, float, str, bool, None
        :return: potential options, return empty if `data` is not a composite JSON node
        """
        options = []
        if len(data) > 1:
            options = JSONPathAutoComplete._generate_list_completes(len(data), prefix)
        else:
            # extract the current node
            cur = data[0]
            if isinstance(cur, list):
                options = JSONPathAutoComplete._generate_list_completes(len(cur), prefix)
            elif isinstance(cur, dict):
                for key in cur.keys():
                    if re.match(r'.*[\.\[\]].*', key) or prefix.startswith('['):
                        options.append("['" + key + "']")
                    else:
                        options.append(key)
                options = list(filter(lambda k: k.startswith(prefix), options))

        return options

    @staticmethod
    def _generate_list_completes(length, prefix):
        """
        Generates completes for an array, use its length also add `*` to represent
        everything.

        :param length: the list length
        :type length: int
        :return: completes for current length.
        """
        options = ['[*]']
        options.extend(['[' + str(index) + ']' for index in range(length)])
        return list(filter(lambda k: k.startswith(prefix), options))
