import urwid

from pyfx.view.json_listwalker import JSONListWalker


class JSONListBox(urwid.ListBox):
    """
    a ListBox with special handling for navigation and
    collapsing of TreeWidgets
    """
    def __init__(self,
                 walker: JSONListWalker
                 ):
        # set body to JSONListWalker
        super().__init__(walker)

    def keypress(self, size, key):
        key = super().keypress(size, key)
        return self.unhandled_input(size, key)

    def unhandled_input(self, size, key) -> str:
        """
        handle macro-navigation keys

        :param size int, widget size
        :param key str, keyboard input

        :return unhandled keyboard input
        """
        if key in ('up', 'ctrl p'):
            self.move_focus_to_prev_line(size)
        elif key in ('down', 'ctrl n'):
            self.move_focus_to_next_line(size)
        elif key == 'enter':
            self.toggle_collapse_on_focused_parent(size)
        else:
            return key

    def toggle_collapse_on_focused_parent(self, size):
        """
        toggle collapse on parent directory
        """

        widget, position = self.get_focus()
        if not widget.is_expandable():
            return

        # TODO: add toggle logic for non-leaf nodes
        self._invalidate()

    def move_focus_to_prev_line(self, size):
        """ move focus to previous line """

        widget, position = self.get_focus()

        prev_widget, prev_position = self._body.get_prev(position)

        if prev_position is None:
            return

        middle, top, bottom = self.calculate_visible(size)

        row_offset, focus_widget, focus_pos, focus_rows, cursor = middle
        trim_top, fill_above = top

        for widget, position, rows in fill_above:
            row_offset -= rows
            if position == prev_position:
                self.change_focus(size, position, row_offset)
                return

        self.change_focus(size, position.get_parent())

    def move_focus_to_next_line(self, size):
        """ move focus to next line """

        widget, position = self.get_focus()

        next_widget, next_position = self._body.get_next(position)

        if next_position is None:
            return

        middle, top, bottom = self.calculate_visible(size)

        row_offset, focus_widget, focus_pos, focus_rows, cursor = middle
        bottom_top, fill_below = bottom

        for widget, position, rows in fill_below:
            row_offset += rows
            if position == next_position:
                self.change_focus(size, position, row_offset)
                return

        self.change_focus(size, position.get_parent())

    def _keypress_max_left(self, size):
        return self.focus_home(size)

    def focus_home(self, size):
        """Move focus to very top."""

        widget, pos = self.body.get_focus()
        root_node = pos.get_root()
        self.change_focus(size, root_node)

    def _keypress_max_right(self, size):
        return self.focus_end(size)

    def focus_end(self, size):
        """Move focus to far bottom."""

        maxrow, maxcol = size
        widget, pos = self.body.get_focus()
        rootnode = pos.get_root()
        rootwidget = rootnode.get_widget()
        lastwidget = rootwidget.last_child()
        lastnode = lastwidget.get_node()

        self.change_focus(size, lastnode, maxrow - 1)
