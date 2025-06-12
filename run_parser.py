from antlr4 import FileStream, CommonTokenStream
from ToyPythonParser import ToyPythonParser
from ToyPythonLexer import ToyPythonLexer
from ToyPythonListener import ToyPythonListener

def main():
    input_stream = FileStream("example.toy")
    lexer = ToyPythonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ToyPythonParser(stream)
    tree = parser.program()

    listener = ToyPythonListener()
    # Walk the tree (optional, if you want to process events)
    from antlr4 import ParseTreeWalker
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == "__main__":
    main()