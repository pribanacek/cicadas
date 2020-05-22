import unittest

from src.parser.Parser import parse_string

class TestTopology(unittest.TestCase):

    def test_no_regions(self):
        program = 'f: A -> B'
        assembler = parse_string(program)
        assembler.get_graph()

        self.assertEqual(len(assembler.regions), 0)

    def test_single_regions(self):
        program = 'f: A -> B\nf = f'
        assembler = parse_string(program)
        assembler.get_graph()

        self.assertEqual(len(assembler.regions), 1)

    def test_nodes_with_no_regions(self):
        program = 'f: A -> B'
        assembler = parse_string(program)
        graph = assembler.get_graph()

        self.assertEqual(len(graph.graph), 2)

    def test_multiple_equivalent_regions(self):
        program = 'f: A -> B\nf = f\nf = f'
        assembler = parse_string(program)
        graph = assembler.get_graph()

        self.assertEqual(len(graph.graph), 2)
    
    def test_node_merging(self):
        program = 'f: A -> B\ng: B -> C'
        assembler = parse_string(program)
        graph = assembler.get_graph()

        self.assertEqual(len(graph.graph), 3)
    
    def test_region_merging(self):
        program = 'f: A -> B\ng: B -> C\nh: A -> C\ng . f = h'
        assembler = parse_string(program)
        graph = assembler.get_graph()

        self.assertEqual(len(graph.regions), 1)
        self.assertEqual(len(graph.graph), 3)

    def test_equivalent_region_merging(self):
        program = 'f: A -> B\ng: B -> C\nh: A -> C\ng . f = h\ng . f = h'
        assembler = parse_string(program)
        graph = assembler.get_graph()

        self.assertEqual(len(graph.regions), 2)
        self.assertEqual(len(graph.graph), 3)
    
    def test_additive_region_merging(self):
        program = 'f: A -> B\ng: B -> A\ng . f = g . f\ng . f = g . f\ng . f = g . f'
        assembler = parse_string(program)
        graph = assembler.get_graph()

        self.assertEqual(len(graph.regions), 3)
        self.assertEqual(len(graph.graph), 6)
