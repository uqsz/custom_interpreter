from __future__ import print_function
import AST
SEP = '|  '

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
        print(SEP*indent, self.value)

    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        print(SEP*indent, self.value)

    @addToClass(AST.String)
    def printTree(self, indent=0):
        print(SEP*indent, self.string)

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        print(SEP*indent, self.name)

    @addToClass(AST.BinExpr)
    def printTree(self, indent):
        print(SEP*indent, self.op)
        self.left.printTree(indent + 1)
        if (self.right != None):
            self.right.printTree(indent + 1)

    @addToClass(AST.UnaryExpr)
    def printTree(self, indent=0):
        print(SEP*indent, self.op)
        self.expr.printTree(indent + 1)

    @addToClass(AST.Recursion)
    def printTree(self, indent=0):
        self.left.printTree(indent)
        self.right.printTree(indent)

    @addToClass(AST.PrintExpr)
    def printTree(self, indent=0):
        print(SEP*indent, "PRINT")
        self.to_print.printTree(indent + 1)

    @addToClass(AST.ReturnExpr)
    def printTree(self, indent=0):
        print(SEP*indent, "RETURN")
        self.to_return.printTree(indent + 1)

    @addToClass(AST.Reference)
    def printTree(self, indent=0):
        print(SEP*indent, "REF")
        print(SEP*indent, self.name)
        self.vect.printTree(indent + 1)

    @addToClass(AST.IfInstruction)
    def printTree(self, indent=0):
        print(SEP*indent, "IF")
        self.cond.printTree(indent + 1)
        print(SEP*indent, "THEN")
        self.instruction.printTree(indent + 1)

    @addToClass(AST.IfElseInstruction)
    def printTree(self, indent=0):
        print(SEP*indent, "IF")
        self.cond.printTree(indent + 1)
        print(SEP*indent, "THEN")
        self.instruction_if.printTree(indent + 1)
        print(SEP*indent, "ELSE")
        self.instruction_else.printTree(indent + 1)

    @addToClass(AST.WhileInstruction)
    def printTree(self, indent=0):
        print(SEP*indent, "WHILE")
        self.cond.printTree(indent + 1)
        print(SEP*indent, "THEN")
        self.instruction.printTree(indent + 1)

    @addToClass(AST.ForInstruction)
    def printTree(self, indent=0):
        print(SEP*indent, "FOR")
        print(SEP*indent, self.iterator)
        print(SEP*indent, "RANGE")
        print(SEP*indent, self.start)
        print(SEP*indent, self.end)
        self.instruction.printTree(indent + 1)


    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print(SEP*indent, "VECTOR")
        self.vector.printTree(indent + 1)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
        # fill in the body

    # define printTree for other classes
    # ...
