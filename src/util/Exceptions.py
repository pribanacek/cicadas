class ParsingException(Exception):
    name = 'ParsingException'

    def __init__(self, msg, pos = None):
        self.msg = msg
        self.position = None
        if pos != None:
            line, col = pos
            if line != None:
                self.position = str(line)
                if col != None:
                    self.position += ':' + str(col)
    
    def __str__(self):
        return self.name + ': ' + self.msg

class SyntaxException(ParsingException):
    name = 'Syntax error'

class TypeMismatchException(ParsingException):
    name = 'Type mismatch error'

class DeclarationException(ParsingException):
    name = 'Declaration error'

class PathValidationException(ParsingException):
    name = 'Path validation error'

class LatexException(Exception):
    pass
