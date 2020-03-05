# Generated from CDLang.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("Z\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\5\2\30\n\2\3\2\6\2")
        buf.write("\33\n\2\r\2\16\2\34\3\3\3\3\3\3\3\3\3\3\5\3$\n\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\63")
        buf.write("\n\5\3\6\3\6\3\6\3\6\5\69\n\6\3\6\5\6<\n\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\tK\n\t\f\t")
        buf.write("\16\tN\13\t\3\n\3\n\5\nR\n\n\3\13\3\13\3\13\3\13\5\13")
        buf.write("X\n\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\3\3\3\25\25")
        buf.write("\2[\2\27\3\2\2\2\4#\3\2\2\2\6\'\3\2\2\2\b,\3\2\2\2\n\64")
        buf.write("\3\2\2\2\f=\3\2\2\2\16B\3\2\2\2\20G\3\2\2\2\22O\3\2\2")
        buf.write("\2\24W\3\2\2\2\26\30\7\25\2\2\27\26\3\2\2\2\27\30\3\2")
        buf.write("\2\2\30\32\3\2\2\2\31\33\5\4\3\2\32\31\3\2\2\2\33\34\3")
        buf.write("\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\3\3\2\2\2\36$\5")
        buf.write("\6\4\2\37$\5\b\5\2 $\5\n\6\2!$\5\f\7\2\"$\5\16\b\2#\36")
        buf.write("\3\2\2\2#\37\3\2\2\2# \3\2\2\2#!\3\2\2\2#\"\3\2\2\2$%")
        buf.write("\3\2\2\2%&\t\2\2\2&\5\3\2\2\2\'(\7\3\2\2()\7\21\2\2)*")
        buf.write("\7\4\2\2*+\7\21\2\2+\7\3\2\2\2,-\5\22\n\2-.\7\5\2\2./")
        buf.write("\5\22\n\2/\60\7\6\2\2\60\62\5\22\n\2\61\63\7\24\2\2\62")
        buf.write("\61\3\2\2\2\62\63\3\2\2\2\63\t\3\2\2\2\64\65\5\20\t\2")
        buf.write("\658\7\7\2\2\669\5\20\t\2\679\7\20\2\28\66\3\2\2\28\67")
        buf.write("\3\2\2\29;\3\2\2\2:<\5\24\13\2;:\3\2\2\2;<\3\2\2\2<\13")
        buf.write("\3\2\2\2=>\7\b\2\2>?\7\23\2\2?@\7\5\2\2@A\5\24\13\2A\r")
        buf.write("\3\2\2\2BC\7\t\2\2CD\7\23\2\2DE\7\5\2\2EF\7\24\2\2F\17")
        buf.write("\3\2\2\2GL\7\23\2\2HI\7\n\2\2IK\7\23\2\2JH\3\2\2\2KN\3")
        buf.write("\2\2\2LJ\3\2\2\2LM\3\2\2\2M\21\3\2\2\2NL\3\2\2\2OQ\7\23")
        buf.write("\2\2PR\5\24\13\2QP\3\2\2\2QR\3\2\2\2R\23\3\2\2\2ST\7\13")
        buf.write("\2\2TU\7\16\2\2UX\7\f\2\2VX\7\r\2\2WS\3\2\2\2WV\3\2\2")
        buf.write("\2X\25\3\2\2\2\13\27\34#\628;LQW")
        return buf.getvalue()


class CDLangParser ( Parser ):

    grammarFileName = "CDLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'size'", "','", "':'", "'->'", "'='", 
                     "'label '", "'style '", "'.'", "'['", "']'", "'[]'", 
                     "<INVALID>", "<INVALID>", "'ID'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TEXT", "COMMENT", "ID", "MEASUREMENT", "NUMBER", 
                      "IDENTIFIER", "STYLE_LIST", "SEPARATOR", "WHITESPACE", 
                      "NEWLINE", "ERROR_CHAR" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_size = 2
    RULE_arrow = 3
    RULE_composition = 4
    RULE_label = 5
    RULE_style = 6
    RULE_path = 7
    RULE_labelledID = 8
    RULE_labelText = 9

    ruleNames =  [ "start", "statement", "size", "arrow", "composition", 
                   "label", "style", "path", "labelledID", "labelText" ]

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
    TEXT=12
    COMMENT=13
    ID=14
    MEASUREMENT=15
    NUMBER=16
    IDENTIFIER=17
    STYLE_LIST=18
    SEPARATOR=19
    WHITESPACE=20
    NEWLINE=21
    ERROR_CHAR=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEPARATOR(self):
            return self.getToken(CDLangParser.SEPARATOR, 0)

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
            if _la==CDLangParser.SEPARATOR:
                self.state = 20
                self.match(CDLangParser.SEPARATOR)


            self.state = 24 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 23
                self.statement()
                self.state = 26 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CDLangParser.T__0) | (1 << CDLangParser.T__5) | (1 << CDLangParser.T__6) | (1 << CDLangParser.IDENTIFIER))) != 0)):
                    break

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

        def EOF(self):
            return self.getToken(CDLangParser.EOF, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 28
                self.size()
                pass

            elif la_ == 2:
                self.state = 29
                self.arrow()
                pass

            elif la_ == 3:
                self.state = 30
                self.composition()
                pass

            elif la_ == 4:
                self.state = 31
                self.label()
                pass

            elif la_ == 5:
                self.state = 32
                self.style()
                pass


            self.state = 35
            _la = self._input.LA(1)
            if not(_la==CDLangParser.EOF or _la==CDLangParser.SEPARATOR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
            self.state = 42
            self.labelledID()
            self.state = 43
            self.match(CDLangParser.T__2)
            self.state = 44
            self.labelledID()
            self.state = 45
            self.match(CDLangParser.T__3)
            self.state = 46
            self.labelledID()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CDLangParser.STYLE_LIST:
                self.state = 47
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


        def ID(self):
            return self.getToken(CDLangParser.ID, 0)

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
            self.state = 50
            self.path()
            self.state = 51
            self.match(CDLangParser.T__4)
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CDLangParser.IDENTIFIER]:
                self.state = 52
                self.path()
                pass
            elif token in [CDLangParser.ID]:
                self.state = 53
                self.match(CDLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CDLangParser.T__8 or _la==CDLangParser.T__10:
                self.state = 56
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

        def IDENTIFIER(self):
            return self.getToken(CDLangParser.IDENTIFIER, 0)

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
            self.state = 59
            self.match(CDLangParser.T__5)
            self.state = 60
            self.match(CDLangParser.IDENTIFIER)
            self.state = 61
            self.match(CDLangParser.T__2)
            self.state = 62
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

        def IDENTIFIER(self):
            return self.getToken(CDLangParser.IDENTIFIER, 0)

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
            self.state = 64
            self.match(CDLangParser.T__6)
            self.state = 65
            self.match(CDLangParser.IDENTIFIER)
            self.state = 66
            self.match(CDLangParser.T__2)
            self.state = 67
            self.match(CDLangParser.STYLE_LIST)
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(CDLangParser.IDENTIFIER)
            else:
                return self.getToken(CDLangParser.IDENTIFIER, i)

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
        self.enterRule(localctx, 14, self.RULE_path)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(CDLangParser.IDENTIFIER)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CDLangParser.T__7:
                self.state = 70
                self.match(CDLangParser.T__7)
                self.state = 71
                self.match(CDLangParser.IDENTIFIER)
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

    class LabelledIDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CDLangParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 16, self.RULE_labelledID)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(CDLangParser.IDENTIFIER)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CDLangParser.T__8 or _la==CDLangParser.T__10:
                self.state = 78
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
        self.enterRule(localctx, 18, self.RULE_labelText)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CDLangParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(CDLangParser.T__8)
                self.state = 82
                self.match(CDLangParser.TEXT)
                self.state = 83
                self.match(CDLangParser.T__9)
                pass
            elif token in [CDLangParser.T__10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(CDLangParser.T__10)
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





