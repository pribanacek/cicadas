# Generated from CDLang.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\30\n\2\r\2\16\2")
        buf.write("\31\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3$\n\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\5\6\67\n\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\7\nK\n\n\f\n\16\nN")
        buf.write("\13\n\3\13\3\13\3\13\3\13\5\13T\n\13\3\13\2\2\f\2\4\6")
        buf.write("\b\n\f\16\20\22\24\2\2\2U\2\27\3\2\2\2\4#\3\2\2\2\6\'")
        buf.write("\3\2\2\2\b,\3\2\2\2\n\62\3\2\2\2\f8\3\2\2\2\16=\3\2\2")
        buf.write("\2\20B\3\2\2\2\22G\3\2\2\2\24S\3\2\2\2\26\30\5\4\3\2\27")
        buf.write("\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2")
        buf.write("\32\33\3\2\2\2\33\34\7\2\2\3\34\3\3\2\2\2\35$\5\6\4\2")
        buf.write("\36$\5\b\5\2\37$\5\n\6\2 $\5\f\7\2!$\5\16\b\2\"$\5\20")
        buf.write("\t\2#\35\3\2\2\2#\36\3\2\2\2#\37\3\2\2\2# \3\2\2\2#!\3")
        buf.write("\2\2\2#\"\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\7\27\2\2&\5\3")
        buf.write("\2\2\2\'(\7\3\2\2()\7\23\2\2)*\7\4\2\2*+\7\23\2\2+\7\3")
        buf.write("\2\2\2,-\7\25\2\2-.\7\5\2\2./\7\25\2\2/\60\7\6\2\2\60")
        buf.write("\61\7\25\2\2\61\t\3\2\2\2\62\63\5\22\n\2\63\66\7\7\2\2")
        buf.write("\64\67\5\22\n\2\65\67\7\22\2\2\66\64\3\2\2\2\66\65\3\2")
        buf.write("\2\2\67\13\3\2\2\289\7\b\2\29:\7\25\2\2:;\7\5\2\2;<\5")
        buf.write("\24\13\2<\r\3\2\2\2=>\7\t\2\2>?\7\25\2\2?@\7\5\2\2@A\7")
        buf.write("\26\2\2A\17\3\2\2\2BC\7\n\2\2CD\7\25\2\2DE\7\5\2\2EF\7")
        buf.write("\21\2\2F\21\3\2\2\2GL\7\25\2\2HI\7\13\2\2IK\7\25\2\2J")
        buf.write("H\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\23\3\2\2\2NL")
        buf.write("\3\2\2\2OP\7\f\2\2PQ\7\17\2\2QT\7\r\2\2RT\7\16\2\2SO\3")
        buf.write("\2\2\2SR\3\2\2\2T\25\3\2\2\2\7\31#\66LS")
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
    RULE_text = 9

    ruleNames =  [ "start", "statement", "size", "arrow", "composition", 
                   "label", "style", "impose", "path", "text" ]

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
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CDLangParser.T__0) | (1 << CDLangParser.T__5) | (1 << CDLangParser.T__6) | (1 << CDLangParser.T__7) | (1 << CDLangParser.ID) | (1 << CDLangParser.SEPARATOR))) != 0)):
                    break

            self.state = 25
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
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 27
                self.size()

            elif la_ == 2:
                self.state = 28
                self.arrow()

            elif la_ == 3:
                self.state = 29
                self.composition()

            elif la_ == 4:
                self.state = 30
                self.label()

            elif la_ == 5:
                self.state = 31
                self.style()

            elif la_ == 6:
                self.state = 32
                self.impose()


            self.state = 35
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
            self.state = 37
            self.match(CDLangParser.T__0)
            self.state = 38
            self.match(CDLangParser.MEASUREMENT)
            self.state = 39
            self.match(CDLangParser.T__1)
            self.state = 40
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CDLangParser.ID)
            else:
                return self.getToken(CDLangParser.ID, i)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(CDLangParser.ID)
            self.state = 43
            self.match(CDLangParser.T__2)
            self.state = 44
            self.match(CDLangParser.ID)
            self.state = 45
            self.match(CDLangParser.T__3)
            self.state = 46
            self.match(CDLangParser.ID)
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.path()
            self.state = 49
            self.match(CDLangParser.T__4)
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CDLangParser.ID]:
                self.state = 50
                self.path()
                pass
            elif token in [CDLangParser.IDENTITY]:
                self.state = 51
                self.match(CDLangParser.IDENTITY)
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

    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CDLangParser.ID, 0)

        def text(self):
            return self.getTypedRuleContext(CDLangParser.TextContext,0)


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
            self.state = 54
            self.match(CDLangParser.T__5)
            self.state = 55
            self.match(CDLangParser.ID)
            self.state = 56
            self.match(CDLangParser.T__2)
            self.state = 57
            self.text()
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
            self.state = 59
            self.match(CDLangParser.T__6)
            self.state = 60
            self.match(CDLangParser.ID)
            self.state = 61
            self.match(CDLangParser.T__2)
            self.state = 62
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
            self.state = 64
            self.match(CDLangParser.T__7)
            self.state = 65
            self.match(CDLangParser.ID)
            self.state = 66
            self.match(CDLangParser.T__2)
            self.state = 67
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
            self.state = 69
            self.match(CDLangParser.ID)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CDLangParser.T__8:
                self.state = 70
                self.match(CDLangParser.T__8)
                self.state = 71
                self.match(CDLangParser.ID)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(CDLangParser.TEXT, 0)

        def getRuleIndex(self):
            return CDLangParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)




    def text(self):

        localctx = CDLangParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_text)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CDLangParser.T__9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(CDLangParser.T__9)
                self.state = 78
                self.match(CDLangParser.TEXT)
                self.state = 79
                self.match(CDLangParser.T__10)
                pass
            elif token in [CDLangParser.T__11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
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





