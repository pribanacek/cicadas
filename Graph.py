import networkx as nx

class Vertex:
    def __init__(self, identifier, label = None):
        self.identifier = identifier
        self.label = label
        if self.label == None:
            self.label = self.identifier

class Edge:
    def __init__(self, identifier, start, end, label = None):
        self.identifier = identifier
        self.start = start
        self.end = end
        self.label = label
        if self.label == None:
            self.label = self.identifier


class Graph:
    def __init__(self, nodes, edges):
        self.graph = nx.DiGraph() # create directed graph
        self.graph.add_nodes_from(nodes)
        self.graph.add_edges_from(edges)
