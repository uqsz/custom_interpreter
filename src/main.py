import sys
import os
import Parser
import Scanner
import TreePrinter
from TypeChecker import TypeChecker
from Interpreter import Interpreter

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(
            sys.argv) > 1 else "examples/example3.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()

    Scanner.lexer.lineno = 1

    parser = Parser.parser

    ast = parser.parse(text, lexer=Scanner.lexer)

    typeChecker = TypeChecker()
    Interpreter = Interpreter()

    # ast.printTree()

    typeChecker.visit(ast)

    if not typeChecker.error:
        Interpreter.visit(ast)
