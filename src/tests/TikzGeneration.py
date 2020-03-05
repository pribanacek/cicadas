import sys

# from src.layout.PlannedGraph import PlannedGraph, PositionedVertex
from src.layout.PlannedGraph import Edge
from src.output.TikzGen import generate_tikz

# def TestA():
#     A = PositionedVertex('A', -1, 1)
#     B = PositionedVertex('B', 1, 1)
#     C = PositionedVertex('C', -1, -1)
#     f = Edge('f', A, B)
#     g = Edge('g', B, C)
#     h = Edge('h', A, C)
#     graph = PlannedGraph([A, B, C], [f, g, h])
#     print('energy:', graph.energy((4, 4)))
#     return generate_tikz(graph)

# def TestB():
#     A = PositionedVertex('A', -1, 1)
#     B = PositionedVertex('B', 1, 1)
#     C = PositionedVertex('C', 1, -1)
#     D = PositionedVertex('D', -1, -1)
#     f = Edge('f', A, B)
#     g = Edge('g', B, C)
#     h = Edge('h', A, D)
#     k = Edge('k', D, C)
#     graph = PlannedGraph([A, B, C, D], [f, g, h, k])
#     print('energy:', graph.energy((4, 4)))
#     return generate_tikz(graph)


# def TestC():
#     A = PositionedVertex('A', -1, 1)
#     B = PositionedVertex('B', 1, 1)
#     C = PositionedVertex('C', 1, -1)
#     D = PositionedVertex('D', -1, -1)
#     E = PositionedVertex('E', 2.5, 2.5)
#     f = Edge('f', A, B)
#     g = Edge('g', B, C)
#     h = Edge('h', A, D)
#     k = Edge('k', D, C)
#     l = Edge('l', A, E)
#     m = Edge('m', B, E)
#     n = Edge('n', C, E)
#     graph = PlannedGraph([A, B, C, D, E], [f, g, h, k, l, m, n])
#     print('energy:', graph.energy((8, 8)))
#     return generate_tikz(graph)
