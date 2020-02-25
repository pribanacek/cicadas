from abc import ABC, abstractmethod
from src.layout.Label import Label
import networkx as nx

class Region(ABC):
    def __init__(self, region_id, label = ''):
        self.region_id = region_id
        # self.node_data = node_data
        # self.edge_data = edge_data
        self.label = Label(label)
    
    @abstractmethod
    def construct_region_graph(self, node_count, edge_count):
        pass
    
    @abstractmethod
    def paths(self):
        pass

    @abstractmethod
    def is_identity(self):
        pass

class RegionLoop(Region):
    def __init__(self, region_id, path, label = ''):
        super().__init__(region_id, label = label)
        self.path = path
    
    def construct_region_graph(self, node_count, edge_count):
        # TODO move subgraph construction here
        pass

    def paths(self):
        return (self.path,)
    
    def is_identity(self):
        return True

class RegionPair(Region):
    def __init__(self, region_id, path_pair, label = ''):
        super().__init__(region_id, label = label)
        self.path_pair = path_pair
    
    def construct_region_graph(self, node_count, edge_count):
        # TODO move subgraph construction here
        pass

    def paths(self):
        return self.path_pair

    def is_identity(self):
        return False


