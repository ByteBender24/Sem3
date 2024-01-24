# The Abstract Factory Pattern is a creational design pattern that provides an interface for
# creating families of related or dependent objects without specifying their concrete classes.
# It allows a client to use an abstract interface to create a set of related objects
# without needing to know the specific classes of those objects.

from abc import ABC, abstractmethod

# Abstract Product A


class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self):
        pass

# Concrete Product A1


class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        return "Product A1 operation"

# Concrete Product A2


class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        return "Product A2 operation"

# Abstract Product B


class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self):
        pass

# Concrete Product B1


class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        return "Product B1 operation"

# Concrete Product B2


class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        return "Product B2 operation"

# Abstract Factory


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

# Concrete Factory 1


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

# Concrete Factory 2


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

# Client Code


def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(product_a.operation_a())
    print(product_b.operation_b())


# Application
if __name__ == "__main__":
    factory1 = ConcreteFactory1()
    client_code(factory1)

    print("\n")

    factory2 = ConcreteFactory2()
    client_code(factory2)
