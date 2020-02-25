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
    def __init__(self, nodes, edges, regions, dimensions):
        self.nodes = nodes
        self.nodeCounts = {node_name: 0 for node_name in self.nodes}
        self.edges = edges
        self.edgeCounts = {edgeId: 0 for edgeId in self.edges}
        self.regions = regions
        self.dimensions = dimensions
        self.graphCycles = {}
        self.graph = nx.OrderedMultiDiGraph()
    
    def addNodeCount(self, node_name):
        self.nodeCounts[node_name] += 1
    
    def addEdgeCount(self, edgeId):
        self.edgeCounts[edgeId] += 1
    
    def newGraphNodeId(self, node_name):
        count = self.nodeCounts[node_name]
        self.addNodeCount(node_name)
        return node_name + '-' + str(count)
    
    def addNodeInstance(self, node_name, graph = None):
        graph = graph if graph != None else self.graph
        node_data = self.nodes[node_name]
        node_id = self.newGraphNodeId(node_name)
        graph.add_node(node_id, data = node_data, pos = (0, 0))
        return node_id
    
    def addEdge(self, edgeId, start = None, end = None, graph = None):
        graph = graph if graph != None else self.graph
        edge = self.edges[edgeId]
        startNode = edge.start.node_name
        endNode = edge.end.node_name
        graphStartId = start if start != None else self.addNodeInstance(startNode, graph = graph)
        graphEndId = end if end != None else self.addNodeInstance(endNode, graph = graph)
        graph.add_edge(graphStartId, graphEndId, edgeId, data = edge)
        self.addEdgeCount(edgeId)
        return (graphStartId, graphEndId)
    
    def addPath(self, path, start = None, end = None, graph = None, loop = False):
        graph = graph if graph != None else self.graph
        path_start_name = self.edges[path.edgeIds[0]].start.node_name
        path_end_name = self.edges[path.edgeIds[-1]].end.node_name
        path_start_id = start if start != None else self.addNodeInstance(path_start_name, graph = graph)
        path_end_id = None
        if loop:
            path_end_id = path_start_id
        elif end != None:
            path_end_id = end
        else:
            path_end_id = self.addNodeInstance(path_end_name, graph = graph)

        pathIds = [path_start_id]
        for i in range(len(path.edgeIds) - 1):
            edgeId = path.edgeIds[i]
            (_, edge_end_id) = self.addEdge(edgeId, start = pathIds[-1], graph = graph)
            pathIds.append(edge_end_id)
        self.addEdge(path.edgeIds[-1], start = pathIds[-1], end = path_end_id, graph = graph)
        pathIds.append(path_end_id)
        return pathIds
        
    def getGraph(self):
        return PlannedGraph(self.graph, self.regions, self.dimensions)

class MergeAssembler(GraphAssembler):   
    def create_fact_subgraphs(self):
        subGraphs = []
        loop_regions = filter(lambda x : x.is_identity(), self.regions)
        pair_regions = filter(lambda x : not x.is_identity(), self.regions)
        for region in loop_regions:
            (loop,) = region.paths()
            graph = nx.OrderedMultiDiGraph()
            path_ids = self.addPath(loop, graph = graph, loop = True)
            data = (graph, path_ids, ())
            subGraphs.append(data)
        for region in pair_regions:
            (pathA, pathB) = region.paths()
            graph = nx.OrderedMultiDiGraph()
            pathAIds = self.addPath(pathA, graph = graph)
            pathBIds = self.addPath(pathB, start = pathAIds[0], end = pathAIds[-1], graph = graph)
            data = (graph, pathAIds, pathBIds)
            subGraphs.append(data)
        return subGraphs
    
    def createRemainingSubGraphs(self):
        subGraphs = []
        for edgeId in self.edges:
            if self.edgeCounts[edgeId] < 1:
                graph = nx.OrderedMultiDiGraph()
                self.addEdge(edgeId, graph = graph)
                subGraphs.append(graph)
        return subGraphs
    
    def node_ids_to_lcs_string(self, node_ids, graph):
        if len(node_ids) < 1:
            return ([], [])
        node = graph.nodes[node_ids[0]]['data']
        id_string = [node_ids[0]]
        name_string = [node.node_name]
        for i in range(len(node_ids) - 1):
            nodeA_id = node_ids[i]
            nodeB_id = node_ids[i + 1]
            edge_data = graph.get_edge_data(nodeA_id, nodeB_id)
            edge_id = list(dict(edge_data).keys())[0]
            nodeB_data = graph.nodes[nodeB_id]['data']
            id_string.append(edge_id)
            name_string.append(edge_id)
            id_string.append(nodeB_id)
            name_string.append(nodeB_data.node_name)
        return (id_string, name_string) ###
    
    def get_max_subgraph_mapping(self, graph, subGraph, pathAIds, pathBIds):
        cutoff = max(len(pathAIds), len(pathBIds))
        (stringAIds, stringANames) = self.node_ids_to_lcs_string(pathAIds, subGraph)
        (stringBIds, stringBNames) = self.node_ids_to_lcs_string(pathBIds, subGraph)
        mappings_A = []
        mappings_B = []
        for node in graph:
            targets = [x for x in graph if x != node]
            allPaths = nx.all_simple_paths(graph, source = node, target = targets, cutoff = cutoff)
            for path in allPaths:
                (pathStringIds, pathStringNames) = self.node_ids_to_lcs_string(path, graph)
                matchA = LCS(stringANames, pathStringNames)
                matchB = LCS(stringBNames, pathStringNames)
                if matchA != None:
                    mapping = get_node_id_mapping(stringAIds, pathStringIds, matchA)
                    mappings_A.append(mapping)
                if matchB != None:
                    mapping = get_node_id_mapping(stringBIds, pathStringIds, matchB)
                    mappings_B.append(mapping)

        maximum_mapping = {}
        if len(mappings_A) + len(mappings_B) > 0:
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
                node_data = subGraph.nodes[nodeId]
                graph.add_node(mappedNodeId, data = node_data['data'], pos = node_data['pos'])
        for start, end, edgeId, edge_data in subGraph.edges(keys = True, data = 'data'):
            mappedStart = start if not start in mapping else mapping[start]
            mappedEnd = end if not end in mapping else mapping[end]
            graph.add_edge(mappedStart, mappedEnd, edgeId, data = edge_data)
        return graph
    
    def mergeFactSubGraphs(self, graph, subGraphs):
        for (subGraph, pathAIds, pathBIds) in subGraphs:
            mapping = self.get_max_subgraph_mapping(graph, subGraph, pathAIds, pathBIds)
            self.mergeFactSubGraph(graph, subGraph, mapping)
    
    def get_random_node_instance(self, graph, node_name):
        nodes = [x for x, y in graph.nodes(data = 'data') if y.node_name == node_name]
        return random.choice(nodes)

    def addUnusedEdges(self):
        for edgeId, count in self.edgeCounts.items():
            if count == 0:
                edge = self.edges[edgeId]
                start_node_name = edge.start.node_name
                end_node_name = edge.end.node_name
                start_node_id = None
                end_node_id = None
                if self.nodeCounts[start_node_name] > 0:
                    start_node_id = self.get_random_node_instance(self.graph, start_node_name)
                elif self.nodeCounts[end_node_name] > 0:
                    end_node_id = self.get_random_node_instance(self.graph, end_node_name)
                self.addEdge(edgeId, start = start_node_id, end = end_node_id)

    def getGraph(self):
        subGraphs = self.create_fact_subgraphs()
        if len(subGraphs) > 0:
            subGraphs = sorted(subGraphs, key = lambda x : len(x[0]))
            (mainGraph, _, _) = subGraphs.pop()
            self.graph = mainGraph
            self.mergeFactSubGraphs(self.graph, subGraphs)
        self.addUnusedEdges()
        return PlannedGraph(self.graph, self.regions, self.dimensions)