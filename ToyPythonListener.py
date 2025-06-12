# Generated from ToyPython.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ToyPythonParser import ToyPythonParser
else:
    from ToyPythonParser import ToyPythonParser

# This class defines a complete listener for a parse tree produced by ToyPythonParser.
class ToyPythonListener(ParseTreeListener):

    # Enter a parse tree produced by ToyPythonParser#program.
    def enterProgram(self, ctx:ToyPythonParser.ProgramContext):
        pass

    # Exit a parse tree produced by ToyPythonParser#program.
    def exitProgram(self, ctx:ToyPythonParser.ProgramContext):
        pass


    # Enter a parse tree produced by ToyPythonParser#statement.
    def enterStatement(self, ctx:ToyPythonParser.StatementContext):
        pass

    # Exit a parse tree produced by ToyPythonParser#statement.
    def exitStatement(self, ctx:ToyPythonParser.StatementContext):
        pass


    # Enter a parse tree produced by ToyPythonParser#emptyStatement.
    def enterEmptyStatement(self, ctx:ToyPythonParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by ToyPythonParser#emptyStatement.
    def exitEmptyStatement(self, ctx:ToyPythonParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by ToyPythonParser#simpleStatement.
    def enterSimpleStatement(self, ctx:ToyPythonParser.SimpleStatementContext):
        pass

    # Exit a parse tree produced by ToyPythonParser#simpleStatement.
    def exitSimpleStatement(self, ctx:ToyPythonParser.SimpleStatementContext):
        pass


    # Enter a parse tree produced by ToyPythonParser#compoundStatement.
    def enterCompoundStatement(self, ctx:ToyPythonParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by ToyPythonParser#compoundStatement.
    def exitCompoundStatement(self, ctx:ToyPythonParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by ToyPythonParser#comparison.
    def enterComparison(self, ctx:ToyPythonParser.ComparisonContext):
        pass

    # Exit a parse tree produced by ToyPythonParser#comparison.
    def exitComparison(self, ctx:ToyPythonParser.ComparisonContext):
        pass


    # Enter a parse tree produced by ToyPythonParser#expression.
    def enterExpression(self, ctx:ToyPythonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ToyPythonParser#expression.
    def exitExpression(self, ctx:ToyPythonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ToyPythonParser#term.
    def enterTerm(self, ctx:ToyPythonParser.TermContext):
        pass

    # Exit a parse tree produced by ToyPythonParser#term.
    def exitTerm(self, ctx:ToyPythonParser.TermContext):
        pass


    # Enter a parse tree produced by ToyPythonParser#factor.
    def enterFactor(self, ctx:ToyPythonParser.FactorContext):
        pass

    # Exit a parse tree produced by ToyPythonParser#factor.
    def exitFactor(self, ctx:ToyPythonParser.FactorContext):
        pass



del ToyPythonParser