import AST as AST


class VariableSymbol():
    def __init__(self, name, type, size=0):
        self.name = name
        self.type = type
        self.size = size


class SymbolTable(object):

    def __init__(self, parent, name):
        self.parent = parent  # parent scope
        self.name = name      # symbol table name
        self.symbols = {}     # dictionary to store symbols
        self.loop = 0

    def put(self, name, type, size=0):
        self.symbols[name] = VariableSymbol(
            name, type, size)  # add symbol to the table

    def get(self, name):
        return self.symbols.get(name)  # retrieve symbol from the table

    def getParentScope(self):
        return self.parent  # return the parent scope

    def pushScope(self, name):
        new_scope = SymbolTable(parent=self, name=name)  # create a new scope
        return new_scope

    def popScope(self):
        return self.parent  # move to the parent scope


class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for child in node.children:
            self.visit(child)


class TypeChecker(NodeVisitor):

    def __init__(self):

        self.scope = SymbolTable(None, "global")

    def visit_IntNum(self, node):  # 1
        return "int"

    def visit_FloatNum(self, node):  # 2
        return "float"

    def visit_String(self, node):  # 3
        return "string"

    def visit_Variable(self, node):  # 4

        variable_symbol = self.scope.get(node.name)
        if variable_symbol:
            return variable_symbol.type
        else:
            return 'none'

    def visit_BinExpr(self, node):  # 5
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)
        op = node.op

        typeError = False

        if op == "=":
            if type2 == "matrix":
                if hasattr(node.right, "m"):
                    x = node.right.size
                else:
                    x = 0
                self.scope.put(node.left.name, type2, x)
            else:
                self.scope.put(node.left.name, type2)

        elif op in ["+=", "-=", "*=", "/="]:
            if self.scope.get(node.left.name) == None:
                print(
                    f"Error at line {node.lineno}: Variable '{node.left.name}' is not defined.")
                return 'none'
            elif self.scope.get(node.left.name).type != type2:
                typeError = True

        elif op in ["+", "-", "*", "/"]:
            if type1 == "int" and type2 == "int":
                return "int"
            elif type1 in {"int", "float"} and type2 in {"int", "float"}:
                return "float"
            else:
                typeError = True

        elif op in [".+", ".-", ".*", "./"]:
            if type1 == "matrix" and type2 == "matrix":
                return "matrix"
            else:
                typeError = True

        elif op in ['>', '<', '>=', '<=', '==', '!=']:
            if type1 in {"int", "float"} and type2 in {"int", "float"}:
                return "bool"
            else:
                typeError = True

        if typeError:
            print(
                f"Error at line {node.lineno}: Incompatible types {type1,type2} for binary operation '{op}'.")
        return "none"

    def visit_UnaryExpr(self, node):  # 6
        type1 = self.visit(node.expr)
        op = node.op

        typeError = False

        if op in ["eye", "zeros", "ones"]:
            if type1 == "int":
                return "matrix"
            else:
                typeError = True

        elif op == "TRANSPOSE":
            if type1 == "matrix":
                return "matrix"
            else:
                typeError = True

        elif op == "MINUS":
            if type1 in ["int", "float", "matrix"]:
                return type1
            else:
                typeError = True

        if typeError:
            print(
                f"Error at line {node.lineno}: Incompatible type '({type1})' for unary operation: '{op}'.")
        return "none"

    def visit_Recursion(self, node):  # 7
        self.visit(node.left)
        self.visit(node.right)

    def visit_PrintExpr(self, node):  # 8
        return "print"

    def visit_ReturnExpr(self, node):  # 9
        return "return"

    def visit_EndExpr(self, node):  # 10
        if self.scope.loop == 0:
            print(
                f"Error at line {node.lineno}: Instruction '{node.to_return}' is not in a loop.")
        return "none"

    def visit_Reference(self, node):  # 11
        var = self.scope.get(node.name)
        error = False

        if var == None:
            print(
                f"Error at line {node.lineno}: Variable '{node.name}' is not defined.")
            error = True

        elif len(node.vect.v) != 2:
            print(
                f"Error at line {node.lineno}: Reference '({node.vect.v})' is not a 2-element vector.")
            error = True

        elif var.type != "matrix":
            print(
                f"Error at line {node.lineno}: Incompatible type '({var.type})' for reference operation.")
            error = True
        elif (node.vect.v[0] >= var.size or node.vect.v[1] >= var.size) and var.size != 0:
            print(
                f"Error at line {node.lineno}: Reference '({node.vect.v})' is out of range.")
            error = True
        if error:
            return "error"
        return "reference"

    def visit_IfInstruction(self, node):  # 12
        type1 = self.visit(node.cond)

        self.visit(node.instruction)

        if type1 != "bool":
            print(
                f"Error at line {node.lineno}: Condition is not a bool statement.")
        return "none"

    def visit_IfElseInstruction(self, node):  # 13
        type1 = self.visit(node.cond)
        self.visit(node.instruction_if)
        self.visit(node.instruction_else)
        if type1 != "bool":
            print(
                f"Error at line {node.lineno}: Condition is not a bool statement.")
        return "none"

    def visit_WhileInstruction(self, node):  # 14
        type1 = self.visit(node.cond)
        self.scope.loop += 1
        self.visit(node.instruction)
        self.scope.loop -= 1

        if type1 != "bool":
            print(
                f"Error at line {node.lineno}: Condition is not a bool statement.")
        return "none"

    def visit_ForInstruction(self, node):  # 15
        type2 = self.visit(node.start)
        type3 = self.visit(node.end)

        self.scope.loop += 1
        self.scope.put(node.iterator, type2)
        self.visit(node.instruction)
        self.scope.loop -= 1

        if not (type3 == type2 == "int"):
            print(
                f"Error at line {node.lineno}: Range does not contains only int types: '{type2}:{type3}'.")
        return "none"

    def visit_Matrix(self, node):  # 16
        if len(node.m) > 0:
            row = len(node.m[0])
            for i in range(1, len(node.m)):
                if len(node.m[i]) != row:
                    print(
                        f"Error at line {node.lineno}: Matrix is not a square matrix.")
                    return "none"
        return "matrix"

    def visit_Vector(self, node):  # 17
        return "vector"

    def visit_Error(self, node):  # 18
        return "error"
