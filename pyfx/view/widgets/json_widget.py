import urwid
from overrides import overrides


class JSONWidget(urwid.WidgetWrap):
    """
    abstract base widget representing something in a nested display
    a JSONWidget contains the following elements:
    * node: JSONSimpleNode
    * expandable: is expandable or not
    * display_key: whether to display key or not
    * inner_widget: text display of current node
    * expanded: flag indicate the current widget is expanded
    """

    """
    unit width of a indent for each depth of a node
    """
    INDENT_COLUMN = 3

    def __init__(self,
                 node: "JSONNode",
                 expandable: bool,
                 display_key: bool,  # flag to indicate display key or not (distinguish array and object)
                 ):
        self._node = node
        self._expandable = expandable
        self._display_key = display_key
        self._inner_widget = None
        # not expanded by default
        self._expanded = False
        widget = self.get_indented_widget()
        super().__init__(widget)

    # =================================================================================== #
    # getters and setters                                                                 #
    # =================================================================================== #

    # node
    def get_node(self):
        return self._node

    # inner_widget
    def get_inner_widget(self):
        if self._inner_widget is None:
            self._inner_widget = self.load_inner_widget()
        return self._inner_widget

    def load_inner_widget(self):
        return _SelectableText(self.get_display_text())

    # expandable
    def is_expandable(self):
        return self._expandable

    # display key
    def is_display_key(self):
        return self._display_key

    # =================================================================================== #
    # display                                                                             #
    # =================================================================================== #

    def get_indented_widget(self):
        widget = self.get_inner_widget()
        indent_cols = self.get_indent_cols()
        indented_widget = urwid.Padding(widget, width=('relative', 100), left=indent_cols)
        return urwid.AttrWrap(indented_widget, None, "focus")

    def get_indent_cols(self):
        return JSONWidget.INDENT_COLUMN * self._node.get_depth()

    def get_display_text(self):
        raise AttributeError("Not implemented in abstract JSONWidget class")

    # =================================================================================== #
    # moving around logic                                                                 #
    # =================================================================================== #

    def next_inorder(self):
        """ return the next TreeWidget depth first from this one """
        # first check if there's a child widget
        first_child = self.first_child()
        if first_child is not None:
            return first_child

        # now we need to hunt for the next sibling
        current_node = self._node
        current_depth = self._node.get_depth()
        next_node = self._node.next_sibling()
        while next_node is None and current_depth > 0:
            # keep going up the tree until we find an ancestor next sibling
            current_node = current_node.get_parent()
            next_node = current_node.next_sibling()
            current_depth -= 1
            assert current_depth == current_node.get_depth()

        if next_node is None:
            # we're at the end of the file
            return None
        else:
            return next_node.get_widget()

    def first_child(self):
        """ return first child if expanded """
        if not self._expandable or not self._expanded:
            return None
        else:
            # node is not leaf and expandable
            if self._node.has_children():
                first_node = self._node.get_first_child()
                return first_node.get_widget()
            else:
                # node has empty children
                # logic for finding the next sibling is in `next_inorder`
                return None

    def prev_inorder(self):
        """ return the previous TreeWidget depth first from this one """
        current_node = self._node
        prev_node = current_node.prev_sibling()
        if prev_node is not None:
            # we need to find the last child of the previous widget if its
            # expanded
            prev_widget = prev_node.get_widget()
            last_child = prev_widget.last_child()
            if last_child is None:
                return prev_widget
            else:
                return last_child

        # need to hunt for the parent
        current_depth = self._node.get_depth()
        if current_depth == 0:
            # we're at the start of the file
            return None
        # return parent widget since we're the first child of current parent
        return current_node.get_parent().get_widget()

    def last_child(self):
        """ return last child if expanded """
        if not self._expandable or not self._expanded:
            return None
        else:
            if self._node.has_children():
                last_child = self._node.get_last_child().get_widget()
            else:
                return None
            # recursively search down for the last descendant
            last_descendant = last_child.last_child()
            if last_descendant is None:
                return last_child
            else:
                return last_descendant

    # =================================================================================== #
    # keyboard and mouse definition                                                       #
    # =================================================================================== #

    def selectable(self):
        """ always true, every line is selectable but only non-leaf nodes are expandable """
        return True

    def keypress(self, size, key):
        """Handle expand & collapse requests (non-leaf nodes)"""
        if not self._expandable:
            return key

        if key == "enter":
            # toggle expanded
            self._expanded = not self._expanded
            # still return key to make :ref:`json_listbox.JSONListBox` to correctly re-render
            return key
        elif self._w.selectable():
            return super().keypress(size, key)
        else:
            return key

    def mouse_event(self, size, event, button, col, row, focus):
        if not self._expandable or event != 'mouse press' or button != 1:
            return False

        if row == 0 and col == self.get_indent_cols():
            self._expanded = not self._expanded
            return True

        return False


class _SelectableText(urwid.Text):
    """
    internal text widget to allow selectable
    """

    @overrides
    def selectable(self):
        return True

    def keypress(self, size, key):
        return key
