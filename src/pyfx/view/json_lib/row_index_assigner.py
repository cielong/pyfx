class RowIndexAssigner:
    """
    An inorder-traversing visitor which traverse JSONNodes and assign row
    index on each node.
    """
    def __init__(self):
        self._max_row_index = 0

    @property
    def max_row_index(self):
        return self._max_row_index

    def __get_and_increment_row_index(self):
        index = self._max_row_index
        self._max_row_index += 1
        return index

    def visit(self, root_node):
        stack = []
        cur = root_node
        while (cur is not None) or (len(stack) > 0):
            if cur is None:
                cur = stack.pop().get_end_node()

            cur.set_index(self.__get_and_increment_row_index())

            if (not hasattr(cur, 'has_children')) or cur.is_end_node():
                cur = cur.next_sibling()
            else:
                stack.append(cur)
                cur = cur.get_first_child()
