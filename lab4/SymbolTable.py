

class VariableSymbol():
    def __init__(self, name, type):
        self.name = name  # Nazwa zmiennej
        self.type = type  # Typ zmiennej


class SymbolTable(object):

    def __init__(self, parent, name): 
        self.parent = parent  # parent scope
        self.name = name      # symbol table name
        self.symbols = {}     # dictionary to store symbols

    def put(self, name, symbol): 
        self.symbols[name] = symbol  # add symbol to the table

    def get(self, name): 
        return self.symbols.get(name)  # retrieve symbol from the table

    def getParentScope(self):
        return self.parent  # return the parent scope

    def pushScope(self, name):
        new_scope = SymbolTable(parent=self, name=name)  # create a new scope
        return new_scope

    def popScope(self):
        return self.parent  # move to the parent scope



