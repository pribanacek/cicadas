import unittest

from src.parser.DiagramObjects import Morphism
from src.parser.EdgeStyles import EdgeStyle
from src.output.TikzGenerator import get_edge_string, get_node_string, get_styles_string

class TestOutput(unittest.TestCase):

    def test_style_string_generation(self):
        styles = ['a', 'b', 'c']
        style_string = get_styles_string(styles)
        self.assertEqual(style_string, '[commutative diagrams/a,commutative diagrams/b,commutative diagrams/c]')

    def test_style_string_single(self):
        styles = ['a']
        style_string = get_styles_string(styles)
        self.assertEqual(style_string, '[commutative diagrams/a]')

    def test_style_string_none(self):
        styles = []
        style_string = get_styles_string(styles)
        self.assertEqual(style_string, '')

    def test_node_string_generation(self):
        node_id = 'node_id'
        label = '$label$'
        position = (3, 4)

        node_string = get_node_string(node_id, label, position)

        self.assertEqual(node_string, '\\node (node_id) at (3, 4) {$label$};')

    def test_node_string_no_label(self):
        node_id = 'node_id'
        label = ''
        position = (3, 4)

        node_string = get_node_string(node_id, label, position)

        self.assertEqual(node_string, '\\node (node_id) at (3, 4) {};')
    

    def test_edge_string_generation(self):
        start = 'A'
        end = 'B'
        edge = Morphism('f', None, None)

        edge_string = get_edge_string(start, end, edge)

        self.assertEqual(edge_string, '(A) edge node {$f$} (B)')
    
    def test_edge_string_styles(self):
        start = 'A'
        end = 'B'
        styles = [EdgeStyle('a'), EdgeStyle('b')]
        edge = Morphism('f', None, None, styles = styles)

        edge_string = get_edge_string(start, end, edge)

        self.assertEqual(edge_string, '(A) edge[commutative diagrams/a,commutative diagrams/b] node {$f$} (B)')
