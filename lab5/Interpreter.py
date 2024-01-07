
import AST
from Memory import *
from Exceptions import *
from visit import *
import sys

sys.setrecursionlimit(10000)


class Interpreter(object):

    def __init__(self):
        self.memory = Memory("global")

    @on('node')
    def visit(self, node):
        pass

    @when(AST.IntNum)  # 1
    def visit(self, node):
        return int(node.value)

    @when(AST.FloatNum)  # 2
    def visit(self, node):
        return node.value

    @when(AST.String)  # 3
    def visit(self, node):
        return node.name

    @when(AST.Variable)  # 4
    def visit(self, node):
        return node.name

    @when(AST.BinExpr)  # 5
    def visit(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op = node.op

        operator_mapping = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '>': lambda x, y: x > y,
            '<': lambda x, y: x < y,
            '>=': lambda x, y: x >= y,
            '<=': lambda x, y: x <= y,
            '==': lambda x, y: x == y,
            '!=': lambda x, y: x != y,
            '.+': lambda x, y: dotadd(x, y),
            '.-': lambda x, y: dotsub(x, y),
            '.*': lambda x, y: dotmul(x, y),
            './': lambda x, y: dotdiv(x, y),
            '+=': lambda x, y: self.memory.put(x, self.memory.get(x)+y),
            '-=': lambda x, y: self.memory.put(x, self.memory.get(x)-y),
            '*=': lambda x, y: self.memory.put(x, self.memory.get(x)*y),
            '/=': lambda x, y: self.memory.put(x, self.memory.get(x)/y),
        }

        if self.memory.has_key(right):
            right = self.memory.get(right)
        if op == "=":
            self.memory.put(left, right),
            return

        operation = operator_mapping[op]

        if op in ["+=", "-=", "*=", "/="]:
            return operation(left, right)
        if self.memory.has_key(left):
            left = self.memory.get(left)
        return operation(left, right)

    @when(AST.UnaryExpr)  # 6
    def visit(self, node):
        expr = self.visit(node.expr)
        op = node.op

        operator_mapping = {
            'eye': lambda x: eye(x),
            'zeros': lambda x: zeros(x),
            'ones': lambda x: ones(x),
            'TRANSPOSE': lambda x: transpose(x),
            'MINUS': lambda x: minus(x),
        }

        if self.memory.has_key(expr):
            expr = self.memory.get(expr)

        operation = operator_mapping[op]

        return operation(expr)

    @when(AST.Recursion)  # 7
    def visit(self, node):
        self.visit(node.left)
        self.visit(node.right)

    @when(AST.PrintExpr)  # 8
    def visit(self, node):

        to_print = node.to_print
        v = []
        while to_print.right != None:
            element = self.visit(to_print.left)
            
            v.append(element)
            to_print = to_print.right

        v.append(self.visit(to_print.left))
        

        for elem in v:
            if self.memory.has_key(str(elem)):
                print(self.memory.get(str(elem)), end=" ")
            else:
                print(str(elem), end=" ")
        print(end="\n")

    @when(AST.ReturnExpr)  # 9
    def visit(self, node):
        pass

    @when(AST.EndExpr)  # 10
    def visit(self, node):
        pass

    @when(AST.Reference)  # 11
    def visit(self, node):
        return self.memory.get(node.name)[node.vect.v[0]][node.vect.v[1]]

    @when(AST.IfInstruction)  # 12
    def visit(self, node):
        r = None
        if self.visit(node.cond):
            r = self.visit(node.instruction)
        return r

    @when(AST.IfElseInstruction)  # 13
    def visit(self, node):
        r = None
        if self.visit(node.cond):
            r = self.visit(node.instruction)
        else:
            r = self.visit(node.instruction_else)
        return r

    @when(AST.WhileInstruction)  # 14
    def visit(self, node):
        r = None
        while self.visit(node.cond):
            r = self.visit(node.instruction)
        return r

    @when(AST.ForInstruction)  # 15
    def visit(self, node):
        r = None
        start = self.visit(node.start)
        end = self.visit(node.end)

        if self.memory.has_key(str(start)):
            start = self.memory.get(str(start))

        if self.memory.has_key(str(end)):
            end = self.memory.get(str(end))

        for i in range(start, end):
            self.memory.put(node.iterator, i)
            r = self.visit(node.instruction)
        return r

    @when(AST.Matrix)  # 16
    def visit(self, node):
        return node.m

    @when(AST.Vector)  # 17
    def visit(self, node):
        return node.v

    @when(AST.Error)  # 18
    def visit(self, node):
        pass


def dotadd(A, B):
    result = [[a + b for a, b in zip(row_a, row_b)]
              for row_a, row_b in zip(A, B)]
    return result


def dotsub(A, B):
    result = [[a - b for a, b in zip(row_a, row_b)]
              for row_a, row_b in zip(A, B)]
    return result


def dotmul(A, B):
    result = [[a * b for a, b in zip(row_a, row_b)]
              for row_a, row_b in zip(A, B)]
    return result


def dotdiv(A, B):
    result = [[a / b for a, b in zip(row_a, row_b)]
              for row_a, row_b in zip(A, B)]
    return result


def eye(x):
    return [[1 if i == j else 0 for j in range(x)] for i in range(x)]


def ones(x):
    return [[1] * x for _ in range(x)]


def zeros(x):
    return [[0] * x for _ in range(x)]


def transpose(x):
    return [[row[i] for row in x] for i in range(len(x[0]))]


def minus(x):
    if isinstance(x, int):
        return -x
    else:
        return [[-element for element in row] for row in x]
