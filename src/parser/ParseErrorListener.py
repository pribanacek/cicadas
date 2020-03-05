from src.util.Exceptions import SyntaxException
from antlr4.error.ErrorListener import ErrorListener

class ParseErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):        
        raise SyntaxException(msg, pos = (line, column))
