# Generated from CDLang.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\7\2\30\n\2\f\2\16\2")
        buf.write("\33\13\2\3\2\6\2\36\n\2\r\2\16\2\37\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\'\n\3\3\3\6\3*\n\3\r\3\16\3+\3\3\5\3/\n\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5<\n\5\3\6\3")
        buf.write("\6\3\6\3\6\5\6B\n\6\3\6\5\6E\n\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\tT\n\t\f\t\16\tW\13\t")
        buf.write("\3\n\3\n\5\n[\n\n\3\13\3\13\3\13\3\13\5\13a\n\13\3\13")
        buf.write("\2\2\f\2\4\6\b\n\f\16\20\22\24\2\2\2f\2\31\3\2\2\2\4&")
        buf.write("\3\2\2\2\6\60\3\2\2\2\b\65\3\2\2\2\n=\3\2\2\2\fF\3\2\2")
        buf.write("\2\16K\3\2\2\2\20P\3\2\2\2\22X\3\2\2\2\24`\3\2\2\2\26")
        buf.write("\30\7\24\2\2\27\26\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2")
        buf.write("\31\32\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\34\36\5\4\3")
        buf.write("\2\35\34\3\2\2\2\36\37\3\2\2\2\37\35\3\2\2\2\37 \3\2\2")
        buf.write("\2 \3\3\2\2\2!\'\5\6\4\2\"\'\5\b\5\2#\'\5\n\6\2$\'\5\f")
        buf.write("\7\2%\'\5\16\b\2&!\3\2\2\2&\"\3\2\2\2&#\3\2\2\2&$\3\2")
        buf.write("\2\2&%\3\2\2\2\'.\3\2\2\2(*\7\24\2\2)(\3\2\2\2*+\3\2\2")
        buf.write("\2+)\3\2\2\2+,\3\2\2\2,/\3\2\2\2-/\7\2\2\3.)\3\2\2\2.")
        buf.write("-\3\2\2\2/\5\3\2\2\2\60\61\7\3\2\2\61\62\7\21\2\2\62\63")
        buf.write("\7\4\2\2\63\64\7\21\2\2\64\7\3\2\2\2\65\66\5\22\n\2\66")
        buf.write("\67\7\5\2\2\678\5\22\n\289\7\6\2\29;\5\22\n\2:<\7\23\2")
        buf.write("\2;:\3\2\2\2;<\3\2\2\2<\t\3\2\2\2=>\5\20\t\2>A\7\7\2\2")
        buf.write("?B\5\20\t\2@B\7\20\2\2A?\3\2\2\2A@\3\2\2\2BD\3\2\2\2C")
        buf.write("E\5\24\13\2DC\3\2\2\2DE\3\2\2\2E\13\3\2\2\2FG\7\b\2\2")
        buf.write("GH\7\22\2\2HI\7\5\2\2IJ\5\24\13\2J\r\3\2\2\2KL\7\t\2\2")
        buf.write("LM\7\22\2\2MN\7\5\2\2NO\7\23\2\2O\17\3\2\2\2PU\7\22\2")
        buf.write("\2QR\7\n\2\2RT\7\22\2\2SQ\3\2\2\2TW\3\2\2\2US\3\2\2\2")
        buf.write("UV\3\2\2\2V\21\3\2\2\2WU\3\2\2\2XZ\7\22\2\2Y[\5\24\13")
        buf.write("\2ZY\3\2\2\2Z[\3\2\2\2[\23\3\2\2\2\\]\7\13\2\2]^\7\16")
        buf.write("\2\2^a\7\f\2\2_a\7\r\2\2`\\\3\2\2\2`_\3\2\2\2a\25\3\2")
        buf.write("\2\2\r\31\37&+.;ADUZ`")
        return buf.getvalue()


class CDLangParser ( Parser ):

    grammarFileName = "CDLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'size'", "','", "':'", "'->'", "'='", 
                     "'label'", "'style'", "'.'", "'['", "']'", "'[]'", 
                     "<INVALID>", "<INVALID>", "'ID'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TEXT", "COMMENT", "ID", "NUMBER", "IDENTIFIER", "STYLE_LIST", 
                      "SEPARATOR", "WHITESPACE", "NEWLINE", "ERROR_CHAR" ]

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
    NUMBER=15
    IDENTIFIER=16
    STYLE_LIST=17
    SEPARATOR=18
    WHITESPACE=19
    NEWLINE=20
    ERROR_CHAR=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(CDLangParser.SEPARATOR)
            else:
                return self.getToken(CDLangParser.SEPARATOR, i)

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
            while _la==CDLangParser.SEPARATOR:
                self.state = 20
                self.match(CDLangParser.SEPARATOR)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.statement()
                self.state = 29 
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


        def EOF(self):
            return self.getToken(CDLangParser.EOF, 0)

        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(CDLangParser.SEPARATOR)
            else:
                return self.getToken(CDLangParser.SEPARATOR, i)

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
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 31
                self.size()
                pass

            elif la_ == 2:
                self.state = 32
                self.arrow()
                pass

            elif la_ == 3:
                self.state = 33
                self.composition()
                pass

            elif la_ == 4:
                self.state = 34
                self.label()
                pass

            elif la_ == 5:
                self.state = 35
                self.style()
                pass


            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CDLangParser.SEPARATOR]:
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 38
                    self.match(CDLangParser.SEPARATOR)
                    self.state = 41 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==CDLangParser.SEPARATOR):
                        break

                pass
            elif token in [CDLangParser.EOF]:
                self.state = 43
                self.match(CDLangParser.EOF)
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

    class SizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(CDLangParser.NUMBER)
            else:
                return self.getToken(CDLangParser.NUMBER, i)

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
            self.state = 46
            self.match(CDLangParser.T__0)
            self.state = 47
            self.match(CDLangParser.NUMBER)
            self.state = 48
            self.match(CDLangParser.T__1)
            self.state = 49
            self.match(CDLangParser.NUMBER)
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
            self.state = 51
            self.labelledID()
            self.state = 52
            self.match(CDLangParser.T__2)
            self.state = 53
            self.labelledID()
            self.state = 54
            self.match(CDLangParser.T__3)
            self.state = 55
            self.labelledID()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CDLangParser.STYLE_LIST:
                self.state = 56
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
            self.state = 59
            self.path()
            self.state = 60
            self.match(CDLangParser.T__4)
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CDLangParser.IDENTIFIER]:
                self.state = 61
                self.path()
                pass
            elif token in [CDLangParser.ID]:
                self.state = 62
                self.match(CDLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CDLangParser.T__8 or _la==CDLangParser.T__10:
                self.state = 65
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
            self.state = 68
            self.match(CDLangParser.T__5)
            self.state = 69
            self.match(CDLangParser.IDENTIFIER)
            self.state = 70
            self.match(CDLangParser.T__2)
            self.state = 71
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
            self.state = 73
            self.match(CDLangParser.T__6)
            self.state = 74
            self.match(CDLangParser.IDENTIFIER)
            self.state = 75
            self.match(CDLangParser.T__2)
            self.state = 76
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
            self.state = 78
            self.match(CDLangParser.IDENTIFIER)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CDLangParser.T__7:
                self.state = 79
                self.match(CDLangParser.T__7)
                self.state = 80
                self.match(CDLangParser.IDENTIFIER)
                self.state = 85
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
            self.state = 86
            self.match(CDLangParser.IDENTIFIER)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CDLangParser.T__8 or _la==CDLangParser.T__10:
                self.state = 87
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
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CDLangParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.match(CDLangParser.T__8)
                self.state = 91
                self.match(CDLangParser.TEXT)
                self.state = 92
                self.match(CDLangParser.T__9)
                pass
            elif token in [CDLangParser.T__10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
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





