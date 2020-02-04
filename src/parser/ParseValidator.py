from src.plan.GraphAssembler import MergeAssembler
from src.layout.PlannedGraph import Vertex, Edge
from .PathFacts import PathFacts


class ParseValidator:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.compositions = {}
        self.pathFacts = PathFacts()

    def addEdge(self, edgeId, nodeAId, nodeBId):
        nodeA = Vertex(nodeAId)
        nodeB = Vertex(nodeBId)
        edge = Edge(edgeId, nodeA, nodeB)
        self.nodes[nodeAId] = nodeA
        self.nodes[nodeBId] = nodeB
        self.edges[edgeId] = edge

    def setLabel(self, objectId, label):
        if objectId in self.nodes:
            self.nodes[objectId].label = label
        if objectId in self.edges:
            self.edges[objectId].label = label
    
    def addStyles(self, edgeId, styleList):
        styles = self.edges[edgeId].styles
        self.edges[edgeId].styles = styles + styleList

    def validatePathContinuity(self, path):
        for i in range(len(path) - 1):
            edge1 = self.edges[path[i]]
            edge2 = self.edges[path[i + 1]]
            if edge1.end.nodeId != edge2.start.nodeId:
                return False
        return True
    
    def validatePathEnds(self, pathA, pathB):
        startNodeA = self.edges[pathA.edgeIds[0]].start.nodeId
        endNodeA = self.edges[pathA.edgeIds[-1]].end.nodeId
        startNodeB = self.edges[pathB.edgeIds[0]].start.nodeId
        endNodeB = self.edges[pathB.edgeIds[-1]].end.nodeId
        return startNodeA == startNodeB and endNodeA == endNodeB
    
    def validateNoIdsInPaths(self, pathA, pathB):
        return not str(pathA) in str(pathB) and not str(pathB) in str(pathA)
    
    def validatePaths(self, pathA, pathB):
        if not self.validatePathContinuity(pathA.edgeIds):
            raise Exception("The declared path " + str(pathA) + " is not a valid path, as it isn't continuous")
        if not self.validatePathContinuity(pathB.edgeIds):
            raise Exception("The declared path " + str(pathB) + " is not a valid path, as it isn't continuous")
        if not self.validatePathEnds(pathA, pathB):
            raise Exception("The declared paths " + str(pathA) + " and " + str(pathB) + " do not share a start/end node")
        # if not self.validateNoIdsInPaths(pathA, pathB):
        #     raise Exception(str(pathA) + " = " + str(pathB) + " : no identities allowed in path equalities")

    def addCompositions(self, pathA, pathB):
        self.validatePaths(pathA, pathB)
        self.pathFacts.addFact(pathA, pathB)

    def getGraphAssembler(self):
        return MergeAssembler(self.nodes, self.edges, self.pathFacts)
