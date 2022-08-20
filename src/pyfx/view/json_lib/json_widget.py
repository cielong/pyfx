import urwid
from overrides import overrides

from ..common import SelectableText


class JSONWidget(urwid.WidgetWrap):
    """
    base widget represents something in a nested display
    a JSONWidget contains the following elements:
    * node: JSONSimpleNode
    * expandable: is expandable or not
    * display_key: whether to display key or not
    * inner_widget: text display of current node
    """

    """
    unit width of a indent for each depth of a node
    """
    INDENT_COLUMN = 3

    def __init__(self, node, expandable, display_key):
        self._node = node
        self._expandable = expandable
        self._display_key = display_key
        self._inner_widget = None
        super().__init__(self.get_indented_widget())

    # ====================================================================== #
    # getters and setters                                                    #
    # ====================================================================== #

    # node
    def get_node(self):
        return self._node

    # inner_widget
    def get_inner_widget(self):
        if self._inner_widget is None:
            self._inner_widget = self.load_inner_widget()
        return self._inner_widget

    def load_inner_widget(self):
        if not self.is_display_key():
            return SelectableText(self.load_value_markup())

        # FIXME: urwid.Columns will discard the calculated column if the column
        #  width is 0, regardless of whether the column itself has 0 width or it
        #  does not fit the whole row
        return urwid.Columns([
            ('pack',
             SelectableText([
                 ('json.key', '"' + str(self.get_node().get_key()) + '"'),
                 ": "
             ])
             ),
            SelectableText(self.load_value_markup())
        ])

    def load_value_markup(self):
        raise NotImplementedError(
            f"{type(self)} has not implemented #load_value_markup"
        )

    # expandable
    def is_expandable(self):
        return self._expandable

    # display key
    def is_display_key(self):
        return self._display_key

    # ====================================================================== #
    # display                                                                #
    # ====================================================================== #

    def get_indented_widget(self):
        widget = self.get_inner_widget()
        indent_cols = self.get_indent_cols()
        indented_widget = urwid.Padding(
            widget, width=('relative', 100), left=indent_cols
        )
        focus_attr_map = {
            None: 'json.focused',  # default
            'json.key': 'json.focused',
            'json.string': 'json.focused',
            'json.null': 'json.focused',
            'json.numeric': 'json.focused',
            'json.integer': 'json.focused',
            'json.bool': 'json.focused',
            'json.generic': 'json.focused',
        }
        return urwid.AttrMap(indented_widget, None, focus_attr_map)

    def get_indent_cols(self):
        return JSONWidget.INDENT_COLUMN * self._node.get_depth()

    # ====================================================================== #
    # moving around                                                          #
    # ====================================================================== #

    def next_inorder(self):
        """
        return the next JSONWidget depth first from this one
        """
        # first check if there's a child widget
        current_node = self._node

        if hasattr(current_node, "has_children") and \
                self == self._node.get_start_widget():
            # current_node is a composite node and current node is focus on
            # start widget
            first_child = current_node.get_first_child()
            if first_child is not None:
                if hasattr(first_child, "has_children"):
                    # first_child can be composite node
                    if first_child.is_expanded():
                        return first_child.get_start_widget()
                    else:
                        return first_child.get_unexpanded_widget()
                else:
                    # simple node
                    return first_child.get_widget()
            return current_node.get_end_node().get_widget()
        # current node is a simple node
        # we need to hunt for the next sibling
        next_node = self._node.next_sibling()
        if next_node is not None:
            if hasattr(next_node, "has_children"):
                # next_node can be composite node
                if next_node.is_expanded():
                    return next_node.get_start_widget()
                else:
                    return next_node.get_unexpanded_widget()
            else:
                return next_node.get_widget()
        # current node is the last node
        current_depth = self._node.get_depth()
        if current_depth == 0:
            # we're at the start of the file
            return None
        return current_node.get_parent().get_end_node().get_widget()

    def prev_inorder(self):
        """
        return the previous JSONWidget depth first from this one
        """
        current_node = self._node

        if current_node.is_end_node():
            # current node is a composite node and current focus is on
            # end_widget
            last_child = current_node.get_last_child()
            if last_child is not None:
                if hasattr(last_child, "has_children"):
                    # first_child can be composite node
                    if last_child.is_expanded():
                        return last_child.get_end_node().get_widget()
                    else:
                        return last_child.get_unexpanded_widget()
                else:
                    # simple node
                    return last_child.get_widget()
            return current_node.get_start_node().get_widget()

        # simple node
        prev_node = current_node.prev_sibling()
        if prev_node is not None:
            # we need to find the last child of the previous widget if its
            # expanded
            if hasattr(prev_node, "has_children"):
                # prev_node can be composite node
                if prev_node.is_expanded():
                    return prev_node.get_end_node().get_widget()
                else:
                    return prev_node.get_unexpanded_widget()
            else:
                return prev_node.get_widget()

        # need to hunt for the parent
        current_depth = self._node.get_depth()
        if current_depth == 0:
            # we're at the start of the file
            return None
        # return parent widget since we're the first child of current parent
        return current_node.get_parent().get_start_widget()

    # ====================================================================== #
    # keyboard and mouse definition                                          #
    # ====================================================================== #

    @overrides
    def selectable(self):
        """
        Always true, every line in pyfx is selectable but only non-leaf nodes
        are expandable
        """
        return True

    @overrides
    def keypress(self, size, key):
        """
        Delegate keypress into inner widget
        """
        if self._w.selectable():
            key = self._w.keypress(size, key)

        return key
