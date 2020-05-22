from src.util.Logging import info
from src.layout.PositionedGraph import PositionedGraph
import src.topology.GraphUtils as GraphUtils
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

def get_lcs_string_mapping(sourceIds, targetIds, match):
    # compute the mapping between two LCS strings
    if match == None:
        return None
    mapping = OrderedDict()
    for i in range(match.size):
        a = sourceIds[match.a + i]
        b = targetIds[match.b + i]
        mapping[a] = b
    return mapping


class GraphAssembler:
    def __init__(self, nodes, edges, regions, dimensions):
        self.nodes = nodes
        self.edges = edges
        self.regions = regions
        self.dimensions = dimensions
        self.node_counts = {node_name: 0 for node_name in self.nodes}
        self.graph = nx.OrderedMultiDiGraph()
        
class MergeAssembler(GraphAssembler):   
    def create_fact_subgraphs(self):
        # construct subgraphs for each region
        for region in self.regions:
            region.construct_region_graph(self.nodes, self.edges, self.node_counts)
        
    def node_ids_to_lcs_string(self, node_ids, graph):
        # construct strings for LCS from a graph path
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
        return (id_string, name_string)
        
    def get_max_subgraph_mapping(self, graph, subGraph, paths, cutoff = None):
        # compute maximum safe mapping between the given graph and the main graph
        pathAIds = paths[0]
        pathBIds = [] if len(paths) < 2 else paths[1]
        cutoff = max(len(pathAIds), len(pathBIds)) if cutoff == None else cutoff
        (stringAIds, stringANames) = self.node_ids_to_lcs_string(pathAIds, subGraph)
        (stringBIds, stringBNames) = self.node_ids_to_lcs_string(pathBIds, subGraph)
        mappings_A = []
        mappings_B = []

        for node in graph:
            targets = [x for x in graph if x != node]
            nx_paths = nx.all_simple_paths(graph, source = node, target = targets, cutoff = cutoff)
            all_paths = list(nx_paths) + [[node]]
            for path in all_paths:
                (pathStringIds, pathStringNames) = self.node_ids_to_lcs_string(path, graph)
                matchA = LCS(stringANames, pathStringNames)
                matchB = LCS(stringBNames, pathStringNames)
                mapping_A = get_lcs_string_mapping(stringAIds, pathStringIds, matchA)
                mapping_B = get_lcs_string_mapping(stringBIds, pathStringIds, matchB)
                if mapping_A != None:
                    mappings_A.append(mapping_A)
                if mapping_B != None:
                    mappings_B.append(mapping_B)

        maximum_mapping = {}
        if len(mappings_A) + len(mappings_B) > 0:
            maximum_mapping = max({}, *mappings_A, *mappings_B, key = len)
        ties = [maximum_mapping]

        for mapA in mappings_A:
            for mapB in mappings_B:
                if self.is_mapping_compatible(mapA, mapB, pathAIds, stringAIds, stringBIds):
                    new_max = OrderedDict(list(mapA.items()) + list(mapB.items()))
                    if len(new_max) > len(maximum_mapping):
                        maximum_mapping = new_max
                        ties = [maximum_mapping]
                    elif len(new_max) == len(maximum_mapping):
                        ties.append(new_max)

        # prefer merge if it's the entirety of either path
        for m in ties:
            x = list(m.keys())[::2]
            if x == pathAIds or x == pathBIds:
                return m

        return maximum_mapping
    
    def is_mapping_compatible(self, mapA, mapB, pathAIds, stringA, stringB):
        # check if two pair-region subgraphs are safe to merge
        listA = list(mapA)
        listB = list(mapB)
        start = pathAIds[0]
        end = pathAIds[-1]
        maps_adjacent = False
        if listA[0] == start and listB[0] == start:
            maps_adjacent = True
        if listA[-1] == end and listB[-1] == end:
            maps_adjacent = True
        
        if not maps_adjacent:
            return False

        caiusA = set(mapA.keys())
        caiusB = set(mapB.keys())
        if len(caiusA) == len(stringA) or len(caiusB) == len(stringB):
            return False

        for ka, va in mapA.items():
            for kb, vb in mapB.items():
                if va == vb and ka != kb:
                    return False
                elif ka == kb and va != vb:
                    return False       
        return True
    
    def merge_fact_subgraph(self, graph, subGraph, mapping):
        # merge the given graphs according to the given mapping
        for node_id in subGraph:
            mapped_id = node_id if not node_id in mapping else mapping[node_id]
            if mapped_id not in graph:
                node_data = subGraph.nodes[node_id]
                graph.add_node(mapped_id, data = node_data['data'], pos = node_data['pos'], regions = node_data['regions'])
            else:
                regionsA = subGraph.nodes[node_id]['regions']
                regionsB = graph.nodes[mapped_id]['regions']
                graph.nodes[mapped_id]['regions'] = regionsA | regionsB
        for start, end, edge_id, edge_data in subGraph.edges(keys = True, data = 'data'):
            mapped_start = start if not start in mapping else mapping[start]
            mapped_end = end if not end in mapping else mapping[end]
            graph.add_edge(mapped_start, mapped_end, edge_id, data = edge_data)
        return graph
    
    def merge_regions(self, graph, regions):
        # successively merge all the regions into the main graph
        for region in regions:
            subgraph = region.graph
            mapping = self.get_max_subgraph_mapping(graph, region.graph, region.path_node_ids)
            region.apply_node_mapping(mapping)
            self.merge_fact_subgraph(graph, subgraph, mapping)
    
    def get_random_node_instance(self, graph, node_name):
        # select a random node from the graph with the given name
        nodes = [x for x, y in graph.nodes(data = 'data') if y.node_name == node_name]
        if len(nodes) == 0:
            return None
        return random.choice(nodes)

    def add_unused_edges(self):
        # add edges that did not feature in any of the regions
        self.nonregion_edges = [eid for eid in self.edges if not any(eid in r.edge_set() for r in self.regions)]
        for edge_id in self.nonregion_edges:
            edge = self.edges[edge_id]
            start_node_name = edge.start.node_name
            end_node_name = edge.end.node_name
            start_node_id = self.get_random_node_instance(self.graph, start_node_name)
            end_node_id = None
            if start_node_id == None:
                end_node_id = self.get_random_node_instance(self.graph, end_node_name)
            GraphUtils.add_edge(self.graph, edge, self.node_counts, start = start_node_id, end = end_node_id)

    def get_graph(self):
        # construct the graph topology and return a positioned graph
        if len(self.regions) > 0:
            self.create_fact_subgraphs()
            loop_regions = filter(lambda x : x.is_identity(), self.regions)
            pair_regions = filter(lambda x : not x.is_identity(), self.regions)
            sort_options = {'key': lambda x : len(x.graph), 'reverse': True}
            self.merge_regions(self.graph, list(sorted(pair_regions, **sort_options)))
            self.add_unused_edges()
            self.merge_regions(self.graph, list(sorted(loop_regions, **sort_options)))
        else:
            self.add_unused_edges()

        N = len(self.graph.nodes)
        E = len(self.graph.edges)
        info('Constructed graph with %s nodes and %s edges' % (N, E))
        
        return PositionedGraph(self.graph, self.regions, self.dimensions)
