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
        edgeId = ctx.ID(0).getText()
        nodeAId = ctx.ID(1).getText()
        nodeBId = ctx.ID(2).getText()
        self.addEdge(edgeId)
        self.addNode(nodeAId)
        self.addNode(nodeBId)
        self.validator.addEdge(edgeId, nodeAId, nodeBId)

    def enterComposition(self, ctx):
        # TODO clean this up
        pathA = ctx.path(0)
        pathB = ctx.path(1)
        identity = pathB == None
        pathFactA = Path(pathA.getText())
        pathFactB = Path(None if identity else pathB.getText())

        for edgeId in pathFactA.edgeIds + pathFactB.edgeIds:
            if not edgeId in self.types:
                raise_unknown_identifier(edgeId)
            elif self.types[edgeId] == NODE:
                raise Exception("Edge identifier expected, but got a node identifier " + edgeId)
        if identity:
            self.validator.add_identity_path(pathFactA)
        else:
            self.validator.add_compositions(pathFactA, pathFactB)

    def enterLabel(self, ctx):
        objectId = ctx.ID().getText()
        label = ctx.text().TEXT()
        labelText = '' if label == None else label.getText().replace('\\]', ']')

        if objectId in self.types:
            self.validator.setLabel(objectId, labelText)
        else:
            raise_unknown_identifier(objectId)

    def enterStyle(self, ctx):
        edgeId = ctx.ID().getText()
        styleList = ctx.STYLE_LIST().getText()[1:-1]
        styles = styleList.split(',')

        if not edgeId in self.types:
            raise_unknown_identifier(edgeId)
        elif self.types[edgeId] == NODE:
            raise Exception("Edge identifier expected, but got a node identifier " + edgeId)
        else:
            self.validator.addStyles(edgeId, styles)
    
    def getGraphAssembler(self):
        return self.validator.getGraphAssembler()