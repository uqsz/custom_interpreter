# Custom Interpreter

This repository is dedicated to the Theory of Compilation course project, which involves building a custom interpreter.

## Overview

This project aims to develop our understanding of how compilers work by building a custom interpreter. We will cover the following key areas:

1. **Lexical Analysis**: The process of breaking down the input source code into tokens, such as identifiers, keywords, operators, and symbols.

2. **Parsing**: Parsing involves analyzing the sequence of tokens to determine the syntactic structure of the source code according to a grammar.

3. **Abstract Syntax Tree (AST) Generation**: After parsing the source code, the compiler constructs an Abstract Syntax Tree (AST) representing the syntactic structure of the program. The AST serves as an intermediate representation of the code and facilitates further analysis and manipulation during subsequent compiler phases.

4. **Semantic Analysis**: Semantic analysis ensures that the syntactically correct code also adheres to the defined semantics of the programming language. This phase includes type checking, scope resolution, and other semantic validations.

5. **Interpreter**: The final phase of the compiler involves interpreting the parsed and analyzed source code to execute it directly.

### Lexical analysis

Creating a lexical analyzer (scanner) for a simple language enabling calculations on matrices. The lexical analyzer recognizes the following lexemes:

- binary operators: +, -, \*, /
- matrix binary operators (for element-wise operations): .+, .-, .\*, ./
- assignment operators: =, +=, -=, \*=, /=
- relational operators: <, >, <=, >=, !=, ==
- parentheses: (,), [,], {,}
- range operator: :
- matrix transpose: '
- comma and semicolon: , ;
- keywords: if, else, for, while
- keywords: break, continue, and return
- keywords: eye, zeros, and ones
- keyword: print
- identifiers (the first character of the identifier is a letter or _, followed by letters, digits, or _)
- integers
- floating-point numbers
- strings

For recognized lexemes, the scanner returns corresponding token, recognized lexeme and line number.

Spaces, tabs, newline characters and comments starting with # until the end of the line are ignored

You can check the implementation in the [Scanner.py](Scanner.py).

### Parsing

Creating a parser for a language for matrix operations. The parser recognizes source code in the form of tokens or report a parsing error in case of invalid input. The parser recognizes the following constructs:

- binary expressions, including element-wise matrix operations
- relational expressions
- unary negation
- matrix transpose
- matrix initialization with specific values
- special matrix functions
- assignment statements, including various assignment operators
- conditional if-else statements
- loops: while and for
- statements: break, continue, and return
- print statement
- compound statements
- arrays and their ranges

You can check the implemented grammar in the [grammar.txt](grammar.txt) and the parser in [Parser.py](Parser.py).

### Abstract Syntax Tree (AST) Generation

Creating and printing an Abstract Syntax Tree (AST) which includes the following constructs in its nodes:

- binary expressions
- relational expressions
- assignment statements
- conditional if-else statements
- loops: while and for
- statements: break, continue, and return
- print statement
- compound statements
- arrays and their ranges

You can check the implementation of AST in [AbstractSyntaxTree.py](AbstractSyntaxTree.py) and the printer in [TreePrinter.py](TreePrinter.py).

### Semantic Analysis

Creating a semantic error analyzer which detects various semantic errors, including:

- Matrix initialization using vectors of different sizes
- Out-of-bounds matrix references (for constant indices)
- Incompatible types or sizes for binary operations, such as:
  - Adding a scalar or vector to a matrix
  - Binary operations on vectors or matrices with incompatible dimensions
- Incorrect usage of initialization functions (eye, zeros, ones) with incorrect parameters
- Improper use of statements:
  - Break or continue statements outside of a loop

You can check the implementation in [TypeChecker.py](TypeChecker.py).

### Interpreter

Creating an interpreter for the language specified in previous exercises. Interpretation only occurs if the previous stages have completed successfully - no syntax or semantic errors occurred.

You can check the implementation in [Interpreter.py](Interpreter.py).

## Tests

You can verify the functionality by running the `test.py` script, which executes the files from the `examples` folder and saves the results in files within the `parsing` folder.

## Repository Setup and Execution

To set up the repository and run the `main.py` script with a file path argument:

1. Clone the repository to your local machine.
2. Ensure that all necessary dependencies are installed (if any).
3. Navigate to the directory containing the repository.
4. Open a terminal or command prompt.
5. Run the `main.py` script with the file path of the input file as an argument.

Example command:

```bash
python main.py /path/to/input_file
```

## Summary

This repository provides an interpreter for a specific language, allowing users to execute code and analyze results. By following the instructions provided, users can set up the repository, execute the interpreter script with input files, and review the output for further analysis and debugging.
