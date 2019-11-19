class PositionedVertex:
    def __init__(self, identifier, x, y, label = None):
        self.identifier = identifier
        self.x = x
        self.y = y
        self.label = label
        if self.label == None:
            self.label = self.identifier


class PlannedGraph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
