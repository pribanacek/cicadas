from .grammar.CDLangListener import CDLangListener
from .Path import Path

EDGE = 'edge'
NODE = 'node'

class ParseListener(CDLangListener):
    def __init__(self, assembler):
        self.types = {}
        self.assembler = assembler
    
    def addEdge(self, edgeId): # move to validator?
        if edgeId in self.types:
            raise Exception(edgeId + " has already been declared")
        else:
            self.types[edgeId] = EDGE
    
    def addNode(self, nodeId):
        if nodeId in self.types:
            idType = self.types[nodeId]
            if idType == EDGE:
                raise Exception(nodeId + " has already been declared as an arrow")
        else:
            self.types[nodeId] = NODE

    def enterArrow(self, ctx):
        edgeId = ctx.ID(0).getText()
        nodeAId = ctx.ID(1).getText()
        nodeBId = ctx.ID(2).getText()
        self.addEdge(edgeId)
        self.addNode(nodeAId)
        self.addNode(nodeBId)
        self.assembler.addEdge(edgeId, nodeAId, nodeBId)

    def enterComposition(self, ctx):
        pathA = Path(ctx.path(0).getText())
        pathB = Path(ctx.path(1).getText())

        for edgeId in pathA.edgeIds + pathB.edgeIds:
            if not edgeId in self.types:
                raise Exception("Unknown identifier " + edgeId)
            elif self.types[edgeId] == NODE:
                raise Exception("Edge identifier expected, but got a node identifier " + edgeId)
        self.assembler.addCompositions(pathA, pathB)

    def enterLabel(self, ctx):
        objectId = ctx.ID().getText()
        label = ctx.text().TEXT()
        labelText = '' if label == None else label.getText().replace('\\]', ']')

        if objectId in self.types:
            self.assembler.setLabel(objectId, labelText)
        else:
            raise Exception("Unknown identifier " + objectId)

    def enterStyle(self, ctx):
        edgeId = ctx.ID().getText()
        style = ctx.text().TEXT().getText()

        if not edgeId in self.types:
            raise Exception("Unknown identifier " + edgeId)
        elif self.types[edgeId] == NODE:
            raise Exception("Edge identifier expected, but got a node identifier " + edgeId)
        else:
            self.assembler.addStyle(edgeId, style)
