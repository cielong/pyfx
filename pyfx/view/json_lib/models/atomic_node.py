from pyfx.view.json_lib.models.json_simple_node import JSONSimpleNode
from pyfx.view.json_lib.widgets.atomic_widget import AtomicWidget


class AtomicNode(JSONSimpleNode):
    """
    implementation of JSON `string`, `integer`, `number`, `boolean` and `null` type node
    """
    # =================================================================================== #
    # ui                                                                                  #
    # =================================================================================== #

    def load_widget(self):
        return AtomicWidget(self, self.is_display_key())
