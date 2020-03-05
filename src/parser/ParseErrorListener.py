import sys
from antlr4 import *
from .grammar.CDLangListener import CDLangListener
from .Path import Path
from .ParseValidator import ParseValidator
from antlr4.error.ErrorListener import *
import io

class ParseErrorListener(ErrorListener):
  
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):        
        position = str(line) + ':' + str(column)
        print('Syntax error at position ' + position + ': ' + msg)
        sys.exit()
