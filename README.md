# Theory of Compilation

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

You can check the grammar in the [grammar.txt](grammar.txt) to gain a comprehensive understanding of the language syntax and constructs recognized by the parser.
