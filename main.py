from antlr4 import *
from ToyPythonLexer import ToyPythonLexer
from ToyPythonParser import ToyPythonParser
import sys

def preprocess_indentation(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    processed_lines = []
    indent_stack = [0]  # To track indentation levels

    for line in lines:
        stripped = line.lstrip()
        indent_level = len(line) - len(stripped)

        if stripped == "" or stripped.startswith("#"):  # Skip empty lines or comments
            processed_lines.append(line)
            continue

        if indent_level > indent_stack[-1]:
            indent_stack.append(indent_level)
            processed_lines.append("<INDENT>\n")
        elif indent_level < indent_stack[-1]:
            while indent_level < indent_stack[-1]:
                indent_stack.pop()
                processed_lines.append("<DEDENT>\n")

        processed_lines.append(line)

    while len(indent_stack) > 1:  # Close remaining indents
        indent_stack.pop()
        processed_lines.append("<DEDENT>\n")

    return processed_lines

def main():
    # Check if the user provided an input file
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    # Get the path to the input file
    file_path = sys.argv[1]

    try:
        # Preprocess the file for indentation
        processed_lines = preprocess_indentation(file_path)
        with open("processed_example.toy", "w") as f:
            f.writelines(processed_lines)

        # Read the preprocessed input file
        input_stream = FileStream("processed_example.toy")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    # Initialize the lexer and parser
    lexer = ToyPythonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ToyPythonParser(stream)

    # Parse the input file
    try:
        tree = parser.program()
        print("Parsed successfully!")
        print("Parse Tree:")
        print(tree.toStringTree(recog=parser))  # Print the parse tree
    except Exception as e:
        print(f"Error during parsing: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()