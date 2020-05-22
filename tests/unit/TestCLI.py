import unittest

from src.cli.ArgParser import parse_arguments

class TestCLI(unittest.TestCase):

    def test_file_name(self):
        command = ['main.py', 'file_foo']
        args = parse_arguments(command)
        self.assertEqual(args.file, 'file_foo')

    def test_default_arguments(self):
        command = ['main.py', 'file']
        args = parse_arguments(command)
        self.assertEqual(vars(args), {
            'file': 'file',
            'o': './output',
            'n': 1,
            'preview': False,
            'suppress_warnings': False
        })
    
    def test_output_file(self):
        command = ['main.py', 'file', '-o', 'out_foo']
        args = parse_arguments(command)
        self.assertEqual(args.o, 'out_foo')

    def test_candidates(self):
        command = ['main.py', 'file', '-n', '500']
        args = parse_arguments(command)
        self.assertEqual(args.n, 500)
    
    def test_suppress_warnings(self):
        command = ['main.py', 'file', '--suppress-warnings']
        args = parse_arguments(command)
        self.assertTrue(args.suppress_warnings)
    
    def test_preview(self):
        command = ['main.py', 'file', '--preview']
        args = parse_arguments(command)
        self.assertTrue(args.preview)
