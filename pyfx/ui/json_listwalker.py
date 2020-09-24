import urwid

from overrides import overrides


class JSONListWalker(urwid.ListWalker):
    """
    ListWalker-compatible class for displaying :ref:`pyfx.ui.widgets.JSONWidget`,
    positions are represented by :ref:`pyfx.ui.models.JSONNode`

    it contains the following elements:
    * start_from: "JSONSimpleNode" with the initial focus
    """

    def __init__(self,
                 start_from: "JSONSimpleNode"
                 ):
        self._focus = start_from

    # =================================================================================== #
    # getters and setters                                                                 #
    # =================================================================================== #
    # focus
    @overrides
    def get_focus(self):
        widget = self._focus.get_widget()
        return widget, self._focus

    def set_focus(self,
                  focus: "JSONSimpleNode"
                  ):
        self._focus = focus
        self._modified()

    # =================================================================================== #
    # movement                                                                            #
    # =================================================================================== #

    @overrides
    def get_next(self,
                 position: "JSONSimpleNode"
                 ):
        widget = position.get_widget()
        target = widget.next_inorder()
        if target is None:
            return None, None
        else:
            return target, target.get_node()

    @overrides
    def get_prev(self,
                 position: "JSONSimpleNode"
                 ):
        widget = position.get_widget()
        target = widget.prev_inorder()
        if target is None:
            return None, None
        else:
            return target, target.get_node()
