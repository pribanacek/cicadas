from .grammar.CDLangListener import CDLangListener
from .Path import Path
from .ParseValidator import ParseValidator

EDGE = 'edge'
NODE = 'node'

def raise_unknown_identifier(object_id):
    raise Exception("Unknown identifier " + object_id)

class ParseListener(CDLangListener):
    def __init__(self):
        self.types = {}
        self.size = None
        self.validator = ParseValidator()

    def separateUnits(self, text):
        '''
        Separates a measurement string into the number and unit components. Eg. 1.2pt -> (1.2, 'pt') 
        Assumes that units are exactly 2 characters long.
        '''
        if len(text) > 1:
            prefix = text[:-2]
            suffix = text[-2:]
            if suffix.isalpha():
                return (float(prefix), suffix)
        return (float(text), None)
    
    def enterSize(self, ctx):
        if self.size != None:
            raise Exception("Size has already been declared")
        width_text = ctx.MEASUREMENT(0).getText()
        height_text = ctx.MEASUREMENT(1).getText()
        (width, width_unit) = self.separateUnits(width_text)
        (height, height_unit) = self.separateUnits(height_text)
        # TODO deal with units
        self.size = (width, height)
        self.validator.set_dimensions(self.size)
        
    def addEdge(self, edgeId): # move to validator?
        if edgeId in self.types:
            raise Exception(edgeId + " has already been declared")
        else:
            self.types[edgeId] = EDGE
    
    def addNode(self, node_name):
        if node_name in self.types:
            if self.types[node_name] == EDGE:
                raise Exception(node_name + " has already been declared as an arrow")
        else:
            self.types[node_name] = NODE

    def enterArrow(self, ctx):
        edge = ctx.labelledID(0)
        nodeA = ctx.labelledID(1)
        nodeB = ctx.labelledID(2)
        styles = ctx.STYLE_LIST()
        edgeId = edge.ID().getText()
        nodeAId = nodeA.ID().getText()
        nodeBId = nodeB.ID().getText()
        self.addEdge(edgeId)
        self.addNode(nodeAId)
        self.addNode(nodeBId)
        self.validator.addEdge(edgeId, nodeAId, nodeBId)

        if edge.labelText() != None:
            self.validator.set_label(edgeId, self.get_label_text(edge.labelText()))
        if nodeA.labelText() != None:
            self.validator.set_label(nodeAId, self.get_label_text(nodeA.labelText()))
        if nodeB.labelText() != None:
            self.validator.set_label(nodeBId, self.get_label_text(nodeB.labelText()))
        if styles != None:
            self.set_styles(edgeId, styles.getText())

    def enterComposition(self, ctx):
        # TODO clean this up
        pathA = ctx.path(0)
        pathB = ctx.path(1)
        label = ctx.labelText()
        label_text = None
        if label != None and label.TEXT() != None:
            label_text = label.TEXT().getText()
        identity = pathB == None
        pathFactA = Path(pathA.getText())
        pathFactB = Path(None if identity else pathB.getText())

        for edgeId in pathFactA.edgeIds + pathFactB.edgeIds:
            if not edgeId in self.types:
                raise_unknown_identifier(edgeId)
            elif self.types[edgeId] == NODE:
                raise Exception("Edge identifier expected, but got a node identifier " + edgeId)
        if identity:
            self.validator.add_identity_path(pathFactA, label_text)
        else:
            self.validator.add_compositions(pathFactA, pathFactB, label_text)

    def get_label_text(self, text_ctx):
        text = text_ctx.TEXT()
        label_text = '' if text == None else text.getText().replace('\\]', ']')
        return label_text

    def enterLabel(self, ctx):
        objectId = ctx.ID().getText()
        label_text = self.get_label_text(ctx.text())

        if objectId in self.types:
            self.validator.set_label(objectId, label_text)
        else:
            raise_unknown_identifier(objectId)
    
    def set_styles(self, object_id, style_text):
        styles = style_text[1:-1].split(',')
        self.validator.add_styles(object_id, styles)

    def enterStyle(self, ctx):
        edgeId = ctx.ID().getText()
        if not edgeId in self.types:
            raise_unknown_identifier(edgeId)
        elif self.types[edgeId] == NODE:
            raise Exception("Edge identifier expected, but got a node identifier " + edgeId)
        else:
            self.set_styles(edgeId, ctx.STYLE_LIST().getText())
    
    def get_graph_assembler(self):
        return self.validator.get_graph_assembler()