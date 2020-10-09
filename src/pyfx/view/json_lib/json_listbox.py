import urwid

from .json_listwalker import JSONListWalker


class JSONListBox(urwid.ListBox):
    """
    a ListBox with special handling for navigation and collapsing of JSONWidgets
    """

    def __init__(self,
                 walker: JSONListWalker
                 ):
        # set body to JSONListWalker
        super().__init__(walker)

    def keypress(self, size, key):
        key = super().keypress(size, key)
        if key in ('up', 'ctrl p'):
            self.move_focus_to_prev_line(size)
        elif key in ('down', 'ctrl n'):
            self.move_focus_to_next_line(size)
        elif key == 'enter':
            self.toggle_collapse_on_focused_parent(size)
        return key

    def toggle_collapse_on_focused_parent(self, size):
        """
        toggle collapse on JSON `object` or `array` node
        """

        widget, position = self.get_focus()
        if not widget.is_expandable():
            return

        if position.is_end_node() and (not position.is_expanded()):
            # switch to unexpanded widget when collapse on end widget
            self.change_focus(size, position.get_start_node())

        self._invalidate()

    def move_focus_to_prev_line(self, size):
        """
        move focus to previous line
        """

        widget, position = self.get_focus()

        prev_widget, prev_position = self._body.get_prev(position)

        if prev_position is None:
            return

        middle, top, bottom = self.calculate_visible(size)

        row_offset, focus_widget, focus_pos, focus_rows, cursor = middle
        trim_top, fill_above = top

        # fetch the first widget above
        widget, position, rows = fill_above[0]
        self.change_focus(size, position, row_offset - rows)

    def move_focus_to_next_line(self, size):
        """
        move focus to next line
        """

        widget, position = self.get_focus()

        next_widget, next_position = self._body.get_next(position)

        if next_position is None:
            # still need to calculate visible, in case of expansion
            self.calculate_visible(size)
            return

        middle, top, bottom = self.calculate_visible(size)

        row_offset, focus_widget, focus_pos, focus_rows, cursor = middle
        bottom_top, fill_below = bottom

        # fetch the first widget below
        widget, position, rows = fill_below[0]
        self.change_focus(size, position, row_offset + rows)
