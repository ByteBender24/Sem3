'''
The Factory Method Pattern is a creational design pattern that provides an interface for creating objects in a superclass 
but allows subclasses to alter the type of objects that will be created. This pattern defines an interface for creating an object but 
leaves the choice of its type to the subclasses, creating an instance of one of several possible classes.
'''

from abc import ABC, abstractmethod

# Abstract Product


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"

# Abstract Creator


class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# Concrete Creators


class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()


class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# Client Code


def get_pet_sound(animal_factory):
    animal = animal_factory.create_animal()
    return animal.speak()


# Using the Factory Method
dog_factory = DogFactory()
cat_factory = CatFactory()

dog_sound = get_pet_sound(dog_factory)
cat_sound = get_pet_sound(cat_factory)

print(dog_sound)  # Output: Woof!
print(cat_sound)  # Output: Meow!
