from src.util.Warning import warn
from src.util.Exceptions import PathValidationException
from src.plan.GraphAssembler import MergeAssembler
from src.plan.Region import RegionLoop, RegionPair
from src.layout.PlannedGraph import Vertex, Edge
from .PathFacts import PathFacts

def raise_path_not_continuous(path):
    raise PathValidationException("The declared path '" + str(path) + "' is not a valid path, as it is not continuous")

def raise_paths_endpoints(pathA, pathB):
    raise PathValidationException("The declared paths '" + str(pathA) + "' and '" + str(pathB) + "' do not share a start/end node")

def raise_path_not_a_loop(path):
    raise PathValidationException("The declared path '" + str(path) + "' does not loop, so cannot be an identity")


class ParseValidator:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.set_labels = set()
        self.dimensions = None
        self.compositions = {}
        self.regions = []
    
    def set_dimensions(self, dimensions):
        self.dimensions = dimensions

    def addEdge(self, edgeId, nodeAId, nodeBId):
        if nodeAId not in self.nodes:
            self.nodes[nodeAId] = Vertex(nodeAId)
        if nodeBId not in self.nodes:
            self.nodes[nodeBId] = Vertex(nodeBId)
        edge = Edge(edgeId, self.nodes[nodeAId], self.nodes[nodeBId])
        self.edges[edgeId] = edge

    def set_label(self, object_id, label):
        if object_id in self.set_labels:
            warn(object_id + ' label has already been defined')
        else:
            self.set_labels.add(object_id)
        if object_id in self.nodes:
            self.nodes[object_id].set_label(label)
        if object_id in self.edges:
            self.edges[object_id].set_label(label)
    
    def add_styles(self, edgeId, style_list):
        # styles = self.edges[edgeId].styles
        # self.edges[edgeId].styles = styles + style_list
        self.edges[edgeId].styles = style_list

    def validate_path_continuity(self, path):
        for i in range(len(path) - 1):
            edge1 = self.edges[path[i]]
            edge2 = self.edges[path[i + 1]]
            if edge1.end.node_name != edge2.start.node_name:
                return False
        return True
    
    def validate_path_ends(self, pathA, pathB):
        startNodeA = self.edges[pathA.edge_ids[0]].start.node_name
        endNodeA = self.edges[pathA.edge_ids[-1]].end.node_name
        startNodeB = self.edges[pathB.edge_ids[0]].start.node_name
        endNodeB = self.edges[pathB.edge_ids[-1]].end.node_name
        return startNodeA == startNodeB and endNodeA == endNodeB
    
    def validate_loop_ends(self, path):
        start = self.edges[path.edge_ids[0]].start.node_name
        end = self.edges[path.edge_ids[-1]].end.node_name
        return start == end
    
    def validate_paths(self, pathA, pathB):
        if not self.validate_path_continuity(pathA.edge_ids):
            raise_path_not_continuous(pathA)
        if not self.validate_path_continuity(pathB.edge_ids):
            raise_path_not_continuous(pathB)
        if not self.validate_path_ends(pathA, pathB):
            raise_paths_endpoints(pathA, pathB)
    
    def validate_path_loop(self, path):
        if not self.validate_path_continuity(path.edge_ids):
            raise_path_not_continuous(path)
        if not self.validate_loop_ends(path):
            raise_path_not_a_loop(path)

    def add_compositions(self, pathA, pathB, label):
        self.validate_paths(pathA, pathB)
        region_id = len(self.regions)
        region = RegionPair(region_id, (pathA, pathB), label = label)
        self.regions.append(region)
    
    def add_identity_path(self, path, label):
        self.validate_path_loop(path)
        region_id = len(self.regions)
        region = RegionLoop(region_id, path, label = label)
        self.regions.append(region)

    def get_graph_assembler(self):
        if self.dimensions == None:
            warn("diagram size has not been declared, using default")
            self.dimensions = (8.0, 8.0)
        return MergeAssembler(self.nodes, self.edges, self.regions, self.dimensions)
