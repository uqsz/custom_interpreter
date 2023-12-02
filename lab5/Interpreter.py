
import AST
from Memory import *
from Exceptions import  *
from visit import *
import sys

sys.setrecursionlimit(10000)

class Interpreter(object):


    @on('node')
    def visit(self, node):
        pass

    @when(AST.IntNum) # 1
    def visit(self,node):
        pass

    @when(AST.FloatNum) # 2
    def visit(self,node):
        pass

    @when(AST.String) # 3
    def visit(self,node):
        pass

    @when(AST.Variable) # 4
    def visit(self,node):
        pass

    @when(AST.BinExpr) # 5
    def visit(self,node):
        pass

    @when(AST.UnaryExpr) # 6
    def visit(self,node):
        pass

    @when(AST.Recursion) # 7
    def visit(self,node):
        pass

    @when(AST.PrintExpr) # 8
    def visit(self,node):
        pass

    @when(AST.ReturnExpr) # 9
    def visit(self,node):
        pass

    @when(AST.EndExpr) # 10
    def visit(self,node):
        pass

    @when(AST.Reference) # 11
    def visit(self,node):
        pass

    @when(AST.IfInstruction) # 12
    def visit(self,node):
        pass

    @when(AST.IfElseInstruction) # 13
    def visit(self,node):
        pass

    @when(AST.WhileInstruction) # 14
    def visit(self,node):
        pass

    @when(AST.ForInstruction) # 15
    def visit(self,node):
        pass

    @when(AST.Matrix) # 16
    def visit(self,node):
        pass

    @when(AST.Vector) # 17
    def visit(self,node):
        pass

    @when(AST.Error) # 18
    def visit(self,node):
        pass


    # @when(AST.BinOp) # 16
    # def visit(self, node):
    #     r1 = node.left.accept(self)
    #     r2 = node.right.accept(self)
    #     # try sth smarter than:
    #     # if(node.op=='+') return r1+r2
    #     # elsif(node.op=='-') ...
    #     # but do not use python eval

    # @when(AST.Assignment)
    # def visit(self, node):
    #     pass
    # #

    # # simplistic while loop interpretation
    # @when(AST.WhileInstr)
    # def visit(self, node):
    #     r = None
    #     while node.cond.accept(self):
    #         r = node.body.accept(self)
    #     return r

