# Single underscore (private)
class MyClass:
    def __init__(self):
        self._my_attr = 42  # Internal attribute with a single underscore prefix

    def _my_method(self):
        # Internal method with a single underscore prefix
        print("Single underscore")


obj = MyClass()
print(obj._my_attr)  # Accessing internal attribute (not recommended)
obj._my_method()

# Double underscore (private)


class MyClass:
    def __init__(self):
        self.__my_attr = 42  # Name-mangled attribute with double underscores•

    def __my_method(self):
        # Name-mangled method with double underscores
        return "Double Underscore"


obj = MyClass()
# print(obj.__my_attr) # Accessing name-mangled attribute (not recommended)
print(obj._MyClass__my_attr)

# obj.__my_method() # Accessing name-mangled method (not recommended)
print(obj._MyClass__my_method())

'''
Note:
see how it is mangled:

Obj._MyClass__my_attr (here _classname+attr)'''
