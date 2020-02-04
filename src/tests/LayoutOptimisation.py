import sys, os, webbrowser

# from src.plan.Graph import Graph, Edge, Vertex
from src.output.TikzGen import generateTikz
from src.layout.LayoutOptimizer import optimizeLayout
from src.output.AutoRender import generatePDF

# def TestA():
#     A = Vertex('A')
#     B = Vertex('B')
#     C = Vertex('C')
#     f = Edge('f', A, B)
#     g = Edge('g', B, C)
#     h = Edge('h', A, C)
#     graph = Graph([A, B, C], [f, g, h])
#     return generateTikz(optimizeLayout(graph))

# def TestB():
#     A1 = Vertex('A1', 'A')
#     B = Vertex('B')
#     A2 = Vertex('A2', 'A')
#     f = Edge('f', A1, B)
#     g = Edge('g', B, A2)
#     h = Edge('id_A', A1, A2)
#     graph = Graph([A1, A2, B], [f, g, h])
#     return generateTikz(optimizeLayout(graph))

# def TestC():
#     A = Vertex('A')
#     B = Vertex('B')
#     C = Vertex('C')
#     D = Vertex('D')
#     f = Edge('f', A, B)
#     g = Edge('g', B, C)
#     h = Edge('h', A, D)
#     k = Edge('k', D, C)
#     graph = Graph([A, B, C, D], [f, g, h, k])
#     return generateTikz(optimizeLayout(graph))

# def TestD():
#     A = Vertex('A')
#     B = Vertex('B')
#     f = Edge('f', A, B)
#     g = Edge('g', B, A)
#     h = Edge('id_A', A, A)
#     k = Edge('id_B', B, B)
#     graph = Graph([A, B], [f, g, h, k])
#     return generateTikz(optimizeLayout(graph))

# def TestE():
#     A = Vertex('A')
#     B = Vertex('B')
#     C = Vertex('C')
#     D = Vertex('D')
#     E = Vertex('E')
#     f = Edge('f', A, B)
#     g = Edge('g', B, C)
#     h = Edge('h', A, D)
#     k = Edge('k', D, C)
#     l = Edge('l', A, E)
#     m = Edge('m', B, E)
#     n = Edge('n', C, E)
#     graph = Graph([A, B, C, D, E], [f, g, h, k, l, m, n])
#     return generateTikz(optimizeLayout(graph))

# def TestF():
#     T = Vertex('T')
#     XY = Vertex('XY', 'X \\times_Z Y')
#     X = Vertex('X')
#     Y = Vertex('Y')
#     Z = Vertex('Z')
#     xy = Edge('(x,y)', T, XY)
#     x = Edge('x', T, X)
#     y = Edge('y', T, Y)
#     p = Edge('p', XY, X)
#     q = Edge('q', XY, Y)
#     f = Edge('f', X, Z)
#     g = Edge('g', Y, Z)
#     graph = Graph([T, XY, X, Y, Z], [xy, x, y, p, q, f, g])
#     return generateTikz(optimizeLayout(graph))

# def TestG():
#     A = Vertex('A', '\\cdots C_{i-1}')
#     B = Vertex('B', 'C_i')
#     C = Vertex('C', 'C_{i+1}')
#     D = Vertex('D', '\\cdots D_{i-1}')
#     E = Vertex('E', 'D_i')
#     F = Vertex('F', 'D_{i+1} \\cdots')
#     a = Edge('\\delta_{C_{i-1}}', A, B)
#     b = Edge('\\delta_{C_i}', B, C)
#     c = Edge('\\delta_{D_{i-1}}', D, E)
#     d = Edge('\\delta_{D_{i-1}}', E, F)
#     e = Edge('\\alpha_{i-1}', A, D)
#     f = Edge('\\alpha_i', B, E)
#     g = Edge('\\alpha{i+1}', C, F)
#     graph = Graph([A, B, C, D, E, F], [a, b, c, d, e, f, g])
#     return generateTikz(optimizeLayout(graph))

# def TestH():
#     A = Vertex('A')
#     B = Vertex('B')
#     C = Vertex('C')
#     D = Vertex('D')
#     f = Edge('f', A, B)
#     g = Edge('g', B, C)
#     h = Edge('h', C, D)
#     a1 = Edge('a', A, C, 'g \\circ f')
#     a2 = Edge('a', A, D, 'h \\circ (g \\circ f)')
#     a3 = Edge('a', A, D, '(h \\circ g) \\circ f')
#     b = Edge('b', B, D, 'h \\circ g')
#     graph = Graph([A, B, C, D], [f, g, h, a1, a2, a3, b])
#     return generateTikz(optimizeLayout(graph))

# def TestI():
#     A = Vertex('A', '((A \\otimes B) \\otimes C) \\otimes D')
#     B = Vertex('B', '(A \\otimes (B \\otimes C)) \\otimes D')
#     C = Vertex('C', 'A \\otimes ((B \\otimes C) \\otimes D)')
#     D = Vertex('D', 'A \\otimes (B \\otimes (C \\otimes D))')
#     E = Vertex('E', '(A \\otimes B) \\otimes (C \\otimes D)')
#     f = Edge('f', A, B, '\\alpha_{A,B,C} \\otimes 1_D')
#     g = Edge('g', B, C, '\\alpha_{A,B \\otimes C,D}')
#     h = Edge('h', C, D, '1_A \\otimes \\alpha_{B,C,D}')
#     i = Edge('i', A, E, '\\alpha_{A \\otimes B,C,D}')
#     j = Edge('j', E, D, '\\alpha_{A,B,C \\otimes D}')
#     graph = Graph([A, B, C, D, E], [f, g, h, i, j])
#     return generateTikz(optimizeLayout(graph))

# def TestJ():
#     A = Vertex('A', 'X \\otimes (Y \\otimes (Z \\otimes T))')
#     B = Vertex('B', '(X \\otimes Y) \\otimes (Z \\otimes T)')
#     C = Vertex('C', '((X \\otimes Y) \\otimes Z) \\otimes T')
#     D = Vertex('D', 'X \\otimes ((Y \\otimes Z) \\otimes T)')
#     E = Vertex('E', '(X \\otimes (Y \\otimes Z)) \\otimes T')
#     f = Edge('f', A, B, '\\phi')
#     g = Edge('g', B, C, '\\phi')
#     h = Edge('h', C, D, '1 \\otimes \\phi')
#     i = Edge('i', A, E, '\\phi')
#     j = Edge('j', E, D, '\\phi \\otimes 1')
#     graph = Graph([A, B, C, D, E], [f, g, h, i, j])
#     return generateTikz(optimizeLayout(graph))

# def TestK():
#     return None #subsets edges

# def TestL():
#     return None #subsets edges

# def TestM():
#     A = Vertex('A', 'X \\otimes (Y \\otimes (Z \\otimes T))')
#     B = Vertex('B', '(X \\otimes Y) \\otimes (Z \\otimes T)')
#     C = Vertex('C', '((X \\otimes Y) \\otimes Z) \\otimes T')
#     D = Vertex('D', 'X \\otimes ((Y \\otimes Z) \\otimes T)')
#     E = Vertex('E', '(X \\otimes (Y \\otimes Z)) \\otimes T')
#     f = Edge('f', A, B, '\\phi')
#     g = Edge('g', B, C, '\\phi')
#     h = Edge('h', C, D, '1 \\otimes \\phi')
#     i = Edge('i', A, E, '\\phi')
#     j = Edge('j', E, D, '\\phi \\otimes 1')
#     graph = Graph([A, B, C, D, E], [f, g, h, i, j])
#     return generateTikz(optimizeLayout(graph))
