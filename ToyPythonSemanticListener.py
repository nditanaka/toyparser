from ToyPythonParser import ToyPythonParser
from ToyPythonListener import ToyPythonListener

class ToyPythonSemanticListener(ToyPythonListener):
    def __init__(self):
        self.variables = {}
        # Stack to control if we are in a True if-block (for nested if)
        self.if_execution_stack = [True]

    def exitSimpleStatement(self, ctx:ToyPythonParser.SimpleStatementContext):
        # Only execute if all enclosing if-blocks are active
        if not all(self.if_execution_stack):
            return

        # Assignment: IDENTIFIER '=' expression NEWLINE (childCount == 4)
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == "=":
            var_name = ctx.getChild(0).getText()
            value = self._eval_expression(ctx.getChild(2))
            self.variables[var_name] = value
        # Print: 'print' '(' expression ')' NEWLINE (childCount == 5)
        elif ctx.getChild(0).getText() == "print":
            expr_ctx = ctx.getChild(2)
            value = self._eval_expression(expr_ctx)
            print(value)

    def enterCompoundStatement(self, ctx:ToyPythonParser.CompoundStatementContext):
        # Only handle 'if' statements
        if ctx.getChild(0).getText() == "if":
            # Evaluate the comparison (second child)
            should_execute = self._eval_comparison(ctx.comparison())
            # Only execute this block if parent context is True AND condition is True
            self.if_execution_stack.append(all(self.if_execution_stack) and should_execute)

    def exitCompoundStatement(self, ctx:ToyPythonParser.CompoundStatementContext):
        if ctx.getChild(0).getText() == "if":
            self.if_execution_stack.pop()

    def _eval_comparison(self, ctx):
        # comparison: expression (('<' | '>' | '==' | '!=' | '<=' | '>=') expression)?
        left = self._eval_expression(ctx.expression(0))
        if ctx.getChildCount() == 1:
            # Just an expression (e.g., if x:)
            return bool(left)
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            right = self._eval_expression(ctx.expression(1))
            if op == ">":
                return left > right
            elif op == "<":
                return left < right
            elif op == "==":
                return left == right
            elif op == "!=":
                return left != right
            elif op == ">=":
                return left >= right
            elif op == "<=":
                return left <= right
        return False

    def _eval_expression(self, ctx):
        # expression: term (('+' | '-') term)*
        result = self._eval_term(ctx.term(0))
        n = ctx.getChildCount()
        i = 1
        while i < n:
            op = ctx.getChild(i).getText()
            right = self._eval_term(ctx.term((i+1)//2))
            if op == "+":
                result = result + right
            elif op == "-":
                result = result - right
            i += 2
        return result

    def _eval_term(self, ctx):
        # term: factor (('*' | '/') factor)*
        result = self._eval_factor(ctx.factor(0))
        n = ctx.getChildCount()
        i = 1
        while i < n:
            op = ctx.getChild(i).getText()
            right = self._eval_factor(ctx.factor((i+1)//2))
            if op == "*":
                result = result * right
            elif op == "/":
                result = result / right
            i += 2
        return result

    def _eval_factor(self, ctx):
        # factor: NUMBER | STRING | IDENTIFIER | '(' expression ')'
        if hasattr(ctx, 'NUMBER') and ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        if hasattr(ctx, 'STRING') and ctx.STRING():
            text = ctx.STRING().getText()
            return text[1:-1]
        if hasattr(ctx, 'IDENTIFIER') and ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            return self.variables.get(var_name, 0)
        # (expression)
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            return self._eval_expression(ctx.expression())
        # If it's just a factor (recursion for ambiguity)
        if ctx.getChildCount() == 1:
            return self._eval_factor(ctx.getChild(0))
        return 0