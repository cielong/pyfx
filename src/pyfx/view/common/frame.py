from dataclasses import dataclass

import urwid
from loguru import logger
from overrides import overrides
from urwid.util import is_mouse_press


@dataclass(frozen=True)
class FrameSnapshot:
    """A snapshot of the current state of the frame."""
    buffer: str
    mini_buffer: str


class Frame(urwid.Widget, urwid.WidgetContainerMixin):
    """An Emacs-like box widget designed for Pyfx use cases.

    It splits the whole terminal into three parts:
       buffer: a section used to show content
       information line: a one-line section to show some helpful information
       mini buffer: a mini editable section to type query etc.

    .. note:: Unlike ::class::`urwid.Frame`, this widget is designed to be the
    top widget used in :class:`urwid.MainLoop`.

    Attributes:
        `_buffers`: A map from string to available widget used in buffer.
        `_current_buffer`: the key of current widget for buffer in buffers
            (might not in focus)

        `_mini_buffers`: A map from string to available widget used in mini
            buffer.
        `_current_mini_buffer`: the key of current widget for mini buffer in
            mini buffers (might not in focus though).

        `_info_line`: A non-selectable text bar that displays helpful
            information.

        `_focus`: The key of current focused widget in the frame.
        `_focus_widget`: The current widget in focus.

        `_backup`: A snapshot of previous state. This is used to restore the
            frame into its previous state.
            E.g., when we popup a warning message, we temporarily switch the
            mini buffer but not focus on it.
    """

    def __init__(self, screen, buffers, mini_buffers,
                 current_buffer, current_mini_buffer):
        """
        Args:
            `screen`(urwid.raw_display.Screen): The screen object represents
                the whole terminal screen.
            `buffers`(dict<str, urwid.Widget>): a map from string to widget used
                in buffer.
            `mini_buffers`(dict<str, urwid.Widget>): a map from string to widget
                used in mini_buffer.
            `current_buffer`(string): the key of current focused widget for
                buffer in buffers.
            `current_mini_buffer`(string): the key of current focused widget
                for mini buffer in mini buffers.
        """
        self.__super.__init__()

        self._screen = screen

        self._buffers = buffers
        self._current_buffer = current_buffer

        self._mini_buffers = mini_buffers
        self._current_mini_buffer = current_mini_buffer

        self._focus = self._current_buffer
        self._focus_widget = self._buffers[self._current_buffer]
        self._info_line = self._create_info_widget(
            self._focus_widget.help_message())

        self._backups = []

    @property
    def buffer(self):
        return self._buffers[self._current_buffer]

    def set_buffer(self, widget_name):
        if widget_name not in self._buffers:
            return
        self._current_buffer = widget_name
        self._invalidate()

    @property
    def mini_buffer(self):
        return self._mini_buffers[self._current_mini_buffer]

    def set_mini_buffer(self, widget_name):
        if widget_name not in self._mini_buffers:
            return
        self._current_mini_buffer = widget_name
        self._invalidate()

    def size(self, widget_name):
        """
        Get the size of the respected widget
        """
        # FIXME: A hacky way to get the widget size to be used by Autocomplete.
        #  we should fix this by refactoring Autocomplete module.
        col, row = self._screen.get_cols_rows()
        if widget_name in self._buffers:
            return col, row - 1
        elif widget_name in self._mini_buffers:
            return col, 1
        return 0, 0

    @property
    def focus(self):
        return self._focus_widget

    def set_focus(self, widget_name):
        if widget_name in self._buffers:
            self._current_buffer = widget_name
            self._focus = self._current_buffer
            self._focus_widget = self._buffers[self._current_buffer]
        elif widget_name in self._mini_buffers:
            self._current_mini_buffer = widget_name
            self._focus = self._current_mini_buffer
            self._focus_widget = self._mini_buffers[self._current_mini_buffer]
        else:
            # swallow this error but log warnings
            logger.warning(f"Unknown widget `{widget_name}` to be focused.")
            return
        self._info_line = self._create_info_widget(
            self._focus_widget.help_message())
        self._invalidate()

    def set_no_focus(self, widget_name):
        """Switches the widget in the pre-defined area (buffer or mini_buffer).
           Don't focus on it.
        """
        if widget_name not in self._buffers and \
                widget_name not in self._mini_buffers:
            logger.warning(f"Unknown widget `{widget_name}`.")
            return

        if widget_name in self._buffers:
            self._current_buffer = widget_name
        else:
            self._current_mini_buffer = widget_name
        self._invalidate()

    def create_snapshot(self):
        self._backups.append(
            FrameSnapshot(self._current_buffer, self._current_mini_buffer))

    def restore(self, index):
        self._current_buffer = self._backups[index].buffer
        self._current_mini_buffer = self._backups[index].mini_buffer

        self._backups.clear()
        self._invalidate()

    def render(self, size, focus=False):
        current_buffer = self._buffers[self._current_buffer]
        current_mini_buffer = self._mini_buffers[self._current_mini_buffer]
        maxcol, maxrow = size
        mini_buffer_trimmed, mini_buffer_rows = self._mini_buffer_rows(
            size, focus)
        combine_list = []
        if mini_buffer_trimmed + 1 < maxrow:
            # There are more rows for buffer to display
            buffer_in_focus = focus and self._focus == self._current_buffer
            max_buffer_rows = maxrow - mini_buffer_trimmed - 1
            buffer = current_buffer.render(
                (maxcol, max_buffer_rows), buffer_in_focus)
            combine_list.append((buffer, 'body', buffer_in_focus))

        # Always render `_info_line`
        info_line = self._info_line.render((maxcol,))
        combine_list.append((info_line, 'info_line', False))

        # Always render `_mini_buffer`
        mini_buffer_in_focus = focus and \
            self._focus == self._current_mini_buffer
        if mini_buffer_trimmed < mini_buffer_rows:
            filler = urwid.Filler(current_mini_buffer, 'bottom')
            mini_buffer = filler.render((maxcol, mini_buffer_trimmed),
                                        mini_buffer_in_focus)
        else:
            mini_buffer = current_mini_buffer.render((maxcol,),
                                                     mini_buffer_in_focus)
        combine_list.append((mini_buffer, 'footer', mini_buffer_in_focus))

        return urwid.CanvasCombine(combine_list)

    def keypress(self, size, key):
        """Passes keypress to widget in focus."""
        maxcol, maxrow = size
        if self._focus in self._mini_buffers:
            # within mini_buffer
            if not self._focus_widget.selectable():
                return key

            if self._focus_widget.keypress((maxcol,), key) is None:
                return None
        else:
            visible_rows, total_rows = self._mini_buffer_rows(size, False)
            if visible_rows < total_rows:
                # the buffer is not visible
                return key
            elif not self._focus_widget.selectable():
                return key

            buffer_size = (maxcol, maxrow - 1 - visible_rows)
            if self._focus_widget.keypress(buffer_size, key) is None:
                return None
        return key

    def mouse_event(self, size, event, button, col, row, focus):
        """Passes mouse event to appropriate part of frame.
        Focus may be changed on button 1 press.
        """
        current_buffer = self._buffers[self._current_buffer]
        current_mini_buffer = self._mini_buffers[self._current_mini_buffer]
        maxcol, maxrow = size

        mini_buffer_trimmed, mini_buffer_rows = self._mini_buffer_rows(
            size, focus)

        if row >= maxrow - mini_buffer_trimmed:
            # within `_mini_buffer`
            if is_mouse_press(event) and button == 1:
                if current_mini_buffer.selectable():
                    self.set_focus(self._current_mini_buffer)
            if not hasattr(current_mini_buffer, 'mouse_event'):
                return False
            return current_mini_buffer.mouse_event(
                (maxcol,), event, button, col,
                # extra rows inside mini_buffer
                row - maxrow + mini_buffer_trimmed, focus)

        # within buffer
        if is_mouse_press(event) and button == 1:
            if current_buffer.selectable():
                self.set_focus(self._current_buffer)
        if not hasattr(current_buffer, 'mouse_event'):
            return False

        # one line for info_line
        max_buffer_rows = maxrow - mini_buffer_trimmed - 1
        return current_buffer.mouse_event(
            (maxcol, max_buffer_rows), event, button, col, row, focus)

    def get_cursor_coords(self, size):
        """Returns the cursor coordinates of the focus widget."""
        current_buffer = self._buffers[self._current_buffer]
        current_mini_buffer = self._mini_buffers[self._current_mini_buffer]
        if not self._focus_widget.selectable():
            return None, None
        elif not hasattr(self._focus_widget, 'get_cursor_coords'):
            return None, None

        maxcol, maxrow = size
        mini_buffer_rows, _ = self._mini_buffer_rows(size, True)

        if self._focus == self._current_buffer:
            row_adjust = 0
            # one line for `_info_line`
            coords = current_buffer.get_cursor_coords(
                (maxcol, maxrow - mini_buffer_rows - 1))
        else:
            # in mini-buffer
            row_adjust = maxrow - mini_buffer_rows
            coords = current_mini_buffer.get_cursor_coords((maxcol,))

        if coords is None:
            return None, None

        x, y = coords
        return x, y + row_adjust

    @overrides
    def selectable(self):
        """Frame is always selectable."""
        return True

    @overrides
    def sizing(self):
        return frozenset([urwid.BOX])

    def _create_info_widget(self, keys):
        text = f"Pyfx        {' '.join(keys)}"
        return urwid.AttrMap(urwid.Columns(
            [urwid.Text(text, wrap=urwid.CLIP)]), 'help')

    def _mini_buffer_rows(self, size, focus):
        """Calculates the number of rows for the mini_buffer.

        Args:
            size(int): see :meth:`urwid.Widget.render` for details.
            focus(bool): ``True`` is this widget is in focus.

        Returns:
            A tuple of (visible mini-buffer rows, total mini-buffer rows)
        """
        (maxcol, maxrow) = size

        mini_buffer_rows = self._mini_buffers[self._current_mini_buffer].rows(
            (maxcol,), focus)

        if mini_buffer_rows + 1 >= maxrow:
            # one line for `_info_line`
            return maxrow - 1, mini_buffer_rows

        return mini_buffer_rows, mini_buffer_rows
