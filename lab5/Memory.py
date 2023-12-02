
class Memory:
    def __init__(self, name):
        self.name = name
        self.variables = {}

    def has_key(self, name):
        return name in self.variables

    def get(self, name):
        if name in self.variables:
            return self.variables[name]
        raise NameError(f"Variable '{name}' not defined in memory '{self.name}'")

    def put(self, name, value):
        self.variables[name] = value


class MemoryStack:
    def __init__(self, memory=None):
        self.stack = []
        if memory:
            self.stack.append(memory)

    def get(self, name):
        for memory in reversed(self.stack):
            if memory.has_key(name):
                return memory.get(name)
        raise NameError(f"Variable '{name}' not defined in memory stack")

    def insert(self, name, value):
        if self.stack:
            self.stack[-1].put(name, value)
        else:
            raise Exception("Memory stack is empty")

    def set(self, name, value):
        for memory in reversed(self.stack):
            if memory.has_key(name):
                memory.put(name, value)
                return
        raise NameError(f"Variable '{name}' not defined in memory stack")

    def push(self, memory):
        self.stack.append(memory)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        raise Exception("Memory stack is empty")

'''Klasa Memory reprezentuje pojedynczą pamięć, a MemoryStack reprezentuje stos pamięci. Stos ten umożliwia operacje takie jak push (dodanie pamięci na wierzch stosu) i pop (usunięcie pamięci z wierzchołka stosu). Metoda get pozwala na pobranie wartości zmiennej z całego stosu pamięci. Metody insert i set umożliwiają dodanie nowej zmiennej lub zmianę wartości istniejącej zmiennej w bieżącej pamięci na wierzchołku stosu.'''



# class Memory:

#     def __init__(self, name): # memory name
#         pass
#     def has_key(self, name):  # variable name
#         pass
#     def get(self, name):         # gets from memory current value of variable <name>
#         pass
#     def put(self, name, value):  # puts into memory current value of variable <name>
#         pass

# class MemoryStack:
                                                                             
#     def __init__(self, memory=None): # initialize memory stack with memory <memory>
#         pass
#     def get(self, name):             # gets from memory stack current value of variable <name>
#         pass
#     def insert(self, name, value): # inserts into memory stack variable <name> with value <value>
#         pass
#     def set(self, name, value): # sets variable <name> to value <value>
#         pass
#     def push(self, memory): # pushes memory <memory> onto the stack
#         pass
#     def pop(self):          # pops the top memory from the stack
#         pass

