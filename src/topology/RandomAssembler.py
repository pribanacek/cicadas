import networkx as nx
from src.layout.PlannedGraph import PlannedGraph
from src.parser.PathFact import PathFact
from .GraphAssembler import GraphAssembler


def trimPaths(pathA, pathB):
    i = 0
    j = 0
    while pathA[i] == pathB[i]:
        i += 1
    while pathA[-j - 1] == pathB[-j - 1]:
        j += 1
    newPathA = pathA[i : len(pathA) - j]
    newPathB = pathA[i : len(pathB) - j]
    return (newPathA, newPathB)

def validPathPair(pathA, pathB):
    visited = {
        pathA[0][0]: True, # start node
        pathA[-1][0]: True # end node
    }
    for _, end, _ in pathA[1:-1]:
        if end in visited:
            return False
        visited[end] = True
    for _, end, _ in pathB[1:-1]:
        if end in visited:
            return False
        visited[end] = True
    return True


def allValidPathPairs(pathList):
    pairs = set()
    for i in range(len(pathList)):
        for j in range(i + 1, len(pathList)):
            (pathA, pathB) = trimPaths(pathList[i], pathList[j])
            if validPathPair(pathA, pathB):
                pathAEdges = tuple(map(lambda x : x[2], pathA))
                pathBEdges = tuple(map(lambda x : x[2], pathB))
                pair = PathFact(pathAEdges, pathBEdges)
                pairs.add(pair)
    return pairs

class RandomAssembler(GraphAssembler):
    def pathToEdgeList(self, nodeList):
        edges = []
        for i in range(len(nodeList) - 1):
            nodeA = nodeList[i]
            nodeB = nodeList[i + 1]
            edge_data = self.graph.get_edge_data(nodeA, nodeB)
            edgeIds = list(edge_data.keys())
            # TODO take care of potential multiple edges properly
            edgeId = edgeIds[0]
            data = (nodeA, nodeB, edgeId)
            edges.append(data)
        return edges
    
    def getCurrentRepresentedFacts(self):
        nodes = list(self.nodes.values())
        graph = self.currentGraph.graph
        factsPresent = set()
        for nodeA in nodes:
            for nodeB in nodes:
                if nodeA != nodeB:
                    allPaths = nx.all_simple_paths(graph, source = nodeA.nodeId, target = nodeB.nodeId)
                    pathList = list(map(self.edgeList, allPaths))
                    factsPresent |= allValidPathPairs(pathList)
        return factsPresent

    def isConsistent(self):
        facts = self.getCurrentRepresentedFacts()
        neededFacts = self.pathFacts.get_facts()
        extraFacts = facts - neededFacts
        missingFacts = neededFacts - facts
        print('extras', *extraFacts, sep='\n')
        print('missing', *missingFacts, sep='\n')
        # print('present', *facts, sep='\n')
        # print('required', *neededFacts, sep='\n')
        return len(extraFacts) == 0 and len(missingFacts) == 0

    def getGraph(self):
        if self.isConsistent():
            print('consistent')
        else:
            print('not consistent')
        return PlannedGraph(self.currentGraph, self.dimensions)