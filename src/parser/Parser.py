import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from .CDLangLexer import CDLangLexer
from .CDLangParser import CDLangParser
from .ParseListener import ParseListener
from .GraphAssembler import GraphAssembler

def parse(filename):
    inputFile = FileStream(filename)
    lexer = CDLangLexer(inputFile)
    stream = CommonTokenStream(lexer)
    parser = CDLangParser(stream)
    tree = parser.start()
    
    assembler = GraphAssembler()
    listener = ParseListener(assembler)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return assembler.getGraph()
