# Generated from CDLang.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("J\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3\37\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t?\n\t\f\t\16")
        buf.write("\tB\13\t\3\n\3\n\3\n\3\n\5\nH\n\n\3\n\2\2\13\2\4\6\b\n")
        buf.write("\f\16\20\22\2\3\3\3\20\20\2G\2\25\3\2\2\2\4\36\3\2\2\2")
        buf.write("\6\"\3\2\2\2\b(\3\2\2\2\n,\3\2\2\2\f\61\3\2\2\2\16\66")
        buf.write("\3\2\2\2\20;\3\2\2\2\22G\3\2\2\2\24\26\5\4\3\2\25\24\3")
        buf.write("\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\3")
        buf.write("\3\2\2\2\31\37\5\6\4\2\32\37\5\b\5\2\33\37\5\n\6\2\34")
        buf.write("\37\5\f\7\2\35\37\5\16\b\2\36\31\3\2\2\2\36\32\3\2\2\2")
        buf.write("\36\33\3\2\2\2\36\34\3\2\2\2\36\35\3\2\2\2\37 \3\2\2\2")
        buf.write(" !\t\2\2\2!\5\3\2\2\2\"#\7\17\2\2#$\7\3\2\2$%\7\17\2\2")
        buf.write("%&\7\4\2\2&\'\7\17\2\2\'\7\3\2\2\2()\5\20\t\2)*\7\5\2")
        buf.write("\2*+\5\20\t\2+\t\3\2\2\2,-\7\6\2\2-.\7\17\2\2./\7\3\2")
        buf.write("\2/\60\5\22\n\2\60\13\3\2\2\2\61\62\7\7\2\2\62\63\7\17")
        buf.write("\2\2\63\64\7\3\2\2\64\65\5\22\n\2\65\r\3\2\2\2\66\67\7")
        buf.write("\b\2\2\678\7\17\2\289\7\3\2\29:\7\16\2\2:\17\3\2\2\2;")
        buf.write("@\7\17\2\2<=\7\t\2\2=?\7\17\2\2><\3\2\2\2?B\3\2\2\2@>")
        buf.write("\3\2\2\2@A\3\2\2\2A\21\3\2\2\2B@\3\2\2\2CD\7\n\2\2DE\7")
        buf.write("\r\2\2EH\7\13\2\2FH\7\f\2\2GC\3\2\2\2GF\3\2\2\2H\23\3")
        buf.write("\2\2\2\6\27\36@G")
        return buf.getvalue()


class CDLangParser ( Parser ):

    grammarFileName = "CDLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'->'", "'='", "'label'", "'style'", 
                     "'impose'", "'.'", "'('", "')'", "'()'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TEXT", "DIRECTION", 
                      "ID", "SEPARATOR", "WHITESPACE", "NEWLINE" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_arrow = 2
    RULE_composition = 3
    RULE_label = 4
    RULE_style = 5
    RULE_impose = 6
    RULE_path = 7
    RULE_text = 8

    ruleNames =  [ "start", "statement", "arrow", "composition", "label", 
                   "style", "impose", "path", "text" ]

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
    TEXT=11
    DIRECTION=12
    ID=13
    SEPARATOR=14
    WHITESPACE=15
    NEWLINE=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CDLangParser.T__3) | (1 << CDLangParser.T__4) | (1 << CDLangParser.T__5) | (1 << CDLangParser.ID))) != 0)):
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 23
                self.arrow()
                pass

            elif la_ == 2:
                self.state = 24
                self.composition()
                pass

            elif la_ == 3:
                self.state = 25
                self.label()
                pass

            elif la_ == 4:
                self.state = 26
                self.style()
                pass

            elif la_ == 5:
                self.state = 27
                self.impose()
                pass


            self.state = 30
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
        self.enterRule(localctx, 4, self.RULE_arrow)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(CDLangParser.ID)
            self.state = 33
            self.match(CDLangParser.T__0)
            self.state = 34
            self.match(CDLangParser.ID)
            self.state = 35
            self.match(CDLangParser.T__1)
            self.state = 36
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
        self.enterRule(localctx, 6, self.RULE_composition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.path()
            self.state = 39
            self.match(CDLangParser.T__2)
            self.state = 40
            self.path()
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
        self.enterRule(localctx, 8, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(CDLangParser.T__3)
            self.state = 43
            self.match(CDLangParser.ID)
            self.state = 44
            self.match(CDLangParser.T__0)
            self.state = 45
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

        def text(self):
            return self.getTypedRuleContext(CDLangParser.TextContext,0)


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
        self.enterRule(localctx, 10, self.RULE_style)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(CDLangParser.T__4)
            self.state = 48
            self.match(CDLangParser.ID)
            self.state = 49
            self.match(CDLangParser.T__0)
            self.state = 50
            self.text()
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
        self.enterRule(localctx, 12, self.RULE_impose)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(CDLangParser.T__5)
            self.state = 53
            self.match(CDLangParser.ID)
            self.state = 54
            self.match(CDLangParser.T__0)
            self.state = 55
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
        self.enterRule(localctx, 14, self.RULE_path)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(CDLangParser.ID)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CDLangParser.T__6:
                self.state = 58
                self.match(CDLangParser.T__6)
                self.state = 59
                self.match(CDLangParser.ID)
                self.state = 64
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
        self.enterRule(localctx, 16, self.RULE_text)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CDLangParser.T__7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.match(CDLangParser.T__7)
                self.state = 66
                self.match(CDLangParser.TEXT)
                self.state = 67
                self.match(CDLangParser.T__8)
                pass
            elif token in [CDLangParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(CDLangParser.T__9)
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





