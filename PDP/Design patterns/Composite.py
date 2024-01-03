'''
The Composite Pattern is a structural design pattern that lets you 
compose objects into tree structures to represent part-whole hierarchies. 
It allows clients to treat individual objects and compositions of objects uniformly.
This pattern is particularly useful when you need to work with objects that form a tree-like structure and 
you want to treat both individual objects and compositions of objects in a uniform way.
'''

from abc import ABC, abstractmethod

# Component interface


class FileSystemComponent(ABC):
    @abstractmethod
    def display(self):
        pass

# Leaf class (individual file)


class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"File: {self.name}")

# Composite class (directory containing files or subdirectories)


class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.display()


# Client code
file1 = File("Document.txt")
file2 = File("Image.jpg")

subdirectory = Directory("Subfolder")
file3 = File("Note.txt")

root_directory = Directory("Root")
root_directory.add_child(file1)
root_directory.add_child(file2)
root_directory.add_child(subdirectory)

subdirectory.add_child(file3)

# Display the entire file system
root_directory.display()

#-----------------------------------------------------------------------------------------------------------------------------------
# Component interface


class GraphicShape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Leaf class (individual shape)


class Circle(GraphicShape):
    def draw(self):
        print("Drawing Circle")

# Leaf class (individual shape)


class Rectangle(GraphicShape):
    def draw(self):
        print("Drawing Rectangle")

# Composite class (group of shapes)


class Group(GraphicShape):
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw(self):
        print("Drawing Group:")
        for shape in self.shapes:
            shape.draw()


# Client code
circle1 = Circle()
circle2 = Circle()
rectangle1 = Rectangle()

group = Group()
group.add_shape(circle1)
group.add_shape(rectangle1)

# Create another group containing circles
group_of_circles = Group()
group_of_circles.add_shape(circle2)

# Add the group of circles to the main group
group.add_shape(group_of_circles)

# Draw the entire graphic
group.draw()
