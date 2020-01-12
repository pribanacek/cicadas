from src.plan.Graph import Graph, Vertex, Edge

EDGE = 'edge'
NODE = 'node'

class GraphAssembler:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.compositions = {}

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
    
    def addStyle(self, edgeId, style):
        self.edges[edgeId].styles.append(style)

    def validatePath(self, path):
        for i in range(len(path) - 1):
            edge1 = self.edges[path[i]]
            edge2 = self.edges[path[i + 1]]
            if edge1.start.nodeId != edge2.end.nodeId:
                return False
        return True
    
    def validatePaths(self, pathA, pathB):
        if not self.validatePath(pathA.edgeIds):
            raise Exception("The declared path " + pathA.text + " is not a valid path")
        elif not self.validatePath(pathB.edgeIds):
            raise Exception("The declared path " + pathB.text + " is not a valid path")
        else:
            startNodeA = self.edges[pathA.edgeIds[-1]].start.nodeId
            endNodeA = self.edges[pathA.edgeIds[0]].end.nodeId
            startNodeB = self.edges[pathB.edgeIds[-1]].start.nodeId
            endNodeB = self.edges[pathB.edgeIds[0]].end.nodeId
            if startNodeA != startNodeB:
                raise Exception("The declared paths " + pathB.text + " do not share a start node so cannot be equal")
            if endNodeA != endNodeB:
                raise Exception("The declared paths " + pathB.text + " do not share an end node so cannot be equal")

    def addCompositions(self, pathA, pathB):
        self.validatePaths(pathA, pathB)

    def getGraph(self):
        nodes = list(self.nodes.values())
        edges = list(self.edges.values())
        return Graph(nodes, edges)