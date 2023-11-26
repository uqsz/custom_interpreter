
import sys
import ply.yacc as yacc
import scanner
import Mparser
import TreePrinter
import TypeChecker

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(
            sys.argv) > 1 else "lab4/examples/example2.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)


    parser = Mparser.parser
    text = file.read()
    ast = parser.parse(text, lexer=scanner.lexer)
    # ast.printTree()

    # Below code shows how to use visitor
    typeChecker = TypeChecker.TypeChecker()
    typeChecker.visit(ast)   # or alternatively ast.accept(typeChecker)
