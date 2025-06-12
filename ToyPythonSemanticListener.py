from ToyPythonParser import ToyPythonParser
from ToyPythonListener import ToyPythonListener

class ToyPythonSemanticListener(ToyPythonListener):
    def __init__(self):
        self.variables = {}

    def exitSimpleStatement(self, ctx:ToyPythonParser.SimpleStatementContext):
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

    def _eval_expression(self, ctx):
        # If it's a number
        if hasattr(ctx, 'NUMBER') and ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        # If it's a string
        if hasattr(ctx, 'STRING') and ctx.STRING():
            text = ctx.STRING().getText()
            return text[1:-1]
        # If it's a variable/identifier
        if hasattr(ctx, 'IDENTIFIER') and ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            # Return the variable value or the name if not found
            return self.variables.get(var_name, var_name)
        # Otherwise, handle nested children (e.g., expression/term/factor structure)
        if ctx.getChildCount() == 1:
            return self._eval_expression(ctx.getChild(0))
        # If it's more complex (e.g., arithmetic, which you can extend here)
        # For now, just return the text
        return ctx.getText()