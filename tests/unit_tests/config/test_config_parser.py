import unittest

from pyfx.config import parse
from tests.fixtures import FIXTURES_DIR


class ConfigurationParserTest(unittest.TestCase):
    def test_parse_keymap_only(self):
        basic_config = FIXTURES_DIR / "configs" / "emacs.yml"
        configuration = parse(basic_config)
        self.assertEqual("emacs", configuration.ui.keymap.mode)
        self.assertEqual("basic", configuration.ui.theme)
