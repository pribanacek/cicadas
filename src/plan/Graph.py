import networkx as nx
import math, random
from src.layout.PlannedGraph import PlannedGraph, PositionedVertex

def randomly(sequence):
    shuffled = list(sequence)
    random.shuffle(shuffled)
    return iter(shuffled)

class Vertex:
    def __init__(self, nodeId, label = None):
        self.nodeId = nodeId
        self.label = label
        self.labelBBox = (0, 0)
        if self.label == None:
            self.label = '$' + self.nodeId + '$'

class Edge:
    def __init__(self, edgeId, start, end, label = None, styles = None):
        self.edgeId = edgeId
        self.start = start
        self.end = end
        self.label = label
        if self.label == None:
            self.label = '$' + self.edgeId + '$'
        self.styles = [] if styles == None else styles


class Graph:
    def __init__(self, nodes, edges):
        self.nodeData = nodes
        self.edgeData = edges
        self.validateInput()

        self.graph = nx.DiGraph()
        nodeIds = list(map(lambda x : (x.nodeId, dict(data=x)), nodes))
        edgeIds = list(map(lambda x : (x.start.nodeId, x.end.nodeId, dict(data=x)), edges))
        self.graph.add_nodes_from(nodeIds)
        self.graph.add_edges_from(edgeIds)
    
    def validateInput(self):
        nodeIds = {}
        for node in self.nodeData:
            if node.nodeId in nodeIds:
                raise Exception('Node ID collision \'' + node.nodeId + '\'')
            nodeIds[node.nodeId] = True
        
        for edge in self.edgeData:
            if not edge.start.nodeId in nodeIds:
                raise Exception('Edge connected to invalid node \'' + edge.start.nodeId + '\'')
            if not edge.end.nodeId in nodeIds:
                raise Exception('Edge connected to invalid node \'' + edge.end.nodeId + '\'')
            
    def superRandomPlan(self, dimensions):
        (width, height) = dimensions
        nodes = []
        for node in self.nodeData:
            x = width * (random.random() - 0.5)
            y = height * (random.random() - 0.5)
            nodes.append(PositionedVertex(node.nodeId, x, y, node.label))
        return PlannedGraph(nodes, self.edgeData)
    
    def randomPlan(self, dimensions):
        (width, _height) = dimensions
        nodes = []
        n = len(self.nodeData)
        angle = 0
        magnitude = width / 4 # TODO deal with rectangular dimensions
        for i in randomly(range(n)):
            node = self.nodeData[i]
            x = magnitude * math.cos(angle)
            y = magnitude * math.sin(angle)
            nodes.append(PositionedVertex(node.nodeId, x, y, node.label))
            angle += 2 * math.pi / n
        return PlannedGraph(nodes, self.edgeData)