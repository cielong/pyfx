from overrides import overrides

from pyfx.view.json_lib.json_composite_end_node import JSONCompositeEndNode
from pyfx.view.json_lib.json_composite_node import JSONCompositeNode
from pyfx.view.json_lib.json_node_creator import JSONNodeCreator
from pyfx.view.json_lib.object.object_end_widget import ObjectEndWidget
from pyfx.view.json_lib.object.object_start_widget import ObjectStartWidget
from pyfx.view.json_lib.object.object_unexpanded_widget import \
    ObjectUnexpandedWidget


class TestClass:
    """
    A class used as a self-defined user class
    """

    def __init__(self, id, name, flag):
        self._id = id
        self._name = name
        self._flag = flag

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def flag(self):
        return self._flag


class TestClassNodeCreator(JSONNodeCreator):
    def __init__(self, node_factory):
        self._node_factory = node_factory

    @overrides
    def create_node(self, key, value, **kwargs):
        if isinstance(value, TestClass):
            return TestClassNode(key, value, self._node_factory, **kwargs)
        return None


class TestClassEndNode(JSONCompositeEndNode):

    def load_widget(self):
        return ObjectEndWidget(self)


class TestClassNode(JSONCompositeNode):

    def __init__(self, key, value, node_factory,
                 parent=None, display_key=True):
        super().__init__(key, value, node_factory, parent, display_key)
        self._children = {}
        self._props = ['id', 'name', 'flag']

    def collapse_all(self):
        for prop, val in vars(self.get_value()).items():
            if isinstance(val, (JSONCompositeNode, JSONCompositeEndNode)):
                val.collapse_all()
        if self.is_expanded():
            self.toggle_expanded()

    def has_children(self):
        return True

    def get_first_child(self):
        return self._get_child_node(self._props[0])

    def get_last_child(self):
        return self._get_child_node(self._props[-1])

    def prev_child(self, key):
        index = self._props.index(key)
        if index == 0:
            return None
        return self._get_child_node(self._props[index - 1])

    def next_child(self, key):
        index = self._props.index(key)
        if index == 2:
            return None
        return self._get_child_node(self._props[index + 1])

    def _get_child_node(self, key):
        if key not in self._children:
            self._children[key] = self._load_child_node(key)
        return self._children[key]

    def _load_child_node(self, key):
        value = getattr(self.get_value(), key)
        return self._node_factory.create_node(key, value, parent=self,
                                              display_key=True)

    def load_end_node(self):
        return TestClassEndNode(self)

    def load_start_widget(self):
        return ObjectStartWidget(self, self.is_display_key())

    def load_unexpanded_widget(self):
        return ObjectUnexpandedWidget(self, self.is_display_key())
