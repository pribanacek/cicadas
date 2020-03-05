import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from .grammar.CDLangLexer import CDLangLexer
from .grammar.CDLangParser import CDLangParser
from .ParseListener import ParseListener
from .ParseErrorListener import ParseErrorListener

def parse(filename):
    inputFile = FileStream(filename)
    lexer = CDLangLexer(inputFile)
    stream = CommonTokenStream(lexer)

    parser = CDLangParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ParseErrorListener())
    
    tree = parser.start()
    
    listener = ParseListener()

    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener.get_graph_assembler()
