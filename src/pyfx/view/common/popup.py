from urwid import CompositeCanvas
from urwid import delegate_to_widget_mixin
from urwid import WidgetDecoration


class PopUpLauncher(delegate_to_widget_mixin('_original_widget'),
                    WidgetDecoration):
    """
    Re-implementation of :py:class:`urwid.PopUpLauncher` to add support for passing
    parameter when create/open pop-ups.

    This helps to create pop-ups with changing information.
    This reimplementation also pass size to :py:method:`.get_pup_up_parameters` when
    rendering, which helps to dynamically decide the position of the popups.
    """

    def __init__(self, original_widget):
        super().__init__(original_widget)
        self._pop_up_widget = None

    @property
    def pop_up_widget(self):
        return self._pop_up_widget

    def create_pop_up(self, *args, **kwargs):
        """
        Subclass must override this method and return a widget
        to be used for the pop-up.  This method is called once each time
        the pop-up is opened.
        """
        raise NotImplementedError("Subclass must override this method")

    def get_pop_up_parameters(self, *args, **kwargs):
        """
        Subclass must override this method and have it return a dict, eg:

        {'left':0, 'top':1, 'overlay_width':30, 'overlay_height':4}

        This method is called each time this widget is rendered.
        """
        raise NotImplementedError("Subclass must override this method")

    def open_pop_up(self, *args, **kwargs):
        self._pop_up_widget = self.create_pop_up(*args, **kwargs)
        self._invalidate()

    def close_pop_up(self, *args, **kwargs):
        self._pop_up_widget = None
        self._invalidate()

    def render(self, size, focus=False):
        canvas = super().render(size, focus)
        if self._pop_up_widget:
            canvas = CompositeCanvas(canvas)
            canvas.set_pop_up(
                self._pop_up_widget,
                **self.get_pop_up_parameters(size)
            )
        return canvas
