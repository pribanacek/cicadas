import sys

from PlannedGraph import PlannedGraph, PositionedVertex
from Graph import Edge
from TikzGen import generateTikz

def TestTikzA():
    A = PositionedVertex('A', -1, 1)
    B = PositionedVertex('B', 1, 1)
    C = PositionedVertex('C', -1, -1)
    f = Edge('f', A, B)
    g = Edge('g', B, C)
    h = Edge('h', A, C)
    graph = PlannedGraph([A, B, C], [f, g, h])
    return generateTikz(graph)

def TestTikzB():
    A = PositionedVertex('A', -1, 1)
    B = PositionedVertex('B', 1, 1)
    C = PositionedVertex('C', 1, -1)
    D = PositionedVertex('D', -1, -1)
    f = Edge('f', A, B)
    g = Edge('g', B, C)
    h = Edge('h', A, D)
    k = Edge('k', D, C)
    graph = PlannedGraph([A, B, C, D], [f, g, h, k])
    return generateTikz(graph)


def TestTikzC():
    A = PositionedVertex('A', -1, 1)
    B = PositionedVertex('B', 1, 1)
    C = PositionedVertex('C', 1, -1)
    D = PositionedVertex('D', -1, -1)
    E = PositionedVertex('E', 2.5, 2.5)
    f = Edge('f', A, B)
    g = Edge('g', B, C)
    h = Edge('h', A, D)
    k = Edge('k', D, C)
    l = Edge('l', A, E)
    m = Edge('m', B, E)
    n = Edge('n', C, E)
    graph = PlannedGraph([A, B, C, D, E], [f, g, h, k, l, m, n])
    return generateTikz(graph)


TESTS = {
    'A': TestTikzA,
    'B': TestTikzB,
    'C': TestTikzC,
}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please specify a test')
    
    test = sys.argv[1]
    if test in TESTS:
        print(TESTS[test]())
    else:
        print('Unknown test ' + test)
