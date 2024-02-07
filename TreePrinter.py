import AbstractSyntaxTree

SEP = ' | '


def show_node(intend, content):
    print(SEP*intend, content)


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


class TreePrinter:

    @addToClass(AbstractSyntaxTree.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " +
                        self.__class__.__name__)

    @addToClass(AbstractSyntaxTree.IntNum)  # 1
    def printTree(self, indent=0):
        show_node(indent, self.value)

    @addToClass(AbstractSyntaxTree.FloatNum)  # 2
    def printTree(self, indent=0):
        show_node(indent, self.value)

    @addToClass(AbstractSyntaxTree.String)  # 3
    def printTree(self, indent=0):
        show_node(indent, self.string)

    @addToClass(AbstractSyntaxTree.Variable)  # 4
    def printTree(self, indent=0):
        show_node(indent, self.name)

    @addToClass(AbstractSyntaxTree.BinExpr)  # 5
    def printTree(self, indent):
        print(SEP*indent, self.op)
        if self.left:
            self.left.printTree(indent + 1)
        if self.right:
            self.right.printTree(indent + 1)

    @addToClass(AbstractSyntaxTree.UnaryExpr)  # 6
    def printTree(self, indent=0):
        show_node(indent,  self.op)
        self.expr.printTree(indent + 1)

    @addToClass(AbstractSyntaxTree.Recursion)  # 7
    def printTree(self, indent=0):
        if self.left:
            self.left.printTree(indent)
        if self.right:
            self.right.printTree(indent)

    @addToClass(AbstractSyntaxTree.PrintExpr)  # 8
    def printTree(self, indent=0):
        show_node(indent, "PRINT")
        if self.to_print:
            self.to_print.printTree(indent + 1)

    @addToClass(AbstractSyntaxTree.EndExpr)  # 9
    def printTree(self, indent=0):
        show_node(indent, self.to_return)

    @addToClass(AbstractSyntaxTree.Reference)  # 10
    def printTree(self, indent=0):
        show_node(indent, "REF")
        show_node(indent+1, self.name)
        if self.vect:
            self.vect.printTree(indent + 1)

    @addToClass(AbstractSyntaxTree.IfInstruction)  # 11
    def printTree(self, indent=0):
        show_node(indent,  "IF")
        if self.cond:
            self.cond.printTree(indent + 1)
        show_node(indent,  "THEN")
        if self.instruction:
            self.instruction.printTree(indent + 1)

    @addToClass(AbstractSyntaxTree.IfElseInstruction)  # 12
    def printTree(self, indent=0):
        show_node(indent, "IF")
        if self.cond:
            self.cond.printTree(indent + 1)
        show_node(indent, "THEN")
        if self.instruction_if:
            self.instruction_if.printTree(indent + 1)
        show_node(indent,  "ELSE")
        if self.instruction_else:
            self.instruction_else.printTree(indent + 1)

    @addToClass(AbstractSyntaxTree.WhileInstruction)  # 13
    def printTree(self, indent=0):
        show_node(indent, "WHILE")
        if self.cond:
            self.cond.printTree(indent + 1)
        if self.instruction:
            self.instruction.printTree(indent + 1)

    @addToClass(AbstractSyntaxTree.ForInstruction)  # 14
    def printTree(self, indent=0):
        show_node(indent,  "FOR")
        show_node(indent+1,  self.iterator)
        show_node(indent,  "RANGE")
        if self.start:
            self.start.printTree(indent + 2)
        if self.end:
            self.end.printTree(indent + 2)
        if self.instruction:
            self.instruction.printTree(indent + 1)

    @addToClass(AbstractSyntaxTree.Matrix)  # 15
    def printTree(self, indent=0):
        show_node(indent,  "MATRIX")
        if self.matrix:
            self.matrix.printTree(indent + 1)

    @addToClass(AbstractSyntaxTree.Vector)  # 16
    def printTree(self, indent=0):
        show_node(indent,  "VECTOR")
        if self.vector:
            self.vector.printTree(indent + 1)
