

class Node(object):
    pass


class IntNum(Node):
    def __init__(self, value):
        self.value = value


class FloatNum(Node):
    def __init__(self, value):
        self.value = value


class String(Node):
    def __init__(self, string):
        self.string = string


class Variable(Node):
    def __init__(self, name):
        self.name = name


class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class UnaryExpr(Node):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr


class Recursion(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class PrintExpr(Node):
    def __init__(self, to_print):
        self.to_print = to_print


class ReturnExpr(Node):
    def __init__(self, to_return):
        self.to_return = to_return


class EndExpr(Node):
    def __init__(self, to_return):
        self.to_return = to_return


class Reference(Node):
    def __init__(self, name, vect):
        self.name = name
        self.vect = vect


class IfInstruction(Node):
    def __init__(self, cond, instruction):
        self.cond = cond
        self.instruction = instruction


class IfElseInstruction(Node):
    def __init__(self, cond, instruction_if, instruction_else):
        self.cond = cond
        self.instruction_if = instruction_if
        self.instruction_else = instruction_else


class WhileInstruction(Node):
    def __init__(self, cond, instruction):
        self.cond = cond
        self.instruction = instruction


class ForInstruction(Node):
    def __init__(self, iterator, start, end, instruction):
        self.iterator = iterator
        self.start = start
        self.end = end
        self.instruction = instruction


class Matrix(Node):
    def __init__(self, matrix):
        self.matrix = matrix


class Vector(Node):
    def __init__(self, vector):
        self.vector = vector


class Error(Node):
    def __init__(self):
        pass
