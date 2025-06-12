# ToyPython Parser

ToyPython is a minimal Python-like interpreter built with [ANTLR4](https://www.antlr.org/) and Python. It parses and interprets a small subset of Python syntax, including assignments, print statements, arithmetic, and if-blocks with indentation.

---

## What’s Included

- **ToyPython.g4** – The main ANTLR grammar for the language.
- **ToyPythonLexer.py / ToyPythonParser.py / ToyPythonListener.py** – ANTLR-generated Python files (do not edit).
- **ToyPythonSemanticListener.py** – Custom Python code for interpreting your ToyPython code.
- **main.py** – Preprocesses input for indentation, runs the parser, and executes the code.
- **example.toy** – An example ToyPython program.

---

## How It Works

1. **Parsing:**  
   The grammar covers basic statements (assignment, print, if), simple expressions, and blocks using indentation.
2. **Indentation:**  
   Python-like indentation is supported by preprocessing source code and custom lexer tweaks.
3. **Interpreting:**  
   The `ToyPythonSemanticListener.py` walks the parse tree and actually runs the code (e.g., does assignments, prints values).

---

## Running It

1. Make sure you have Python 3 and install the ANTLR runtime:

   ```sh
   pip install antlr4-python3-runtime
   ```

2. (Only if you edit `ToyPython.g4`) Regenerate parser files:

   ```sh
   antlr4 -Dlanguage=Python3 ToyPython.g4
   ```

3. Run the example:

   ```sh
   python main.py example.toy
   ```

   This will output the parse tree and interpret the program.

---

## Example ToyPython Code

```
x = 5
if x > 0:
    print("Positive number")
print("Done")
```

---

## Extending

- To add more language features, edit `ToyPython.g4` and update `ToyPythonSemanticListener.py`.
- If you add grammar rules, re-run ANTLR as above.

---

**Yay! Have fun experimenting with this tiny version of Python.**
