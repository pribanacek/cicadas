from src.plan.GraphAssembler import MergeAssembler
from src.layout.PlannedGraph import Vertex, Edge
from .PathFacts import PathFacts


class ParseValidator:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.set_labels = set()
        self.dimensions = None
        self.compositions = {}
        self.path_facts = PathFacts()
        self.path_loops = PathFacts()
    
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
            print('WARNING: ' + object_id + ' label has already been defined.')  # TODO generalise warnings
        else:
            self.set_labels.add(object_id)
        if object_id in self.nodes:
            self.nodes[object_id].label = label
        if object_id in self.edges:
            self.edges[object_id].label = label
    
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
        startNodeA = self.edges[pathA.edgeIds[0]].start.node_name
        endNodeA = self.edges[pathA.edgeIds[-1]].end.node_name
        startNodeB = self.edges[pathB.edgeIds[0]].start.node_name
        endNodeB = self.edges[pathB.edgeIds[-1]].end.node_name
        return startNodeA == startNodeB and endNodeA == endNodeB
    
    def validate_loop_ends(self, path):
        start = self.edges[path.edgeIds[0]].start.node_name
        end = self.edges[path.edgeIds[-1]].end.node_name
        return start == end
    
    def validate_paths(self, pathA, pathB):
        if not self.validate_path_continuity(pathA.edgeIds):
            raise Exception("The declared path " + str(pathA) + " is not a valid path, as it isn't continuous")
        if not self.validate_path_continuity(pathB.edgeIds):
            raise Exception("The declared path " + str(pathB) + " is not a valid path, as it isn't continuous")
        if not self.validate_path_ends(pathA, pathB):
            raise Exception("The declared paths " + str(pathA) + " and " + str(pathB) + " do not share a start/end node")
    
    def validate_path_loop(self, path):
        if not self.validate_path_continuity(path.edgeIds):
            raise Exception("The declared path " + str(path) + " is not a valid path, as it isn't continuous")
        if not self.validate_loop_ends(path):
            raise Exception("The declared path " + str(path) + " does not loop, so cannot be an ID")

    def add_compositions(self, pathA, pathB):
        self.validate_paths(pathA, pathB)
        self.path_facts.add_fact(pathA, pathB)
    
    def add_identity_path(self, path):
        self.validate_path_loop(path)
        self.path_loops.add_fact(path)

    def get_graph_assembler(self):
        if self.dimensions == None:
            raise Exception("Dimensions have not been declared") # TODO use some nice default
        return MergeAssembler(self.nodes, self.edges, self.path_facts, self.path_loops, self.dimensions)
