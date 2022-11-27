import unittest

from pyfx.config import parse
from pyfx.error import PyfxException
from tests.fixtures import FIXTURES_DIR


class ConfigurationParserTest(unittest.TestCase):
    def test_parse_keymap_only(self):
        config = FIXTURES_DIR / "configs" / "emacs.yml"
        configuration = parse(config)
        self.assertEqual("emacs", configuration.ui.keymap.mode)
        self.assertEqual("basic", configuration.ui.theme)

    def test_parse_invalid(self):
        config = FIXTURES_DIR / "configs" / "invalid_config.yml"
        self.assertRaisesRegex(PyfxException, r"Parse and validate .*",
                               parse(config))
