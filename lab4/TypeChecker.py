import AST


class VariableSymbol():
    def __init__(self, name, type):
        self.name = name  # Nazwa zmiennej
        self.type = type  # Typ zmiennej


class SymbolTable(object):

    def __init__(self, parent, name):
        self.parent = parent  # parent scope
        self.name = name      # symbol table name
        self.symbols = {}     # dictionary to store symbols

    def put(self, name, type):
        self.symbols[name] = VariableSymbol(
            name, type)  # add symbol to the table

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

    # Called if no explicit visitor function exists for a node.
    def generic_visit(self, node):
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    # def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)


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
        return node.name

    def visit_BinExpr(self, node):  # 5
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)
        op = node.op
        if op == "=":
            self.scope.put(type1, type2)
        elif op in ["+=", "-=", "*=", "/="]:
            if self.scope.get(type1) == None:
                print(f"Error: Variable no in scope: '{type1}'.")
                return 'error'
            elif self.scope.get(type1).type != type2:
                print(
                    f"Error: Incompatible types for binary operation '{op}'.")
                return 'error'
        elif op in ["+", "-", "*", "/"]:
            if type1 == "int" and type2 == "int":
                return "int"
            elif (type1 == "int" and type2 == "float") or (type1 == "float" and type2 == "int") or (type1 == "float" and type2 == "float"):
                return "float"
            else:
                print(
                    f"Error: Operation '{op}' not for types: '{type1}','{type2}'.")
                return 'error'
        elif op in [".+", ".-", ".*", "./"]:
            if type1 == "matrix" and type2 == "matrix":
                return "matrix"
            else:
                print(
                    f"Error: Operation '{op}' not for types: '{type1}','{type2}'.")
                return "error"
        elif op in ['>', '<', '>=', '<=', '==', '!=']:
            if (type1 == "int" or type1 == "float") and (type2 == "int" or type2 == "float"):
                return "bool"
            else:
                print(
                    f"Error: Operation '{op}' not for types: '{type1}','{type2}'.")
                return "error"

        # ...
        #

    def visit_UnaryExpr(self, node):  # 6
        type1 = self.visit(node.expr)
        op = node.op
        if op in ["eye", "zeros", "ones"]:
            if type1 == "int":
                return "matrix"
            else:
                print(f"Error: Operation '{op}' not for type: '{type1}'.")
                return "error"
        elif op == "TRANSPOSE":
            if type1 != "matrix":
                print(f"Error: Operation '{op}' not for type: '{type1}'.")
                return "error"

    def visit_Recursion(self, node):  # 7
        self.visit(node.left)
        self.visit(node.right)

    def visit_PrintExpr(self, node):  # 8
        return "print"

    def visit_ReturnExpr(self, node):  # 9
        return "return"

    def visit_EndExpr(self, node):  # 10
        pass

    def visit_Reference(self, node):  # 11
        return "reference"

    def visit_IfInstruction(self, node):  # 12
        pass

    def visit_IfElseInstruction(self, node):  # 13
        pass

    def visit_WhileInstruction(self, node):  # 14
        pass

    def visit_ForInstruction(self, node):  # 15
        pass

    def visit_Matrix(self, node):  # 16
        return "matrix"

    def visit_Vector(self, node):  # 17
        return "vector"

    def visit_Error(self, node):  # 18
        pass


class TypeChecker(NodeVisitor):

    def __init__(self):
        # You may need to initialize some attributes for your type checker
        pass

    def visit_IntNum(self, node):  # 1
        # Example: Assuming integers are always valid
        return 'int'

    def visit_FloatNum(self, node):  # 2
        # Example: Assuming floating-point numbers are always valid
        return 'float'

    def visit_String(self, node):  # 3
        # Example: Assuming strings are always valid
        return 'string'

    def visit_Variable(self, node):  # 4
        # Example: Check if the variable is defined in the symbol table
        variable_symbol = symbol_table.get(node.name)
        if variable_symbol:
            return variable_symbol.type
        else:
            print(f"Error: Variable '{node.name}' not defined.")
            return 'error'

    def visit_BinExpr(self, node):  # 5
        type1 = self.visit(node.left)
        type2 = self.visit(node.right)
        op = node.op

        # Example: Check if the types are compatible for the binary operation
        if type1 == 'int' and type2 == 'int':
            return 'int'
        elif type1 == 'float' and type2 == 'float':
            return 'float'
        else:
            print(f"Error: Incompatible types for binary operation '{op}'.")
            return 'error'

    def visit_UnaryExpr(self, node):  # 6
        # Example: Assuming unary operations are only allowed on numeric types
        operand_type = self.visit(node.expr)
        if operand_type in ['int', 'float']:
            return operand_type
        else:
            print(f"Error: Invalid type for unary operation '{node.op}'.")
            return 'error'

    # Implement similar logic for other node types...

    def visit_Error(self, node):  # 18
        return 'error'
