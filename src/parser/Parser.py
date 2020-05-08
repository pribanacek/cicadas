import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker, InputStream
from .grammar.CDLangLexer import CDLangLexer
from .grammar.CDLangParser import CDLangParser
from .ParseListener import ParseListener
from .ParseErrorListener import ParseErrorListener

def _parse_stream(input_stream):
    lexer = CDLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CDLangParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ParseErrorListener())
    tree = parser.start()
    listener = ParseListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.get_graph_assembler()

def parse_file(filename):
    input_stream = FileStream(filename)
    return _parse_stream(input_stream)

def parse_string(string):
    input_stream = InputStream(string)
    return _parse_stream(input_stream)