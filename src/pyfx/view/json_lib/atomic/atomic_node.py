from .atomic_widget import AtomicWidget
from ..json_simple_node import JSONSimpleNode


class AtomicNode(JSONSimpleNode):
    """
    implementation of JSON `string`, `integer`, `number`, `boolean` and `null` type node
    """
    # =================================================================================== #
    # ui                                                                                  #
    # =================================================================================== #

    def load_widget(self):
        return AtomicWidget(self, self.is_display_key())
