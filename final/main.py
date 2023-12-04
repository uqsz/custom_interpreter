import sys
import os
import ply.yacc as yacc
import compilator.Scanner as scanner
import compilator.Mparser as Mparser
from compilator.TypeChecker import TypeChecker
from compilator.TreePrinter import TreePrinter


if __name__ == '__main__':

    directory_examples = "final/examples"
    directory_output = "final/output"

    for filename in os.listdir(directory_examples):
        filepath = os.path.join(directory_examples, filename)
        try:
            with open(filepath, "r") as example:
                output_filepath = os.path.join(directory_output, filename)
                text = example.read()
        except IOError:
            print(f"Cannot open {filename} file")

        output_filepath = output_filepath[:-1]+"txt"
        try:
            with open(output_filepath, "w") as output_file:
                sys.stdout = output_file
                parser = Mparser.parser
                scanner.lexer.lineno = 1
                ast = parser.parse(text, lexer=scanner.lexer)
                if ast:
                    ast.printTree()
                    typeChecker = TypeChecker()
                    typeChecker.visit(ast)
                print("SUCCESS")
                sys.stdout = sys.__stdout__
        except IOError:
            print(f"Cannot open {filename} file")
