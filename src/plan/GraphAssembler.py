from src.layout.PlannedGraph import PlannedGraph
import networkx as nx

from difflib import SequenceMatcher
from collections import OrderedDict
import random

def LCS(str1, str2):
    seqMatch = SequenceMatcher(None, str1, str2)
    match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))
    if match.size != 0:
        return match
    return None

def get_node_id_mapping(sourceIds, targetIds, match):
    mapping = OrderedDict()
    for i in range(match.size):
        a = sourceIds[match.a + i]
        b = targetIds[match.b + i]
        mapping[a] = b
    return mapping


class GraphAssembler:
    def __init__(self, nodes, edges, pathFacts):
        self.nodes = nodes
        self.nodeCounts = {nodeId: 0 for nodeId in self.nodes}
        self.edges = edges
        self.edgeCounts = {edgeId: 0 for edgeId in self.edges}
        self.pathFacts = pathFacts
        self.graphCycles = {}
        self.graph = nx.MultiDiGraph()
    
    def addNodeCount(self, nodeId):
        self.nodeCounts[nodeId] += 1
    
    def addEdgeCount(self, edgeId):
        self.edgeCounts[edgeId] += 1
    
    def newGraphNodeId(self, nodeId):
        count = self.nodeCounts[nodeId]
        self.addNodeCount(nodeId)
        return nodeId + '-' + str(count)
    
    def addNodeInstance(self, nodeId, graph = None):
        graph = graph if graph != None else self.graph
        node = self.nodes[nodeId]
        graphNodeId = self.newGraphNodeId(nodeId)
        graph.add_node(graphNodeId, data = node, pos = (0, 0))
        return graphNodeId
    
    def addEdge(self, edgeId, start = None, end = None, graph = None):
        graph = graph if graph != None else self.graph
        edge = self.edges[edgeId]
        startNode = edge.start.nodeId
        endNode = edge.end.nodeId
        graphStartId = start if start != None else self.addNodeInstance(startNode, graph = graph)
        graphEndId = end if end != None else self.addNodeInstance(endNode, graph = graph)
        graph.add_edge(graphStartId, graphEndId, edgeId, data = edge)
        self.addEdgeCount(edgeId)
        return (graphStartId, graphEndId)
    
    def addPath(self, path, start = None, end = None, graph = None):
        graph = graph if graph != None else self.graph
        pathStartNode = self.edges[path.edgeIds[0]].start.nodeId
        pathEndNode = self.edges[path.edgeIds[-1]].end.nodeId
        pathStartGraphId = start if start != None else self.addNodeInstance(pathStartNode, graph = graph)
        pathEndGraphId = end if end != None else self.addNodeInstance(pathEndNode, graph = graph)
        pathIds = [pathStartGraphId]
        for i in range(len(path.edgeIds) - 1):
            edgeId = path.edgeIds[i]
            (_, edgeEndId) = self.addEdge(edgeId, start = pathIds[-1], graph = graph)
            pathIds.append(edgeEndId)
        self.addEdge(path.edgeIds[-1], start = pathIds[-1], end = pathEndGraphId, graph = graph)
        pathIds.append(pathEndGraphId)
        return pathIds
    
    def getGraph(self):
        return PlannedGraph(self.graph)

class MergeAssembler(GraphAssembler):   
    def createFactSubGraphs(self):
        subGraphs = []
        for fact in self.pathFacts.getFacts():
            (pathA, pathB) = fact.paths()
            graph = nx.MultiDiGraph()
            pathAIds = self.addPath(pathA, graph = graph)
            pathBIds = self.addPath(pathB, start = pathAIds[0], end = pathAIds[-1], graph = graph)
            data = (graph, pathAIds, pathBIds)
            subGraphs.append(data)
        return subGraphs
    
    def createRemainingSubGraphs(self):
        subGraphs = []
        for edgeId in self.edges:
            if self.edgeCounts[edgeId] < 1:
                graph = nx.MultiDiGraph()
                self.addEdge(edgeId, graph = graph)
                subGraphs.append(graph)
        return subGraphs
    
    def nodeIdsToLCSString(self, nodeIds, graph):
        node = graph.nodes[nodeIds[0]]['data']
        idString = [nodeIds[0]]
        nameString = [node.nodeId]
        for i in range(len(nodeIds) - 1):
            nodeAId = nodeIds[i]
            nodeBId = nodeIds[i + 1]
            edgeData = graph.get_edge_data(nodeAId, nodeBId)
            edgeId = list(dict(edgeData).keys())[0]
            nodeB = graph.nodes[nodeBId]['data']
            idString.append(edgeId)
            nameString.append(edgeId)
            idString.append(nodeBId)
            nameString.append(nodeB.nodeId)
        return (idString, nameString) ###
    
    def get_max_subgraph_mapping(self, graph, subGraph, pathAIds, pathBIds):
        cutoff = max(len(pathAIds), len(pathBIds))
        (stringAIds, stringANames) = self.nodeIdsToLCSString(pathAIds, subGraph)
        (stringBIds, stringBNames) = self.nodeIdsToLCSString(pathBIds, subGraph)
        mappings_A = []
        mappings_B = []
        for node in graph:
            targets = [x for x in graph if x != node]
            allPaths = nx.all_simple_paths(graph, source = node, target = targets, cutoff = cutoff)
            for path in allPaths:
                (pathStringIds, pathStringNames) = self.nodeIdsToLCSString(path, graph)
                matchA = LCS(stringANames, pathStringNames)
                matchB = LCS(stringBNames, pathStringNames)
                if matchA != None:
                    mapping = get_node_id_mapping(stringAIds, pathStringIds, matchA)
                    mappings_A.append(mapping)
                if matchB != None:
                    mapping = get_node_id_mapping(stringBIds, pathStringIds, matchB)
                    mappings_B.append(mapping)
        maximum_mapping = max(*mappings_A, *mappings_B, key = len)
        for mapA in mappings_A:
            for mapB in mappings_B:
                if self.is_mapping_compatible(mapA, mapB, pathAIds):
                    new_max = OrderedDict(list(mapA.items()) + list(mapB.items()))
                    if len(new_max) > len(maximum_mapping):
                        maximum_mapping = new_max
        return maximum_mapping
    
    def is_mapping_compatible(self, mapA, mapB, pathAIds):
        caiusA = set(mapA.keys())
        caiusB = set(mapB.keys())
        for k in caiusA.intersection(caiusB):
            if mapA[k] != mapB[k]:
                return False

        listA = list(mapA)
        listB = list(mapB)
        if listA[0] == pathAIds[0]:
            if len(listA) > 1 and len(listB) > 1 and listA[1] == listB[1]:
                # must take different routes initially
                return False
        elif listA[0] == listB[0]: # if it's not the path start node, that can't share a start node
            return False
        return True
    
    def mergeFactSubGraph(self, graph, subGraph, mapping):
        for nodeId in subGraph:
            mappedNodeId = nodeId if not nodeId in mapping else mapping[nodeId]
            if mappedNodeId not in graph:
                nodeData = subGraph.nodes[nodeId]
                graph.add_node(mappedNodeId, data = nodeData['data'], pos = nodeData['pos'])
        for start, end, edgeId, edgeData in subGraph.edges(keys = True, data = 'data'):
            mappedStart = start if not start in mapping else mapping[start]
            mappedEnd = end if not end in mapping else mapping[end]
            graph.add_edge(mappedStart, mappedEnd, edgeId, data = edgeData)
        return graph
    
    def mergeFactSubGraphs(self, graph, subGraphs):
        for (subGraph, pathAIds, pathBIds) in subGraphs:
            mapping = self.get_max_subgraph_mapping(graph, subGraph, pathAIds, pathBIds)
            self.mergeFactSubGraph(graph, subGraph, mapping)
    
    def get_random_node_instance(self, graph, node_name):
        nodes = [x for x, y in graph.nodes(data = 'data') if y.nodeId == node_name]
        return random.choice(nodes)

    def addUnusedEdges(self):
        for edgeId, count in self.edgeCounts.items():
            if count == 0:
                edge = self.edges[edgeId]
                startNodeName = edge.start.nodeId
                endNodeName = edge.end.nodeId
                startNodeId = None
                endNodeId = None
                if self.nodeCounts[startNodeName] > 0:
                    startNodeId = self.get_random_node_instance(self.graph, startNodeName)
                elif self.nodeCounts[endNodeName] > 0:
                    endNodeId = self.get_random_node_instance(self.graph, endNodeName)
                self.addEdge(edgeId, start = startNodeId, end = endNodeId)

    def getGraph(self):
        subGraphs = self.createFactSubGraphs()
        if len(subGraphs) > 0:
            subGraphs = sorted(subGraphs, key = lambda x : len(x[0]))
            (mainGraph, _, _) = subGraphs.pop()
            self.graph = mainGraph
            self.mergeFactSubGraphs(self.graph, subGraphs)
        self.addUnusedEdges()
        return PlannedGraph(self.graph)