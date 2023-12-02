

class Node(object):
    def __init__(self, lineno):
        self.lineno = lineno


class IntNum(Node):  # 1
    def __init__(self, value, lineno):
        super().__init__(lineno)
        self.value = value


class FloatNum(Node):  # 2
    def __init__(self, value, lineno):
        super().__init__(lineno)
        self.value = value


class String(Node):  # 3
    def __init__(self, string, lineno):
        super().__init__(lineno)
        self.string = string


class Variable(Node):  # 4
    def __init__(self, name, lineno):
        super().__init__(lineno)
        self.name = name


class BinExpr(Node):  # 5
    def __init__(self, op, left, right, lineno):
        super().__init__(lineno)
        self.op = op
        self.left = left
        self.right = right


class UnaryExpr(Node):  # 6
    def __init__(self, op, expr, lineno):
        super().__init__(lineno)
        self.op = op
        self.expr = expr


class Recursion(Node):  # 7
    def __init__(self, left, right, lineno):
        super().__init__(lineno)
        self.left = left
        self.right = right


class PrintExpr(Node):  # 8
    def __init__(self, to_print, lineno):
        super().__init__(lineno)
        self.to_print = to_print


class ReturnExpr(Node):  # 9
    def __init__(self, to_return, lineno):
        super().__init__(lineno)
        self.to_return = to_return


class EndExpr(Node):  # 10
    def __init__(self, to_return, lineno):
        super().__init__(lineno)
        self.to_return = to_return


class Reference(Node):  # 11
    def __init__(self, name, vect, lineno):
        super().__init__(lineno)
        self.name = name
        self.vect = vect


class IfInstruction(Node):  # 12
    def __init__(self, cond, instruction, lineno):
        super().__init__(lineno)
        self.cond = cond
        self.instruction = instruction


class IfElseInstruction(Node):  # 13
    def __init__(self, cond, instruction_if, instruction_else, lineno):
        super().__init__(lineno)
        self.cond = cond
        self.instruction_if = instruction_if
        self.instruction_else = instruction_else


class WhileInstruction(Node):  # 14
    def __init__(self, cond, instruction, lineno):
        super().__init__(lineno)
        self.cond = cond
        self.instruction = instruction


class ForInstruction(Node):  # 15
    def __init__(self, iterator, start, end, instruction, lineno):
        super().__init__(lineno)
        self.iterator = iterator
        self.start = start
        self.end = end
        self.instruction = instruction


class Matrix(Node):  # 16
    def __init__(self, matrix, lineno):
        super().__init__(lineno)
        self.matrix = matrix
        self.m = []
        while hasattr(matrix, 'left'):
            self.m.append(matrix.right.v)
            matrix = matrix.left
        self.m.append(matrix.v)
        self.m.reverse()


class Vector(Node):  # 17
    def __init__(self, vector, lineno):
        super().__init__(lineno)
        self.vector = vector
        self.v = []
        while hasattr(vector, 'left'):
            self.v.append(vector.right.value)
            vector = vector.left
        self.v.append(vector.value)
        self.v.reverse()


class Error(Node):  # 18
    def __init__(self):
        pass
