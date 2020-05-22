import unittest

import src.parser.Parser as Parser
from src.util.Exceptions import SyntaxException

def get_node_labels(assembler):
    return list(map(lambda x : x.label.text, assembler.nodes.values()))

def get_edge_labels(assembler):
    return list(map(lambda x : x.label.text, assembler.edges.values()))

def get_edge_styles(assembler):
    return list(map(lambda x : x.get_styles(), assembler.edges.values()))

class TestParsing(unittest.TestCase):

    def test_syntax_error_raised(self):
        program = 'f: A - B'
        with self.assertRaises(SyntaxException):
            Parser.parse_string(program)

    def test_default_labels(self):
        program = 'f: A -> B'
        assembler = Parser.parse_string(program)
        node_labels = get_node_labels(assembler)
        edge_labels = get_edge_labels(assembler)

        self.assertCountEqual(node_labels, ['$A$', '$B$'])
        self.assertCountEqual(edge_labels, ['$f$'])

    def test_inline_labels(self):
        program = 'f: A[foo] -> B'
        assembler = Parser.parse_string(program)
        node_labels = get_node_labels(assembler)
        edge_labels = get_edge_labels(assembler)

        self.assertCountEqual(node_labels, ['foo', '$B$'])
        self.assertCountEqual(edge_labels, ['$f$'])
    
    def test_label_declaration(self):
        program = 'f: A -> B\nlabel A : [foo]\nlabel f : [$bar$]'
        assembler = Parser.parse_string(program)
        node_labels = get_node_labels(assembler)
        edge_labels = get_edge_labels(assembler)

        self.assertCountEqual(node_labels, ['foo', '$B$'])
        self.assertCountEqual(edge_labels, ['$bar$'])

    def test_inline_styles(self):
        program = 'f: A -> B (k)'
        assembler = Parser.parse_string(program)
        edge_styles = get_edge_styles(assembler)[0]

        self.assertCountEqual(edge_styles, ['k'])
    
    def test_style_declaration(self):
        program = 'f: A -> B\n style f : (hook)'
        assembler = Parser.parse_string(program)
        edge_styles = get_edge_styles(assembler)[0]

        self.assertCountEqual(edge_styles, ['hook'])

    def test_padding_newlines(self):
        program = '\n\nf: A -> B\n\n\ng: C -> D\n'
        assembler = Parser.parse_string(program)
        node_labels = get_node_labels(assembler)
        edge_labels = get_edge_labels(assembler)

        self.assertEqual(len(node_labels), 4)
        self.assertEqual(len(edge_labels), 2)
    
    def test_padding_whitespace(self):
        program = '      f:  A ->     B \ng:C->          D '
        assembler = Parser.parse_string(program)
        node_labels = get_node_labels(assembler)
        edge_labels = get_edge_labels(assembler)

        self.assertEqual(len(node_labels), 4)
        self.assertEqual(len(edge_labels), 2)
    
    def test_whitespace_between_newlines(self):
        program = 'f: A -> B\n\n    \n\n  \ng:C -> D'
        assembler = Parser.parse_string(program)
        node_labels = get_node_labels(assembler)
        edge_labels = get_edge_labels(assembler)

        self.assertEqual(len(node_labels), 4)
        self.assertEqual(len(edge_labels), 2)
