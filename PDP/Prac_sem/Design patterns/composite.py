# treats individual objects and compositions of objects uniformly.

from abc import ABC, abstractmethod


class Component(ABC):

  @abstractmethod
  def size(self):
    pass


class File(Component):

  def __init__(self, fname, fsize):
    self.fname = fname
    self.fsize = fsize

  def size(self):
    return self.fsize


class Folder(Component):

  def __init__(self, name, components):
    self.name = name
    self.components = components

  def size(self):
    total = 0
    for component in self.components:
      total = total+component.size()
    return total

  def add(self, component):
    self.components.append(component)


file1 = File("file1.doc", 100)
file2 = File("file2.doc", 200)
file3 = File("file3.pdf", 300)


folder1 = Folder("Folder1", [file1, file2, file3])


file4 = File("file4.txt", 400)
file5 = File("file5.txt", 500)


folder2 = Folder("Folder2", [file4, file5])

folder3 = Folder("Root", [folder1, folder2])

print(file1.size())
print(folder1.size())
print(folder3.size())

file6 = File("File6", 600)


folder3.add(file6)

print(folder3.size())

components = [folder1, folder2, folder3]

for component in components:
  print(component.size())

# -------------------------------------------------------------------------------------------------
print("\n\n")


# Component Interface

class FileSystemComponent(ABC):
    @abstractmethod
    def display(self):
        pass

# Leaf


class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"File: {self.name}")

# Composite


class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.display()


# Client Code
if __name__ == "__main__":
    file1 = File("file1.txt")
    file2 = File("file2.txt")

    directory1 = Directory("Folder 1")
    directory1.add(file1)

    directory2 = Directory("Folder 2")
    directory2.add(file2)

    root_directory = Directory("Root")
    root_directory.add(directory1)
    root_directory.add(directory2)

    # Displaying the file system structure
    root_directory.display()
