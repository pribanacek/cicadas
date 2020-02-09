from .grammar.CDLangListener import CDLangListener
from .Path import Path
from .ParseValidator import ParseValidator

EDGE = 'edge'
NODE = 'node'

class ParseListener(CDLangListener):
    def __init__(self):
        self.types = {}
        self.validator = ParseValidator()
    
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
        pathA = Path(ctx.path(0).getText())
        pathB = Path(ctx.path(1).getText())

        for edgeId in pathA.edgeIds + pathB.edgeIds:
            if not edgeId in self.types:
                raise Exception("Unknown identifier " + edgeId)
            elif self.types[edgeId] == NODE:
                raise Exception("Edge identifier expected, but got a node identifier " + edgeId)
        self.validator.addCompositions(pathA, pathB)

    def enterLabel(self, ctx):
        objectId = ctx.ID().getText()
        label = ctx.text().TEXT()
        labelText = '' if label == None else label.getText().replace('\\]', ']')

        if objectId in self.types:
            self.validator.setLabel(objectId, labelText)
        else:
            raise Exception("Unknown identifier " + objectId)

    def enterStyle(self, ctx):
        edgeId = ctx.ID().getText()
        styleList = ctx.STYLE_LIST().getText()[1:-1]
        styles = styleList.split(',')

        if not edgeId in self.types:
            raise Exception("Unknown identifier " + edgeId)
        elif self.types[edgeId] == NODE:
            raise Exception("Edge identifier expected, but got a node identifier " + edgeId)
        else:
            self.validator.addStyles(edgeId, styles)
    
    def getGraphAssembler(self):
        return self.validator.getGraphAssembler()