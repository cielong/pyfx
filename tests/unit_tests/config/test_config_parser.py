import pathlib
import unittest

from pyfx.config import parse

here = pathlib.Path(__file__).parent.resolve()


class ConfigurationParserTest(unittest.TestCase):
    def test_parse_keymap_only(self):
        keymap_only_config = here / "configs" / "keymap_only.yml"
        configuration = parse(keymap_only_config)
        self.assertEqual("emacs", configuration.view.keymap.mode)
        self.assertIsNotNone(configuration.view.keymap.mapping)
        self.assertEqual("basic", configuration.view.appearance.theme)
        self.assertIsNotNone(configuration.view.appearance.color_scheme)
