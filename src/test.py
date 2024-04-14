import sys
import os
import Parser
import Scanner
import TreePrinter
from TypeChecker import TypeChecker
from Interpreter import Interpreter

if __name__ == '__main__':

    directory_examples = "examples"
    directory_parsing = "parsing"

    parser = Parser.parser

    Interpreter = Interpreter()

    for filename in os.listdir(directory_examples):
        filepath = os.path.join(directory_examples, filename)
        parsing_filepath = os.path.join(directory_parsing, filename)

        with open(filepath, "r") as example:
            text = example.read()

        Scanner.lexer.lineno = 1

        ast = parser.parse(text, lexer=Scanner.lexer)

        parsing_filepath = parsing_filepath[:-1]+"txt"
        with open(parsing_filepath, "w") as parsing_file:
            sys.stdout = parsing_file
            if ast:
                print(filename + "\n")
                print("ABSTRACT SYNTAX TREE:")
                ast.printTree()
                print("\nTYPE CHECKER:")
                typeChecker = TypeChecker()
                typeChecker.visit(ast)
                if not typeChecker.error:
                    print("\nINTERPRETER:")
                    Interpreter.visit(ast)
        sys.stdout = sys.__stdout__
