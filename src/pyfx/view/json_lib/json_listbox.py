import urwid
from loguru import logger
from overrides import overrides


class JSONListBox(urwid.ListBox):
    """
    a ListBox with special handling for navigation and collapsing of JSONWidgets
    """
    def __init__(self, walker):
        # set body to JSONListWalker
        super().__init__(walker)

    @overrides
    def keypress(self, size, key):
        (maxcol, maxrow) = size

        if self.set_focus_pending or self.set_focus_valign_pending:
            self._set_focus_complete((maxcol, maxrow), focus=True)

        focus_widget, pos = self._body.get_focus()
        if focus_widget is None:
            # empty listbox, can't do anything
            return key

        if focus_widget.selectable():
            key = focus_widget.keypress((maxcol,), key)
            if key is None:
                self.make_cursor_visible((maxcol, maxrow))
                return None

        if key == "up":
            self.move_focus_to_prev_line(size)

        elif key == "down":
            self.move_focus_to_next_line(size)

        elif key == "enter":
            self.toggle_collapse_on_focused_parent(size)

        return key

    def toggle_collapse_on_focused_parent(self, size):
        """
        toggle collapse on JSON `object` or `array` node
        """

        widget, position = self.get_focus()
        if not widget.is_expandable():
            return

        position.toggle_expanded()

        if position.is_end_node() and (not position.is_expanded()):
            # switch to unexpanded widget when collapse on end widget
            self.change_focus(size, position.get_start_node())

        self._invalidate()

    def move_focus_to_prev_line(self, size):
        """
        move focus to previous line
        """
        maxcol, maxrow = size

        widget, position = self.get_focus()

        prev_widget, prev_position = self._body.get_prev(position)

        if prev_position is None:
            return

        middle, top, bottom = self.calculate_visible(size, True)

        if middle is None:
            # this should not happen and need to be look into.
            logger.info(f"{self}.calculate_visible({size}, True) returns middle as None")
            return

        row_offset, focus_widget, focus_pos, focus_rows, cursor = middle
        trim_top, fill_above = top

        # fetch the first widget above if exist
        if len(fill_above) > 0:
            widget, position, rows = fill_above[0]
            self.change_focus(size, position, row_offset - rows)
            return

        # must scroll since we at the first row of the current canvas
        self._invalidate()

        self.change_focus(size, prev_position, 0, 'below')

    def move_focus_to_next_line(self, size):
        """
        move focus to next line
        """
        maxcol, maxrow = size

        widget, position = self.get_focus()

        next_widget, next_position = self._body.get_next(position)

        if next_position is None:
            # still need to calculate visible, in case of expansion
            self.calculate_visible(size, True)
            return

        middle, top, bottom = self.calculate_visible(size, True)

        if middle is None:
            # this should not happen and need to be look into.
            logger.info(f"{self}.calculate_visible({size}, True) returns middle as None")
            return

        row_offset, focus_widget, focus_pos, focus_rows, cursor = middle
        bottom_top, fill_below = bottom

        # fetch the first widget below
        if len(fill_below) > 0:
            widget, position, rows = fill_below[0]
            self.change_focus(size, position, row_offset + focus_rows)
            return

        # must scroll since we at the last row of the current canvas
        self._invalidate()

        self.change_focus(size, next_position, maxrow, 'above')
