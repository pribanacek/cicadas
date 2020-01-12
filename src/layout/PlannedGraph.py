import random, math, copy, numpy as np
import networkx as nx

def ccw(A, B, C):
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)

def intersect(A, B, C, D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


def nodesSortedByAngles(nodes, centre):
    angles = list(map(lambda x : (x, math.degrees(math.atan2(x.y - centre.y, x.x - centre.x))), nodes))
    return sorted(angles, key=lambda x : x[1])

class PositionedVertex:
    def __init__(self, nodeId, x, y, label = None):
        self.nodeId = nodeId
        self.x = x
        self.y = y
        self.label = label
        self.labelBBox = (0, 0)
        if self.label == None:
            self.label = self.nodeId
    
    def copy(self):
        return PositionedVertex(self.nodeId, self.x, self.y, self.label)

class PlannedGraph:
    def __init__(self, nodes, edges):
        self.nodeData = nodes
        self.edgeData = edges
        self.graph = nx.DiGraph() # create directed graph
        nodeIds = list(map(lambda x : (x.nodeId, dict(data=x)), nodes))
        edgeIds = list(map(lambda x : (x.start.nodeId, x.end.nodeId, dict(data=x)), edges))
        self.graph.add_nodes_from(nodeIds)
        self.graph.add_edges_from(edgeIds)
        self.angleValues = []
        
    def randomNeighbour(self, radius):
        nxGraph = copy.deepcopy(self.graph)
        node = random.choice(list(nxGraph.nodes))
        angle = random.random() * math.pi
        x = nxGraph.nodes[node]['data'].x
        y = nxGraph.nodes[node]['data'].y
        nxGraph.nodes[node]['data'].x = x + radius * math.cos(angle)
        nxGraph.nodes[node]['data'].y = y + radius * math.sin(angle)
        nodesList = list(map(lambda x : x[1], list(nxGraph.nodes.data('data'))))
        edgesList = list(map(lambda x : x[2], list(nxGraph.edges.data('data'))))
        return PlannedGraph(nodesList, edgesList)
    
    def recentreNodes(self):
        totalX = 0
        totalY = 0
        for node in self.nodeData:
            totalX += node.x
            totalY += node.y
        numberOfNodes = len(self.nodeData)
        offsetX = totalX / numberOfNodes
        offsetY = totalY / numberOfNodes
        for node in self.nodeData:
            node.x -= offsetX
            node.y -= offsetY
    
    def energy(self, dimensions):
        A = 100 * self.nodeDistances()
        B = 10 * self.borderDistance(dimensions)
        C = 25 * self.edgeLengths()
        D = 1 * self.bondAngles()
        E = 50 * self.edgeDifferences()
        F = 1 * self.horizontalness()
        G = 30 * self.nodeEdgeDistances()
        H = 10 * self.angleDifferences()
        I = 740 * self.edgeIntersections()
        # print([A, B, C, D, E, F, G, H])
        energy = A + B + C + D + E + F + G + H + I
        return energy
    
    def avgNodePosition(self):
        xTotal = 0
        yTotal = 0
        for node in self.nodeData:
            xTotal += node.x
            yTotal += node.y
        return xTotal ** 2 + yTotal ** 2
    
    def edgeNodes(self, edge):
        start = self.graph.nodes[edge.start.nodeId]['data']
        end = self.graph.nodes[edge.end.nodeId]['data']
        return (start, end)

    def edgeLengthSq(self, edge):
        (start, end) = self.edgeNodes(edge)
        d2 = (start.x - end.x) ** 2 + (start.y - end.y) ** 2
        return d2
        
    def nodeDistances(self):
        A = 1 # change this for shorter edge lengths like \in labels
        total = 0
        for i in range(len(self.nodeData)):
            for j in range(i, len(self.nodeData)):
                node1 = self.nodeData[i]
                node2 = self.nodeData[j]
                d2 = node1.x ** 2 + node2.y ** 2
                if d2 > 0:
                    total += A / d2
        return total
    
    def borderDistance(self, dimensions):
        (width, height) = dimensions
        minX = min(self.nodeData, key = lambda node : node.x)
        maxX = max(self.nodeData, key = lambda node : node.x)
        minY = min(self.nodeData, key = lambda node : node.y)
        maxY = max(self.nodeData, key = lambda node : node.y)
        graphWidth = maxX.x - minX.x
        graphHeight = maxY.y - minY.y
        if graphHeight >= height or graphWidth >= width:
            return math.inf
        dx2 = (width - graphWidth) ** 2
        dy2 = (height - graphHeight) ** 2
        return 1 / dx2 + 1 / dy2
    
    def edgeLengths(self):
        total = 0
        for edge in self.edgeData:
            total += self.edgeLengthSq(edge) # some adjustment factor for individual edges
        return total

    def edgeDifferences(self):
        numOfEdges = len(self.edgeData)
        total = 0
        for i in range(numOfEdges):
            for j in range(i + 1, numOfEdges):
                length1 = self.edgeLengthSq(self.edgeData[i])
                length2 = self.edgeLengthSq(self.edgeData[j])
                total += abs(length1 - length2) # some adjustment factor for individual edges
        return total
    
    def nodeEdgeDistances(self):
        # if len(self.edgeData) == 0:
        #     return 0
        total = 0
        for node in self.nodeData:
            for edge in self.edgeData:
                (p1, p2) = self.edgeNodes(edge)
                if node != p1 and node != p2 and p1 != p2:
                    edgeLengthSq = (p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2
                    numerator = ((p2.y - p1.y) * node.x - (p2.x - p1.x) * node.y + p2.x * p1.y - p2.y * p1.x) ** 2
                    d2 = numerator / edgeLengthSq
                    total += 1 / d2
        return total

    def bondAngles(self):
        goodAngles = (0, 30, 45, 60)
        total = 0
        self.angleValues = []
        for node in self.nodeData:
            nodeId = node.nodeId
            edges = list(self.graph.in_edges(nodeId, data=True)) + list(self.graph.out_edges(nodeId, data=True))
            neighbourNodeIds = list(map(lambda x : x[0] if x[0] != node else x[1], edges))
            neighbourNodes = list(map(lambda x : self.graph.nodes[x]['data'], neighbourNodeIds))
            sortedNeighbours = nodesSortedByAngles(neighbourNodes, node)
            for i in range(len(sortedNeighbours) - 1):
                angle = sortedNeighbours[i + 1][1] - sortedNeighbours[i][1]
                self.angleValues.append(angle)
                angleRatings = list(map(lambda target : np.exp(abs((angle % 90) - target)), goodAngles))
                total += min(angleRatings)
        return total
    
    def angleDifferences(self):
        n = len(self.angleValues)
        total = 0
        for i in range(n):
            for j in range(i + 1, n):
                a1 = self.angleValues[i] % 90
                a2 = self.angleValues[j] % 90
                total += abs(a1 - a2) # some adjustment factor for individual edges
        return total

    def horizontalness(self):
        rating = math.inf
        for edge in self.edgeData:
            (start, end) = self.edgeNodes(edge)
            xDiff = abs(start.x - end.x)
            yDiff = abs(start.y - end.y)
            diff = min(xDiff, yDiff)
            measure = np.exp(100 * diff)
            rating = min(rating, measure)
        return rating
    
    def edgeIntersections(self):
        n = len(self.edgeData)
        total = 0
        for i in range(n):
            for j in range(i + 1, n):
                (startA, endA) = self.edgeNodes(self.edgeData[i])
                (startB, endB) = self.edgeNodes(self.edgeData[j])
                if intersect(startA, endA, startB, endB):
                    total += 1
        return total