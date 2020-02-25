# Generated from CDLang.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\6\2\32\n\2")
        buf.write("\r\2\16\2\33\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3&\n\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5")
        buf.write("\5\65\n\5\3\6\3\6\3\6\3\6\5\6;\n\6\3\6\5\6>\n\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\7\nR\n\n\f\n\16\nU\13\n\3\13\3\13\5\13Y\n")
        buf.write("\13\3\f\3\f\3\f\3\f\5\f_\n\f\3\f\2\2\r\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\2\2\2b\2\31\3\2\2\2\4%\3\2\2\2\6)\3\2\2\2")
        buf.write("\b.\3\2\2\2\n\66\3\2\2\2\f?\3\2\2\2\16D\3\2\2\2\20I\3")
        buf.write("\2\2\2\22N\3\2\2\2\24V\3\2\2\2\26^\3\2\2\2\30\32\5\4\3")
        buf.write("\2\31\30\3\2\2\2\32\33\3\2\2\2\33\31\3\2\2\2\33\34\3\2")
        buf.write("\2\2\34\35\3\2\2\2\35\36\7\2\2\3\36\3\3\2\2\2\37&\5\6")
        buf.write("\4\2 &\5\b\5\2!&\5\n\6\2\"&\5\f\7\2#&\5\16\b\2$&\5\20")
        buf.write("\t\2%\37\3\2\2\2% \3\2\2\2%!\3\2\2\2%\"\3\2\2\2%#\3\2")
        buf.write("\2\2%$\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'(\7\27\2\2(\5\3\2")
        buf.write("\2\2)*\7\3\2\2*+\7\23\2\2+,\7\4\2\2,-\7\23\2\2-\7\3\2")
        buf.write("\2\2./\5\24\13\2/\60\7\5\2\2\60\61\5\24\13\2\61\62\7\6")
        buf.write("\2\2\62\64\5\24\13\2\63\65\7\26\2\2\64\63\3\2\2\2\64\65")
        buf.write("\3\2\2\2\65\t\3\2\2\2\66\67\5\22\n\2\67:\7\7\2\28;\5\22")
        buf.write("\n\29;\7\22\2\2:8\3\2\2\2:9\3\2\2\2;=\3\2\2\2<>\5\26\f")
        buf.write("\2=<\3\2\2\2=>\3\2\2\2>\13\3\2\2\2?@\7\b\2\2@A\7\25\2")
        buf.write("\2AB\7\5\2\2BC\5\26\f\2C\r\3\2\2\2DE\7\t\2\2EF\7\25\2")
        buf.write("\2FG\7\5\2\2GH\7\26\2\2H\17\3\2\2\2IJ\7\n\2\2JK\7\25\2")
        buf.write("\2KL\7\5\2\2LM\7\21\2\2M\21\3\2\2\2NS\7\25\2\2OP\7\13")
        buf.write("\2\2PR\7\25\2\2QO\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2")
        buf.write("\2T\23\3\2\2\2US\3\2\2\2VX\7\25\2\2WY\5\26\f\2XW\3\2\2")
        buf.write("\2XY\3\2\2\2Y\25\3\2\2\2Z[\7\f\2\2[\\\7\17\2\2\\_\7\r")
        buf.write("\2\2]_\7\16\2\2^Z\3\2\2\2^]\3\2\2\2_\27\3\2\2\2\n\33%")
        buf.write("\64:=SX^")
        return buf.getvalue()


class CDLangParser ( Parser ):

    grammarFileName = "CDLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'size'", "','", "':'", "'->'", "'='", 
                     "'label'", "'style'", "'impose'", "'.'", "'['", "']'", 
                     "'[]'", "<INVALID>", "<INVALID>", "<INVALID>", "'ID'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TEXT", "COMMENT", "DIRECTION", "IDENTITY", 
                      "MEASUREMENT", "NUMBER", "ID", "STYLE_LIST", "SEPARATOR", 
                      "WHITESPACE", "NEWLINE" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_size = 2
    RULE_arrow = 3
    RULE_composition = 4
    RULE_label = 5
    RULE_style = 6
    RULE_impose = 7
    RULE_path = 8
    RULE_labelledID = 9
    RULE_labelText = 10

    ruleNames =  [ "start", "statement", "size", "arrow", "composition", 
                   "label", "style", "impose", "path", "labelledID", "labelText" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    TEXT=13
    COMMENT=14
    DIRECTION=15
    IDENTITY=16
    MEASUREMENT=17
    NUMBER=18
    ID=19
    STYLE_LIST=20
    SEPARATOR=21
    WHITESPACE=22
    NEWLINE=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CDLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CDLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(CDLangParser.StatementContext,i)


        def getRuleIndex(self):
            return CDLangParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = CDLangParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.statement()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CDLangParser.T__0) | (1 << CDLangParser.T__5) | (1 << CDLangParser.T__6) | (1 << CDLangParser.T__7) | (1 << CDLangParser.ID) | (1 << CDLangParser.SEPARATOR))) != 0)):
                    break

            self.state = 27
            self.match(CDLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEPARATOR(self):
            return self.getToken(CDLangParser.SEPARATOR, 0)

        def size(self):
            return self.getTypedRuleContext(CDLangParser.SizeContext,0)


        def arrow(self):
            return self.getTypedRuleContext(CDLangParser.ArrowContext,0)


        def composition(self):
            return self.getTypedRuleContext(CDLangParser.CompositionContext,0)


        def label(self):
            return self.getTypedRuleContext(CDLangParser.LabelContext,0)


        def style(self):
            return self.getTypedRuleContext(CDLangParser.StyleContext,0)


        def impose(self):
            return self.getTypedRuleContext(CDLangParser.ImposeContext,0)


        def getRuleIndex(self):
            return CDLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = CDLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 29
                self.size()

            elif la_ == 2:
                self.state = 30
                self.arrow()

            elif la_ == 3:
                self.state = 31
                self.composition()

            elif la_ == 4:
                self.state = 32
                self.label()

            elif la_ == 5:
                self.state = 33
                self.style()

            elif la_ == 6:
                self.state = 34
                self.impose()


            self.state = 37
            self.match(CDLangParser.SEPARATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEASUREMENT(self, i:int=None):
            if i is None:
                return self.getTokens(CDLangParser.MEASUREMENT)
            else:
                return self.getToken(CDLangParser.MEASUREMENT, i)

        def getRuleIndex(self):
            return CDLangParser.RULE_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSize" ):
                listener.enterSize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSize" ):
                listener.exitSize(self)




    def size(self):

        localctx = CDLangParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(CDLangParser.T__0)
            self.state = 40
            self.match(CDLangParser.MEASUREMENT)
            self.state = 41
            self.match(CDLangParser.T__1)
            self.state = 42
            self.match(CDLangParser.MEASUREMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrowContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labelledID(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CDLangParser.LabelledIDContext)
            else:
                return self.getTypedRuleContext(CDLangParser.LabelledIDContext,i)


        def STYLE_LIST(self):
            return self.getToken(CDLangParser.STYLE_LIST, 0)

        def getRuleIndex(self):
            return CDLangParser.RULE_arrow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrow" ):
                listener.enterArrow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrow" ):
                listener.exitArrow(self)




    def arrow(self):

        localctx = CDLangParser.ArrowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arrow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.labelledID()
            self.state = 45
            self.match(CDLangParser.T__2)
            self.state = 46
            self.labelledID()
            self.state = 47
            self.match(CDLangParser.T__3)
            self.state = 48
            self.labelledID()
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CDLangParser.STYLE_LIST:
                self.state = 49
                self.match(CDLangParser.STYLE_LIST)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompositionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def path(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CDLangParser.PathContext)
            else:
                return self.getTypedRuleContext(CDLangParser.PathContext,i)


        def IDENTITY(self):
            return self.getToken(CDLangParser.IDENTITY, 0)

        def labelText(self):
            return self.getTypedRuleContext(CDLangParser.LabelTextContext,0)


        def getRuleIndex(self):
            return CDLangParser.RULE_composition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComposition" ):
                listener.enterComposition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComposition" ):
                listener.exitComposition(self)




    def composition(self):

        localctx = CDLangParser.CompositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_composition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.path()
            self.state = 53
            self.match(CDLangParser.T__4)
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CDLangParser.ID]:
                self.state = 54
                self.path()
                pass
            elif token in [CDLangParser.IDENTITY]:
                self.state = 55
                self.match(CDLangParser.IDENTITY)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CDLangParser.T__9 or _la==CDLangParser.T__11:
                self.state = 58
                self.labelText()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CDLangParser.ID, 0)

        def labelText(self):
            return self.getTypedRuleContext(CDLangParser.LabelTextContext,0)


        def getRuleIndex(self):
            return CDLangParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = CDLangParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(CDLangParser.T__5)
            self.state = 62
            self.match(CDLangParser.ID)
            self.state = 63
            self.match(CDLangParser.T__2)
            self.state = 64
            self.labelText()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StyleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CDLangParser.ID, 0)

        def STYLE_LIST(self):
            return self.getToken(CDLangParser.STYLE_LIST, 0)

        def getRuleIndex(self):
            return CDLangParser.RULE_style

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStyle" ):
                listener.enterStyle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStyle" ):
                listener.exitStyle(self)




    def style(self):

        localctx = CDLangParser.StyleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_style)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(CDLangParser.T__6)
            self.state = 67
            self.match(CDLangParser.ID)
            self.state = 68
            self.match(CDLangParser.T__2)
            self.state = 69
            self.match(CDLangParser.STYLE_LIST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ImposeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CDLangParser.ID, 0)

        def DIRECTION(self):
            return self.getToken(CDLangParser.DIRECTION, 0)

        def getRuleIndex(self):
            return CDLangParser.RULE_impose

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpose" ):
                listener.enterImpose(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpose" ):
                listener.exitImpose(self)




    def impose(self):

        localctx = CDLangParser.ImposeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_impose)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(CDLangParser.T__7)
            self.state = 72
            self.match(CDLangParser.ID)
            self.state = 73
            self.match(CDLangParser.T__2)
            self.state = 74
            self.match(CDLangParser.DIRECTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PathContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CDLangParser.ID)
            else:
                return self.getToken(CDLangParser.ID, i)

        def getRuleIndex(self):
            return CDLangParser.RULE_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath" ):
                listener.enterPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath" ):
                listener.exitPath(self)




    def path(self):

        localctx = CDLangParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_path)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(CDLangParser.ID)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CDLangParser.T__8:
                self.state = 77
                self.match(CDLangParser.T__8)
                self.state = 78
                self.match(CDLangParser.ID)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelledIDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CDLangParser.ID, 0)

        def labelText(self):
            return self.getTypedRuleContext(CDLangParser.LabelTextContext,0)


        def getRuleIndex(self):
            return CDLangParser.RULE_labelledID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelledID" ):
                listener.enterLabelledID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelledID" ):
                listener.exitLabelledID(self)




    def labelledID(self):

        localctx = CDLangParser.LabelledIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_labelledID)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(CDLangParser.ID)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CDLangParser.T__9 or _la==CDLangParser.T__11:
                self.state = 85
                self.labelText()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelTextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(CDLangParser.TEXT, 0)

        def getRuleIndex(self):
            return CDLangParser.RULE_labelText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelText" ):
                listener.enterLabelText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelText" ):
                listener.exitLabelText(self)




    def labelText(self):

        localctx = CDLangParser.LabelTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_labelText)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CDLangParser.T__9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(CDLangParser.T__9)
                self.state = 89
                self.match(CDLangParser.TEXT)
                self.state = 90
                self.match(CDLangParser.T__10)
                pass
            elif token in [CDLangParser.T__11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(CDLangParser.T__11)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





