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

    def test_start(self):
        runner = CliRunner(mix_stderr=False)
        with runner.isolated_filesystem():
            with open('test.json', 'w') as f:
                f.write('1')
            result = runner.invoke(main, args=('test.json',))

            # the input inside CliRunner is a fake input, and will cause pyfx
            # crash
            self.assertEqual(result.exit_code, 1)
            self.assertEqual(result.stderr, "Error: Unknown error: fileno.\n")
