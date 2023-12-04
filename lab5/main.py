
import sys
import ply.yacc as yacc
import Mparser
import scanner
from TreePrinter import TreePrinter
from TypeChecker import TypeChecker
from Interpreter import Interpreter


if __name__ == '__main__':

    try:
        filename = "lab5/examples/matrix.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()

    parser = Mparser.parser

    ast = parser.parse(text, lexer=scanner.lexer)
    ast.printTree()

    typeChecker = TypeChecker()
    typeChecker.visit(ast)

    Interpreter=Interpreter()
    Interpreter.visit(ast)
    # in future
    # ast.accept(OptimizationPass1())
    # ast.accept(OptimizationPass2())
    # ast.accept(CodeGenerator())
