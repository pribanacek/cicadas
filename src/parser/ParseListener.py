from src.util.Exceptions import DeclarationException, TypeMismatchException
from .grammar.CDLangListener import CDLangListener
from .Path import Path
from .ParseValidator import ParseValidator

EDGE = 'edge'
NODE = 'node'

def raise_unknown_identifier(x, pos = None):
    raise DeclarationException("unknown identifier '" + x + "'", pos = pos)

def raise_already_declared(x, pos = None):
    raise DeclarationException(x + " has already been declared", pos = pos)

def raise_type_mismatch_edge(x, pos = None):
    raise TypeMismatchException("node identifier expected, but got an edge identifier " + x, pos = pos)

def raise_type_mismatch_node(x, pos = None):
    raise TypeMismatchException("edge identifier expected, but got a node identifier " + x, pos = pos)


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
            raise_already_declared("size", pos = (ctx.start.line, ctx.start.column))
        width_text = ctx.NUMBER(0).getText()
        height_text = ctx.NUMBER(1).getText()
        (width, _) = self.separateUnits(width_text)
        (height, _) = self.separateUnits(height_text)
        # TODO deal with units
        self.size = (width, height)
        self.validator.set_dimensions(self.size)
        
    def addEdge(self, edge_id, pos = None):
        if edge_id in self.types:
            raise_already_declared("edge '%s'" % edge_id, pos = pos)
        else:
            self.types[edge_id] = EDGE
    
    def addNode(self, node_name, pos = None):
        if node_name in self.types:
            if self.types[node_name] == EDGE:
                raise_type_mismatch_edge(node_name, pos = pos)
        else:
            self.types[node_name] = NODE

    def enterArrow(self, ctx):
        line = ctx.start.line
        edge = ctx.labelledID(0)
        nodeA = ctx.labelledID(1)
        nodeB = ctx.labelledID(2)
        styles = ctx.STYLE_LIST()
        edge_id = edge.IDENTIFIER().getText()
        nodeAId = nodeA.IDENTIFIER().getText()
        nodeBId = nodeB.IDENTIFIER().getText()
        self.addEdge(edge_id, pos = (line, edge.start.column))
        self.addNode(nodeAId, pos = (line, nodeA.start.column))
        self.addNode(nodeBId, pos = (line, nodeB.start.column))
        self.validator.addEdge(edge_id, nodeAId, nodeBId)

        if edge.labelText() != None:
            self.validator.set_label(edge_id, self.get_label_text(edge.labelText()))
        if nodeA.labelText() != None:
            self.validator.set_label(nodeAId, self.get_label_text(nodeA.labelText()))
        if nodeB.labelText() != None:
            self.validator.set_label(nodeBId, self.get_label_text(nodeB.labelText()))
        if styles != None:
            self.set_styles(edge_id, styles.getText())

    def enterComposition(self, ctx):
        # TODO clean this up
        line = ctx.start.line
        pathA = ctx.path(0)
        pathB = ctx.path(1)
        label = ctx.labelText()
        label_text = None
        if label != None and label.TEXT() != None:
            label_text = label.TEXT().getText()
        identity = pathB == None
        pathFactA = Path(pathA.getText())
        pathFactB = Path(None if identity else pathB.getText())

        for edge_id in pathFactA.edge_ids + pathFactB.edge_ids:
            if not edge_id in self.types:
                raise_unknown_identifier(edge_id, pos = (line, None))
            elif self.types[edge_id] == NODE:
                raise_type_mismatch_node(edge_id, pos = (line, None))
        if identity:
            self.validator.add_identity_path(pathFactA, label_text)
        else:
            self.validator.add_compositions(pathFactA, pathFactB, label_text)

    def get_label_text(self, text_ctx):
        text = text_ctx.TEXT()
        label_text = '' if text == None else text.getText().replace('\\]', ']')
        return label_text

    def enterLabel(self, ctx):
        object_id = ctx.IDENTIFIER().getText()
        label_text = self.get_label_text(ctx.labelText())

        if object_id in self.types:
            self.validator.set_label(object_id, label_text)
        else:
            raise_unknown_identifier(object_id, pos = (ctx.start.line, None))
    
    def set_styles(self, object_id, style_text):
        styles = style_text[1:-1].split(',')
        self.validator.add_styles(object_id, styles)

    def enterStyle(self, ctx):
        edge_id = ctx.IDENTIFIER().getText()
        if not edge_id in self.types:
            raise_unknown_identifier(edge_id, pos = (ctx.start.line, None))
        elif self.types[edge_id] == NODE:
            raise_type_mismatch_node(edge_id, pos = (ctx.start.line, None))
        else:
            self.set_styles(edge_id, ctx.STYLE_LIST().getText())
    
    def get_graph_assembler(self):
        return self.validator.get_graph_assembler()