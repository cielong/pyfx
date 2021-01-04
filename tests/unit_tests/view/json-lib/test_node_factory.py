import unittest

from pyfx.view.json_lib import NodeFactory


def inorder_traverse(root):
    """
    Helper function to walk the tree and generate the inorder route
    """
    routes = []
    stack = []
    cur = root
    while (cur is not None) or (len(stack) > 0):
        if cur is None:
            cur = stack.pop().get_end_node()

        routes.append(cur)

        if (not hasattr(cur, 'has_children')) or cur.is_end_node():
            cur = cur.next_sibling()
        else:
            stack.append(cur)
            cur = cur.get_first_child()

    return routes


class NodeFactoryTest(unittest.TestCase):
    def test_create_root_node_with_row_index(self):
        data = {
            "k1": {
                "k1.1": 'val'
            }
        }
        
        root = NodeFactory.create_root_node(data, assign_row_index=True)

        node_routes = inorder_traverse(root)

        node_indices = [r.get_index() for r in node_routes]

        self.assertEqual(list(range(0, 5)), node_indices)
