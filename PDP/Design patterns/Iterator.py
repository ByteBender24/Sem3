'''
The Iterator Pattern is a behavioral design pattern that provides a way to access the elements of a collection 
sequentially without exposing its underlying representation. It defines a common interface for traversing 
different types of collections, allowing the client to iterate over elements without knowing the internal structure of the collection.

Key components of the Iterator Pattern:

    Iterator Interface: Defines an interface with methods like has_next() and next() for accessing elements sequentially.
    Concrete Iterator: Implements the Iterator Interface and keeps track of the current position within the collection.
    Aggregate Interface: Defines an interface for creating iterators.
    Concrete Aggregate: Implements the Aggregate Interface and provides an implementation for creating an iterator.
    Client: Uses the iterator to traverse the elements of the collection.
'''

from abc import ABC, abstractmethod

# Iterator Interface


# class Iterator(ABC):
#     @abstractmethod
#     def has_next(self):
#         pass

#     @abstractmethod
#     def next(self):
#         pass

# # Concrete Iterator


# class ConcreteIterator(Iterator):
#     def __init__(self, collection):
#         self.collection = collection
#         self.index = 0

#     def has_next(self):
#         return self.index < len(self.collection)

#     def next(self):
#         if self.has_next():
#             result = self.collection[self.index]
#             self.index += 1
#             return result
#         else:
#             raise StopIteration

# # Aggregate Interface


# class Aggregate(ABC):
#     @abstractmethod
#     def create_iterator(self):
#         pass

# # Concrete Aggregate


# class ConcreteAggregate(Aggregate):
#     def __init__(self, data):
#         self.data = data

#     def create_iterator(self):
#         return ConcreteIterator(self.data)

# # Client


# def client_code(aggregate):
#     iterator = aggregate.create_iterator()

#     while iterator.has_next():
#         element = iterator.next()
#         print(element)


# # Usage
# data_collection = [1, 2, 3, 4, 5]
# aggregate = ConcreteAggregate(data_collection)
# client_code(aggregate)


#--------------------------------
#usign trees

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTreeInOrderIterator:
    def __init__(self, root):
        self.root = root
        self.stack = []

    def __iter__(self):
        return self

    def __next__(self):
        while self.root or self.stack:
            if self.root:
                print('self.root_old', self.root)

                self.stack.append(self.root)
                self.root = self.root.left
                print('self.root' , self.root)
            else:
                node = self.stack.pop()
                value = node.value
                self.root = node.right
                return value
        raise StopIteration


# Example usage:
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Use the iterator for in-order traversal
iterator = BinaryTreeInOrderIterator(root)
for value in iterator:
    print(value)
