

class Node(object):
    pass


class IntNum(Node): # 1
    def __init__(self, value):
        self.value = value


class FloatNum(Node): # 2
    def __init__(self, value):
        self.value = value


class String(Node): # 3
    def __init__(self, string):
        self.string = string


class Variable(Node): # 4
    def __init__(self, name):
        self.name = name


class BinExpr(Node): # 5
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class UnaryExpr(Node): # 6
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr


class Recursion(Node): # 7
    def __init__(self, left, right):
        self.left = left
        self.right = right


class PrintExpr(Node): # 8
    def __init__(self, to_print):
        self.to_print = to_print


class ReturnExpr(Node): # 9
    def __init__(self, to_return):
        self.to_return = to_return


class EndExpr(Node): # 10
    def __init__(self, to_return):
        self.to_return = to_return


class Reference(Node): # 11
    def __init__(self, name, vect):
        self.name = name
        self.vect = vect


class IfInstruction(Node): # 12
    def __init__(self, cond, instruction):
        self.cond = cond
        self.instruction = instruction


class IfElseInstruction(Node): # 13
    def __init__(self, cond, instruction_if, instruction_else):
        self.cond = cond
        self.instruction_if = instruction_if
        self.instruction_else = instruction_else


class WhileInstruction(Node): # 14
    def __init__(self, cond, instruction):
        self.cond = cond
        self.instruction = instruction


class ForInstruction(Node): # 15
    def __init__(self, iterator, start, end, instruction):
        self.iterator = iterator
        self.start = start
        self.end = end
        self.instruction = instruction


class Matrix(Node): # 16
    def __init__(self, matrix):
        self.matrix = matrix


class Vector(Node): # 17
    def __init__(self, vector):
        self.vector = vector


class Error(Node): # 18
    def __init__(self):
        pass
