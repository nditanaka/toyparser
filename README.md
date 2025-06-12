# ToyPython Parser

ToyPython is a minimal Python-like interpreter built with [ANTLR4](https://www.antlr.org/) and Python. It parses and interprets a small subset of Python syntax, including assignments, print statements, arithmetic, and if-blocks with indentation.

---

## What’s Included

- **ToyPython.g4** – The ANTLR grammar for the language.
- **ToyPythonLexer.py / ToyPythonParser.py / ToyPythonListener.py** – ANTLR-generated Python files.
- **ToyPythonSemanticListener.py** – Custom Python code for interpreting ToyPython code.
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
   java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 ToyPython.g4
   ```

   This will generate (or update) files like:
   - `ToyPythonLexer.py`
   - `ToyPythonParser.py`
   - `ToyPythonListener.py`

3. Run the example:

   ```sh
   python main.py example.toy
   ```

   This will output the parse tree and interpret the program.

---

## Example Inputs & Outputs

### Printing, Assignment, and If Statement

**Input:**

```
x = 5
print("Hello, world!")
if x > 0:
    print("x is positive")
print(x)
```

**Output:**

```
Parsed successfully!
Parse Tree:
(program (statement (simpleStatement x = (expression (term (factor 5))) \n)) (statement (simpleStatement print ( (expression (term (factor "Hello, world!"))) ) \n)) (statement (compoundStatement if (comparison (expression (term (factor x))) > (expression (term (factor 0)))) : \n <INDENT> (statement (simpleStatement print ( (expression (term (factor "x is positive"))) ) \n)) <DEDENT>)) (statement (simpleStatement print ( (expression (term (factor x))) ) \n)) <EOF>)
Hello, world!
x is positive
5
```

---

### String Assignment, String Concatenation, and Comparison

**Input:**

```
name = "Alice"
score = 10
if score >= 10:
    print("Congratulations " + name)
print("End of program")
```

**Output:**

```
Parsed successfully!
Parse Tree:
(program (statement (simpleStatement name = (expression (term (factor "Alice"))) \n)) (statement (simpleStatement score = (expression (term (factor 10))) \n)) (statement (compoundStatement if (comparison (expression (term (factor score))) >= (expression (term (factor 10)))) : \n <INDENT> (statement (simpleStatement print ( (expression (term (factor "Congratulations ") + (term (factor name)))) ) \n)) <DEDENT>)) (statement (simpleStatement print ( (expression (term (factor "End of program"))) ) \n)) <EOF>)
Congratulations Alice
End of program
```

---

### Arithmetic Expressions and Comparison

**Input:**

```
a = 3
b = 7
print(a + b)
if a < b:
    print("a is less than b")
print("Finished")
```

**Output:**

```
Parsed successfully!
Parse Tree:
(program (statement (simpleStatement a = (expression (term (factor 3))) \n)) (statement (simpleStatement b = (expression (term (factor 7))) \n)) (statement (simpleStatement print ( (expression (term (factor a) + (term (factor b)))) ) \n)) (statement (compoundStatement if (comparison (expression (term (factor a))) < (expression (term (factor b)))) : \n <INDENT> (statement (simpleStatement print ( (expression (term (factor "a is less than b"))) ) \n)) <DEDENT>)) (statement (simpleStatement print ( (expression (term (factor "Finished"))) ) \n)) <EOF>)
10
a is less than b
Finished
```

---

### If Condition That Fails

**Input:**

```
x = 0
if x != 0:
    print("Nonzero")
print("Done")
```

**Output:**

```
Parsed successfully!
Parse Tree:
(program (statement (simpleStatement x = (expression (term (factor 0))) \n)) (statement (compoundStatement if (comparison (expression (term (factor x))) != (expression (term (factor 0)))) : \n <INDENT> (statement (simpleStatement print ( (expression (term (factor "Nonzero"))) ) \n)) <DEDENT>)) (statement (simpleStatement print ( (expression (term (factor "Done"))) ) \n)) <EOF>)
Done
```

---

## Extending

- To add more language features, we would need to edit `ToyPython.g4` and update `ToyPythonSemanticListener.py`.
- If we add grammar rules, re-run ANTLR as above.

---

**That’s it! Have fun experimenting with tiny Python.**
