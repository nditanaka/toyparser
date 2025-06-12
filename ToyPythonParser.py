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
        4,1,24,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,4,0,21,8,0,11,0,12,0,22,1,0,1,0,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        3,3,44,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,53,8,4,11,4,12,4,54,1,
        4,1,4,1,5,1,5,1,5,3,5,62,8,5,1,6,1,6,1,6,5,6,67,8,6,10,6,12,6,70,
        9,6,1,7,1,7,1,7,5,7,75,8,7,10,7,12,7,78,9,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,3,8,87,8,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,3,1,0,7,12,
        1,0,13,14,1,0,15,16,91,0,20,1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,6,
        43,1,0,0,0,8,45,1,0,0,0,10,58,1,0,0,0,12,63,1,0,0,0,14,71,1,0,0,
        0,16,86,1,0,0,0,18,21,3,2,1,0,19,21,3,4,2,0,20,18,1,0,0,0,20,19,
        1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,24,1,0,0,0,
        24,25,5,0,0,1,25,1,1,0,0,0,26,29,3,6,3,0,27,29,3,8,4,0,28,26,1,0,
        0,0,28,27,1,0,0,0,29,3,1,0,0,0,30,31,5,17,0,0,31,5,1,0,0,0,32,33,
        5,1,0,0,33,34,5,2,0,0,34,35,3,12,6,0,35,36,5,3,0,0,36,37,5,17,0,
        0,37,44,1,0,0,0,38,39,5,22,0,0,39,40,5,4,0,0,40,41,3,12,6,0,41,42,
        5,17,0,0,42,44,1,0,0,0,43,32,1,0,0,0,43,38,1,0,0,0,44,7,1,0,0,0,
        45,46,5,5,0,0,46,47,3,10,5,0,47,48,5,6,0,0,48,49,5,17,0,0,49,52,
        5,18,0,0,50,53,3,2,1,0,51,53,3,4,2,0,52,50,1,0,0,0,52,51,1,0,0,0,
        53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,56,1,0,0,0,56,57,5,
        19,0,0,57,9,1,0,0,0,58,61,3,12,6,0,59,60,7,0,0,0,60,62,3,12,6,0,
        61,59,1,0,0,0,61,62,1,0,0,0,62,11,1,0,0,0,63,68,3,14,7,0,64,65,7,
        1,0,0,65,67,3,14,7,0,66,64,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,
        69,1,0,0,0,69,13,1,0,0,0,70,68,1,0,0,0,71,76,3,16,8,0,72,73,7,2,
        0,0,73,75,3,16,8,0,74,72,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,
        77,1,0,0,0,77,15,1,0,0,0,78,76,1,0,0,0,79,87,5,20,0,0,80,87,5,21,
        0,0,81,87,5,22,0,0,82,83,5,2,0,0,83,84,3,12,6,0,84,85,5,3,0,0,85,
        87,1,0,0,0,86,79,1,0,0,0,86,80,1,0,0,0,86,81,1,0,0,0,86,82,1,0,0,
        0,87,17,1,0,0,0,10,20,22,28,43,52,54,61,68,76,86
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
    RULE_emptyStatement = 2
    RULE_simpleStatement = 3
    RULE_compoundStatement = 4
    RULE_comparison = 5
    RULE_expression = 6
    RULE_term = 7
    RULE_factor = 8

    ruleNames =  [ "program", "statement", "emptyStatement", "simpleStatement", 
                   "compoundStatement", "comparison", "expression", "term", 
                   "factor" ]

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


        def emptyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyPythonParser.EmptyStatementContext)
            else:
                return self.getTypedRuleContext(ToyPythonParser.EmptyStatementContext,i)


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
            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 5, 22]:
                    self.state = 18
                    self.statement()
                    pass
                elif token in [17]:
                    self.state = 19
                    self.emptyStatement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4325410) != 0)):
                    break

            self.state = 24
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
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.simpleStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
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


    class EmptyStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ToyPythonParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ToyPythonParser.RULE_emptyStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)




    def emptyStatement(self):

        localctx = ToyPythonParser.EmptyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_emptyStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(ToyPythonParser.NEWLINE)
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
        self.enterRule(localctx, 6, self.RULE_simpleStatement)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(ToyPythonParser.T__0)
                self.state = 33
                self.match(ToyPythonParser.T__1)
                self.state = 34
                self.expression()
                self.state = 35
                self.match(ToyPythonParser.T__2)
                self.state = 36
                self.match(ToyPythonParser.NEWLINE)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(ToyPythonParser.IDENTIFIER)
                self.state = 39
                self.match(ToyPythonParser.T__3)
                self.state = 40
                self.expression()
                self.state = 41
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


        def emptyStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ToyPythonParser.EmptyStatementContext)
            else:
                return self.getTypedRuleContext(ToyPythonParser.EmptyStatementContext,i)


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
        self.enterRule(localctx, 8, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(ToyPythonParser.T__4)
            self.state = 46
            self.comparison()
            self.state = 47
            self.match(ToyPythonParser.T__5)
            self.state = 48
            self.match(ToyPythonParser.NEWLINE)
            self.state = 49
            self.match(ToyPythonParser.INDENT)
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 52
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 5, 22]:
                    self.state = 50
                    self.statement()
                    pass
                elif token in [17]:
                    self.state = 51
                    self.emptyStatement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4325410) != 0)):
                    break

            self.state = 56
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
        self.enterRule(localctx, 10, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.expression()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8064) != 0):
                self.state = 59
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8064) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 60
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
        self.enterRule(localctx, 12, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.term()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 64
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 65
                self.term()
                self.state = 70
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
        self.enterRule(localctx, 14, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.factor()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 72
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 73
                self.factor()
                self.state = 78
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
        self.enterRule(localctx, 16, self.RULE_factor)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(ToyPythonParser.NUMBER)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(ToyPythonParser.STRING)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.match(ToyPythonParser.IDENTIFIER)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.match(ToyPythonParser.T__1)
                self.state = 83
                self.expression()
                self.state = 84
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





