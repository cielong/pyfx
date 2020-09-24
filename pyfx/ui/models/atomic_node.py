from overrides import overrides

from pyfx.ui.models.json_simple_node import JSONSimpleNode
from pyfx.ui.widgets.atomic_widget import AtomicWidget

from typing import Union


class AtomicNode(JSONSimpleNode):
    """
    implementation of JSON `string`, `integer`, `number`, `boolean` and `null` type node
    """
    # =================================================================================== #
    # ui                                                                                  #
    # =================================================================================== #

    def load_widget(self):
        return AtomicWidget(self, self.is_display_key())
