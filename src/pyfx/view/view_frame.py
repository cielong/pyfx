from overrides import overrides

from .common import PopUpLauncher, Frame


class ViewFrame(PopUpLauncher):
    """
    A wrapper of the frame as the main UI of Pyfx.

    This is created to provide pop up support in Pyfx.
    """

    def __init__(self, screen, bodies, footers, popups_factory,
                 default_body, default_footer):
        self._popup_factories = popups_factory
        super().__init__(Frame(
            screen=screen,
            buffers=bodies,
            mini_buffers=footers,
            current_buffer=default_body,
            current_mini_buffer=default_footer,
        ))

    def focus(self, widget_name):
        self.original_widget.set_focus(widget_name)

    def size(self, widget_name):
        return self.original_widget.size(widget_name)

    # This is a workaround we used to be able to popup autocomplete window in
    # query bar
    # The implementation of PopUpLauncher only support pop up within the
    # launcher's canvas, i.e., autocomplete-edit's popup launcher should be
    # implemented in the container widget of the edit widget
    @overrides
    def create_pop_up(self, *args, **kwargs):
        popup_factory = kwargs['pop_up_type']
        del kwargs['pop_up_type']
        return self._popup_factories[popup_factory](*args, **kwargs)
