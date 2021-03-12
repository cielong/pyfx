import unittest

from click.testing import CliRunner

from pyfx.__version__ import __version__
from pyfx.cli import main


class CliTest(unittest.TestCase):

    def test_help(self):
        runner = CliRunner()
        result = runner.invoke(main, '--help')
        self.assertEqual(result.exit_code, 0)

    def test_version(self):
        runner = CliRunner()
        result = runner.invoke(main, '--version')
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, f"pyfx, version {__version__}\n")
