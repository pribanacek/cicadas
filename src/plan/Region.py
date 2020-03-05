from abc import ABC, abstractmethod
from src.layout.Label import Label
import src.plan.GraphUtils as GraphUtils
import networkx as nx
import numpy as np

class Region(ABC):
    def __init__(self, region_id, label = ''):
        self.region_id = region_id
        # self.node_data = node_data
        # self.edge_data = edge_data
        self.label = Label(label)
        self.graph = nx.OrderedMultiDiGraph()
        self.path_node_ids = None
    
    @abstractmethod
    def construct_region_graph(self, node_data, edge_data, node_counts):
        pass

    def apply_node_mapping(self, mapping):
        mapped_path_ids = tuple(map(lambda ids : tuple(map(lambda x: x if not x in mapping else mapping[x], ids)), self.path_node_ids))
        self.mapped_path_ids = mapped_path_ids
        self.node_id_mapping = mapping
    
    def compute_label_position(self, graph):
        mapped_set = list(self.mapped_path_ids[0]) + ([] if len(self.mapped_path_ids) < 2 else list(self.mapped_path_ids[1]))
        positions = np.array([graph.nodes[node_id]['pos'] for node_id in set(mapped_set)])
        x, y = positions.sum(axis = 0) / len(positions)
        self.label_position = np.array((x, y))
        return self.label_position
    
    @abstractmethod
    def paths(self):
        pass

    @abstractmethod
    def edge_set(self):
        pass

    @abstractmethod
    def ordered_edges(self):
        pass

    @abstractmethod
    def is_identity(self):
        pass

class RegionLoop(Region):
    def __init__(self, region_id, path, label = ''):
        super().__init__(region_id, label = label)
        self.path = path
    
    def construct_region_graph(self, node_data, edge_data, node_counts):
        path = list(map(lambda x : edge_data[x], self.path.edge_ids))
        path_ids = GraphUtils.add_path(self.graph, path, node_counts, loop = True, regions = [self.region_id])
        self.path_node_ids = (path_ids,)
        return self.graph

    def paths(self):
        return (self.path,)

    def ordered_edges(self):
        return list(self.path.edge_ids)
    
    def edge_set(self):
        return set(self.path.edge_ids)
    
    def is_identity(self):
        return True

class RegionPair(Region):
    def __init__(self, region_id, path_pair, label = ''):
        super().__init__(region_id, label = label)
        self.path_pair = path_pair
    
    def construct_region_graph(self, node_data, edge_data, node_counts):
        pathA, pathB = self.path_pair
        pathA = list(map(lambda x : edge_data[x], pathA.edge_ids))
        pathB = list(map(lambda x : edge_data[x], pathB.edge_ids))
        pathAIds = GraphUtils.add_path(self.graph, pathA, node_counts, regions = [self.region_id])
        pathBIds = GraphUtils.add_path(self.graph, pathB, node_counts, start = pathAIds[0], end = pathAIds[-1], regions = [self.region_id])
        self.path_node_ids = (pathAIds, pathBIds)
        return self.graph

    def paths(self):
        return self.path_pair
    
    def ordered_edges(self):
        pathA, pathB = self.path_pair
        return list(pathA.edge_ids) + list(reversed(pathB.edge_ids))
    
    def edge_set(self):
        pathA, pathB = self.path_pair
        return set(pathA.edge_ids) | set(pathB.edge_ids)

    def is_identity(self):
        return False


