'''
The Template Method Pattern is a behavioral design pattern that defines the skeleton of an algorithm in the superclass 
but lets subclasses override specific steps of the algorithm without changing its structure.
 It allows a method's steps to be defined by its subclasses while keeping the overall algorithm structure in place.
'''

from abc import ABC, abstractmethod

# Abstract Class (Template)


class AbstractClassTemplate(ABC):
    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    @abstractmethod
    def step_three(self):
        pass

# Concrete Class 1


class ConcreteClass1(AbstractClassTemplate):
    def step_one(self):
        print("ConcreteClass1: Step One")

    def step_two(self):
        print("ConcreteClass1: Step Two")

    def step_three(self):
        print("ConcreteClass1: Step Three")

# Concrete Class 2


class ConcreteClass2(AbstractClassTemplate):
    def step_one(self):
        print("ConcreteClass2: Step One")

    def step_two(self):
        print("ConcreteClass2: Step Two")

    def step_three(self):
        print("ConcreteClass2: Step Three")

# Client Code


def client_code(template):
    template.template_method()


# Usage
template1 = ConcreteClass1()
template2 = ConcreteClass2()

client_code(template1)
client_code(template2)
