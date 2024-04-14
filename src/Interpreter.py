
import inspect
import AbstractSyntaxTree as AST
import sys

sys.setrecursionlimit(10000)


__all__ = ['on', 'when']


def on(param_name):
    def f(fn):
        dispatcher = Dispatcher(param_name, fn)
        return dispatcher
    return f


def when(param_type):
    def f(fn):
        frame = inspect.currentframe().f_back
        func_name = fn.func_name if 'func_name' in dir(fn) else fn.__name__
        dispatcher = frame.f_locals[func_name]
        if not isinstance(dispatcher, Dispatcher):
            dispatcher = dispatcher.dispatcher
        dispatcher.add_target(param_type, fn)

        def ff(*args, **kw):
            return dispatcher(*args, **kw)
        ff.dispatcher = dispatcher
        return ff
    return f


class Dispatcher(object):
    def __init__(self, param_name, fn):
        self.param_index = self.__argspec(fn).args.index(param_name)
        self.param_name = param_name
        self.targets = {}

    def __call__(self, *args, **kw):
        typ = args[self.param_index].__class__
        d = self.targets.get(typ)
        if d is not None:
            return d(*args, **kw)
        else:
            issub = issubclass
            t = self.targets
            ks = iter(t)
            return [t[k](*args, **kw) for k in ks if issub(typ, k)]

    def add_target(self, typ, target):
        self.targets[typ] = target

    @staticmethod
    def __argspec(fn):
        # Support for Python 3 type hints requires inspect.getfullargspec
        if hasattr(inspect, 'getfullargspec'):
            return inspect.getfullargspec(fn)
        else:
            return inspect.getargspec(fn)


class BreakException(Exception):
    pass


class ContinueException(Exception):
    pass


class Memory:
    def __init__(self, name):
        self.name = name
        self.variables = {}

    def has_key(self, name):
        if type(name) == list:
            return False
        return name in self.variables

    def get(self, name):
        if name in self.variables:
            return self.variables[name]
        raise NameError(
            f"Variable '{name}' not defined in memory '{self.name}'")

    def put(self, name, value):
        self.variables[name] = value


class Interpreter(object):

    def __init__(self):
        self.memory = Memory("global")

    @on('node')
    def visit(self, node):
        pass

    @when(AST.IntNum)  # 1
    def visit(self, node):
        return node.value

    @when(AST.FloatNum)  # 2
    def visit(self, node):
        return node.value

    @when(AST.String)  # 3
    def visit(self, node):
        return node.string

    @when(AST.Variable)  # 4
    def visit(self, node):
        return node.name

    @when(AST.BinExpr)  # 5
    def visit(self, node):
        left = node.left
        if not isinstance(left, AST.Reference):
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
            content = right
            if isinstance(left, AST.Reference):
                content = self.memory.get(left.name)
                v = self.visit(node.left.vect)
                content[v[0]][v[1]] = right
            self.memory.put(left, content)
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
        else:
            v.append(self.visit(to_print.left))

        for elem in v:
            elem = str(elem)
            if self.memory.has_key(elem):
                print(self.memory.get(elem), end=" ")
            else:
                print(elem, end=" ")
        print(end="\n")

    @when(AST.EndExpr)  # 9
    def visit(self, node):
        raise BreakException()

    @when(AST.Reference)  # 10
    def visit(self, node):
        v = self.visit(node.vect)
        print(v)
        return self.memory.get(node.name)[v[0]][v[1]]

    @when(AST.IfInstruction)  # 11
    def visit(self, node):
        r = None
        if self.visit(node.cond):
            r = self.visit(node.instruction)
        return r

    @when(AST.IfElseInstruction)  # 12
    def visit(self, node):
        r = None
        if self.visit(node.cond):
            r = self.visit(node.instruction)
        else:
            r = self.visit(node.instruction_else)
        return r

    @when(AST.WhileInstruction)  # 13
    def visit(self, node):
        r = None
        while self.visit(node.cond):
            try:
                r = self.visit(node.instruction)
            except BreakException:
                return r
        return r

    @when(AST.ForInstruction)  # 14
    def visit(self, node):
        r = None
        start = self.visit(node.start)
        end = self.visit(node.end)

        if self.memory.has_key(str(start)):
            start = self.memory.get(str(start))

        if self.memory.has_key(str(end)):
            end = self.memory.get(str(end))

        for i in range(start, end):
            try:
                self.memory.put(node.iterator, i)
                r = self.visit(node.instruction)
            except BreakException:
                return r
        return r

    @when(AST.Matrix)  # 15
    def visit(self, node):
        m = []
        while hasattr(node, 'left'):
            m.append(node.right)
            node = node.left
        else:
            m.append(node)
        return m

    @when(AST.Vector)  # 16
    def visit(self, node):
        v = []
        node = node.vector
        while hasattr(node, 'right'):
            v.append(node.left.value)
            node = node.right
        else:
            v.append(node.value)
        return v


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
