# Generated from ToyPython.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,83,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,3,1,26,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,39,8,2,1,3,1,3,1,
        3,1,3,1,3,1,3,4,3,47,8,3,11,3,12,3,48,1,3,1,3,1,4,1,4,1,4,3,4,56,
        8,4,1,5,1,5,1,5,5,5,61,8,5,10,5,12,5,64,9,5,1,6,1,6,1,6,5,6,69,8,
        6,10,6,12,6,72,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,81,8,7,1,7,0,
        0,8,0,2,4,6,8,10,12,14,0,3,1,0,7,12,1,0,13,14,1,0,15,16,84,0,17,
        1,0,0,0,2,25,1,0,0,0,4,38,1,0,0,0,6,40,1,0,0,0,8,52,1,0,0,0,10,57,
        1,0,0,0,12,65,1,0,0,0,14,80,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,
        18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,22,5,
        0,0,1,22,1,1,0,0,0,23,26,3,4,2,0,24,26,3,6,3,0,25,23,1,0,0,0,25,
        24,1,0,0,0,26,3,1,0,0,0,27,28,5,1,0,0,28,29,5,2,0,0,29,30,3,10,5,
        0,30,31,5,3,0,0,31,32,5,17,0,0,32,39,1,0,0,0,33,34,5,22,0,0,34,35,
        5,4,0,0,35,36,3,10,5,0,36,37,5,17,0,0,37,39,1,0,0,0,38,27,1,0,0,
        0,38,33,1,0,0,0,39,5,1,0,0,0,40,41,5,5,0,0,41,42,3,8,4,0,42,43,5,
        6,0,0,43,44,5,17,0,0,44,46,5,18,0,0,45,47,3,2,1,0,46,45,1,0,0,0,
        47,48,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,50,51,5,
        19,0,0,51,7,1,0,0,0,52,55,3,10,5,0,53,54,7,0,0,0,54,56,3,10,5,0,
        55,53,1,0,0,0,55,56,1,0,0,0,56,9,1,0,0,0,57,62,3,12,6,0,58,59,7,
        1,0,0,59,61,3,12,6,0,60,58,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,
        63,1,0,0,0,63,11,1,0,0,0,64,62,1,0,0,0,65,70,3,14,7,0,66,67,7,2,
        0,0,67,69,3,14,7,0,68,66,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,
        71,1,0,0,0,71,13,1,0,0,0,72,70,1,0,0,0,73,81,5,20,0,0,74,81,5,21,
        0,0,75,81,5,22,0,0,76,77,5,2,0,0,77,78,3,10,5,0,78,79,5,3,0,0,79,
        81,1,0,0,0,80,73,1,0,0,0,80,74,1,0,0,0,80,75,1,0,0,0,80,76,1,0,0,
        0,81,15,1,0,0,0,8,19,25,38,48,55,62,70,80
    ]

class ToyPythonParser ( Parser ):

    grammarFileName = "ToyPython.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'('", "')'", "'='", "'if'", 
                     "':'", "'<'", "'>'", "'=='", "'!='", "'<='", "'>='", 
                     "'+'", "'-'", "'*'", "'/'", "<INVALID>", "'<INDENT>'", 
                     "'<DEDENT>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NEWLINE", "INDENT", "DEDENT", "NUMBER", 
                      "STRING", "IDENTIFIER", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_simpleStatement = 2
    RULE_compoundStatement = 3
    RULE_comparison = 4
    RULE_expression = 5
    RULE_term = 6
    RULE_factor = 7

    ruleNames =  [ "program", "statement", "simpleStatement", "compoundStatement", 
                   "comparison", "expression", "term", "factor" ]

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
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    NEWLINE=17
    INDENT=18
    DEDENT=19
    NUMBER=20
    STRING=21
    IDENTIFIER=22
    WS=23
    COMMENT=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ToyPythonParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyPythonParser.StatementContext)
            else:
                return self.getTypedRuleContext(ToyPythonParser.StatementContext,i)


        def getRuleIndex(self):
            return ToyPythonParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ToyPythonParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.statement()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4194338) != 0)):
                    break

            self.state = 21
            self.match(ToyPythonParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleStatement(self):
            return self.getTypedRuleContext(ToyPythonParser.SimpleStatementContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(ToyPythonParser.CompoundStatementContext,0)


        def getRuleIndex(self):
            return ToyPythonParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ToyPythonParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.simpleStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.compoundStatement()
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


    class SimpleStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ToyPythonParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(ToyPythonParser.NEWLINE, 0)

        def IDENTIFIER(self):
            return self.getToken(ToyPythonParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ToyPythonParser.RULE_simpleStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleStatement" ):
                listener.enterSimpleStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleStatement" ):
                listener.exitSimpleStatement(self)




    def simpleStatement(self):

        localctx = ToyPythonParser.SimpleStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simpleStatement)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(ToyPythonParser.T__0)
                self.state = 28
                self.match(ToyPythonParser.T__1)
                self.state = 29
                self.expression()
                self.state = 30
                self.match(ToyPythonParser.T__2)
                self.state = 31
                self.match(ToyPythonParser.NEWLINE)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(ToyPythonParser.IDENTIFIER)
                self.state = 34
                self.match(ToyPythonParser.T__3)
                self.state = 35
                self.expression()
                self.state = 36
                self.match(ToyPythonParser.NEWLINE)
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


    class CompoundStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(ToyPythonParser.ComparisonContext,0)


        def NEWLINE(self):
            return self.getToken(ToyPythonParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(ToyPythonParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(ToyPythonParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyPythonParser.StatementContext)
            else:
                return self.getTypedRuleContext(ToyPythonParser.StatementContext,i)


        def getRuleIndex(self):
            return ToyPythonParser.RULE_compoundStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundStatement" ):
                listener.enterCompoundStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundStatement" ):
                listener.exitCompoundStatement(self)




    def compoundStatement(self):

        localctx = ToyPythonParser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(ToyPythonParser.T__4)
            self.state = 41
            self.comparison()
            self.state = 42
            self.match(ToyPythonParser.T__5)
            self.state = 43
            self.match(ToyPythonParser.NEWLINE)
            self.state = 44
            self.match(ToyPythonParser.INDENT)
            self.state = 46 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                self.statement()
                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4194338) != 0)):
                    break

            self.state = 50
            self.match(ToyPythonParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyPythonParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ToyPythonParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ToyPythonParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = ToyPythonParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.expression()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8064) != 0):
                self.state = 53
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8064) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 54
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyPythonParser.TermContext)
            else:
                return self.getTypedRuleContext(ToyPythonParser.TermContext,i)


        def getRuleIndex(self):
            return ToyPythonParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = ToyPythonParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.term()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 58
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 59
                self.term()
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


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyPythonParser.FactorContext)
            else:
                return self.getTypedRuleContext(ToyPythonParser.FactorContext,i)


        def getRuleIndex(self):
            return ToyPythonParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = ToyPythonParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.factor()
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 66
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 67
                self.factor()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ToyPythonParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ToyPythonParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(ToyPythonParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(ToyPythonParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ToyPythonParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = ToyPythonParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_factor)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(ToyPythonParser.NUMBER)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(ToyPythonParser.STRING)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.match(ToyPythonParser.IDENTIFIER)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.match(ToyPythonParser.T__1)
                self.state = 77
                self.expression()
                self.state = 78
                self.match(ToyPythonParser.T__2)
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





