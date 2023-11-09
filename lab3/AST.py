

class Node(object):
    pass


class IntNum(Node):
    def __init__(self, value):
        self.value = value


class FloatNum(Node):

    def __init__(self, value):
        self.value = value


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
        self.object = expr


class Parenth(Node):
    def __init__(self, expr):
        self.op = expr


# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
