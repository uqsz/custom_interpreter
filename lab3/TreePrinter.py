from __future__ import print_function
import AST


def addToClass(cls):

    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " +
                        self.__class__.__name__)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        print(self.value)

    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        print(self.value)

    @addToClass(AST.String)
    def printTree(self, indent=0):
        print(self.string)

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        print(self.name)

    @addToClass(AST.BinExpr)
    def printTree(self, indent):
        print(self.op)
        self.left.printTree(indent + 1)
        if (self.right != None):
            self.right.printTree(indent + 1)

    @addToClass(AST.UnaryExpr)
    def printTree(self, indent=0):
        print(self.op)
        self.expr.printTree(indent + 1)

    @addToClass(AST.Recursion)
    def printTree(self, indent=0):
        self.right.printTree(indent+1)
        self.left.printTree(indent)

    @addToClass(AST.PrintExpr)
    def printTree(self, indent=0):
        print("PRINT")
        self.to_print.printTree(indent + 1)

    @addToClass(AST.PrintExpr)
    def printTree(self, indent=0):
        print("PRINT")
        self.to_print.printTree(indent + 1)

    @addToClass(AST.ReturnExpr)
    def printTree(self, indent=0):
        print("RETURN")
        self.to_return.printTree(indent + 1)

    @addToClass(AST.Reference)
    def printTree(self, indent=0):
        print("REF")
        print(self.name)
        self.vect.printTree(indent + 1)

    @addToClass(AST.IfInstruction)
    def printTree(self, indent=0):
        print("IF")
        self.to_return.printTree(indent + 1)

    @addToClass(AST.IfElseInstruction)
    def printTree(self, indent=0):
        print("RETURN")
        self.to_return.printTree(indent + 1)

    @addToClass(AST.WhileInstruction)
    def printTree(self, indent=0):
        print("RETURN")
        self.to_return.printTree(indent + 1)

    @addToClass(AST.ForInstruction)
    def printTree(self, indent=0):
        print("RETURN")
        self.to_return.printTree(indent + 1)

    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print("VECTOR")
        self.vector.printTree(indent + 1)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
        # fill in the body

    # define printTree for other classes
    # ...
