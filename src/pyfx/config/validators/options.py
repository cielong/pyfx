from overrides import overrides
from yamale.validators import Validator


class Options(Validator):
    tag = 'options'

    @overrides
    def __init__(self, *args, **kwargs):
        super(Options, self).__init__(*args, **kwargs)
        self.options = set(args)

    @overrides
    def _is_valid(self, value):
        return value in self.options

    @overrides
    def fail(self, value):
        return f"'{value}' is not a valid option in {tuple(sorted(self.options))}"
