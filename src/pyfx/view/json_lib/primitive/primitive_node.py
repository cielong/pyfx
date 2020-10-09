from .primitive_widget import PrimitiveWidget
from ..json_simple_node import JSONSimpleNode


class PrimitiveNode(JSONSimpleNode):
    """
    implementation of JSON `string`, `integer`, `number`, `boolean` and `null` type node
    """
    # =================================================================================== #
    # ui                                                                                  #
    # =================================================================================== #

    def load_widget(self):
        return PrimitiveWidget(self, self.is_display_key())
