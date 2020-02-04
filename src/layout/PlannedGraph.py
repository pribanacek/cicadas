import random, math, copy, numpy as np
import networkx as nx

class Vertex:
    def __init__(self, nodeId, label = None):
        self.nodeId = nodeId
        self.label = label
        self.dimensions = (0, 0)
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

def ccw(A, B, C):
    (Ax, Ay) = A
    (Bx, By) = B
    (Cx, Cy) = C
    return (Cy - Ay) * (Bx - Ax) > (By - Ay) * (Cx - Ax)

def intersect(A, B, C, D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


def nodesSortedByAngles(nodes, centre):
    angles = list(map(lambda x : (x, math.degrees(math.atan2(x.y - centre.y, x.x - centre.x))), nodes))
    return sorted(angles, key=lambda x : x[1])

class PlannedGraph:
    def __init__(self, graph):
        self.graph = graph
        self.nodeData = graph.nodes.data('data')
        self.nodePositions = graph.nodes.data('pos')
        self.edgeData = graph.edges(data = 'data', keys = True)
        self.angleValues = []
        
    def getPositions(self):
        return dict(self.nodePositions)
    
    def setNodePosition(self, nodeId, position, graph = None):
        graph = graph if graph != None else self.graph
        graph.nodes[nodeId]['pos'] = position
    
    def randomPlan(self, dimensions):
        (width, height) = dimensions
        for nodeId, _ in self.nodeData:
            x = round(width * (random.random() - 0.5))
            y = round(height * (random.random() - 0.5))
            self.setNodePosition(nodeId, (x, y))
        
    def randomNeighbour(self, radius):
        graph = self.graph.copy()
        nodeId = random.choice(list(graph.nodes))
        (x, y) = self.nodePositions[nodeId]
        dx = radius * (random.random() * 2 - 1)
        dy = radius * (random.random() * 2 - 1)
        newX = x + (dx if radius < 1 else round(dx))
        newY = y + (dy if radius < 1 else round(dy))
        self.setNodePosition(nodeId, (newX, newY), graph = graph)
        return PlannedGraph(graph)
    
    def recentreNodes(self):
        totalX = 0
        totalY = 0
        for nodeId, (x, y) in self.nodePositions:
            totalX += x
            totalY += y
        numberOfNodes = len(self.nodeData)
        offsetX = totalX / numberOfNodes
        offsetY = totalY / numberOfNodes
        for nodeId, (x, y) in self.nodePositions:
            newX = x - offsetX
            newY = y - offsetY
            self.setNodePosition(nodeId, (newX, newY))
    
    def energy(self, dimensions):
        A = 100 * self.nodeDistances()
        B = 10 * self.borderDistance(dimensions)
        C = 25 * self.edgeLengths()
        D = 1 * self.bondAngles()
        E = 50 * self.edgeDifferences()
        F = 1 * self.horizontalness()
        G = 30 * self.nodeEdgeDistances()
        H = 0 * self.angleDifferences()
        I = 740 * self.edgeIntersections()
        # print([A, B, C, D, E, F, G, H, I])
        energy = A + B + C + D + E + F + G + H + I
        return energy
    
    def avgNodePosition(self):
        xTotal = 0
        yTotal = 0
        for _, (x, y) in self.nodePositions:
            xTotal += x
            yTotal += y
        return xTotal ** 2 + yTotal ** 2
    
    def nodeDistanceSq(self, startId, endId):
        (startX, startY) = self.nodePositions[startId]
        (endX, endY) = self.nodePositions[endId]
        d2 = (startX - endX) ** 2 + (startY - endY) ** 2
        return d2
        
    def nodeDistances(self):
        A = 1 # change this for shorter edge lengths like \in labels
        total = 0
        nodeValues = list(self.getPositions().values())
        for i in range(len(nodeValues)):
            for j in range(i + 1, len(nodeValues)):
                (x1, y1) = nodeValues[i]
                (x2, y2) = nodeValues[j]
                d2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
                if d2 > 0:
                    total += A / d2
        return total
    
    def borderDistance(self, dimensions):
        (width, height) = dimensions
        positionValues = self.getPositions().values()
        (minX, _) = min(positionValues, key = lambda xy: xy[0])
        (maxX, _) = max(positionValues, key = lambda xy: xy[0])
        (_, minY) = min(positionValues, key = lambda xy: xy[1])
        (_, maxY) = max(positionValues, key = lambda xy: xy[1])
        graphWidth = maxX - minX
        graphHeight = maxY - minY
        if graphHeight >= height or graphWidth >= width:
            return math.inf
        dx2 = (width - graphWidth) ** 2
        dy2 = (height - graphHeight) ** 2
        return 1 / dx2 + 1 / dy2
    
    def edgeLengths(self):
        total = 0
        for (startId, endId, _, _) in self.edgeData:
            total += self.nodeDistanceSq(startId, endId) # some adjustment factor for individual edges
        return total

    def edgeDifferences(self):
        total = 0
        edges = list(self.edgeData)
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                (startA, endA, _, _) = edges[i]
                (startB, endB, _, _) = edges[j]
                length1 = self.nodeDistanceSq(startA, endA)
                length2 = self.nodeDistanceSq(startB, endB)
                total += abs(length1 - length2) # some adjustment factor for individual edges
        return total
    
    def nodeEdgeDistances(self):
        # if len(self.edgeData) == 0:
        #     return 0
        total = 0
        for nodeId, _ in self.nodeData:
            for (start, end, _, _) in self.edgeData:
                if nodeId != start and nodeId != end and start != end:
                    (p1x, p1y) = self.nodePositions[start]
                    (p2x, p2y) = self.nodePositions[end]
                    (nodeX, nodeY) = self.nodePositions[nodeId]
                    edgeLengthSq = self.nodeDistanceSq(start, end)
                    numerator = ((p2y - p1y) * nodeX - (p2x - p1x) * nodeY + p2x * p1y - p2y * p1x) ** 2
                    if numerator == 0 or edgeLengthSq == 0:
                        return 100
                    d2 = numerator / edgeLengthSq
                    total += 1 / d2
        return total

    def bondAngles(self):
        total = 0
        # goodAngles = (0, 30, 45, 60)
        # self.angleValues = []
        # for nodeId, node in self.nodeData.items():
        #     edges = list(self.graph.in_edges(nodeId, data=True)) + list(self.graph.out_edges(nodeId, data=True))
        #     neighbourNodeIds = list(map(lambda x : x[0] if x[0] != node else x[1], edges))
        #     neighbourNodes = list(map(lambda x : self.graph.nodes[x]['data'], neighbourNodeIds))
        #     sortedNeighbours = nodesSortedByAngles(neighbourNodes, node) # broken
        #     for i in range(len(sortedNeighbours) - 1):
        #         angle = sortedNeighbours[i + 1][1] - sortedNeighbours[i][1]
        #         self.angleValues.append(angle)
        #         angleRatings = list(map(lambda target : np.exp(abs((angle % 90) - target)), goodAngles))
        #         total += min(angleRatings)
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
        for (start, end, _, _) in self.edgeData:
            (startX, startY) = self.nodePositions[start]
            (endX, endY) = self.nodePositions[end]
            xDiff = abs(startX - endX)
            yDiff = abs(startY - endY)
            diff = min(xDiff, yDiff)
            measure = np.exp(100 * diff)
            rating = min(rating, measure)
        return rating
    
    def edgeIntersections(self):
        total = 0
        edges = list(self.edgeData)
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                (startA, endA, _, _) = edges[i]
                (startB, endB, _, _) = edges[j]
                startAPos = self.nodePositions[startA]
                startBPos = self.nodePositions[startB]
                endAPos = self.nodePositions[endA]
                endBPos = self.nodePositions[endB]
                if intersect(startAPos, endAPos, startBPos, endBPos):
                    total += 1
        return total