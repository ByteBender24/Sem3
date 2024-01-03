'''
The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families 
of related or dependent objects without specifying their concrete classes. It involves defining interfaces 
for creating families of related or dependent objects, and concrete implementations for those interfaces.

Key components of the Abstract Factory Pattern:

Abstract Factory: Declares an interface for creating a family of products.

Concrete Factory: Implements the Abstract Factory interface and creates a family of related products.

Abstract Product: Declares an interface for a type of product.

Concrete Product: Implements the Abstract Product interface.

Client: Uses the Abstract Factory and Abstract Product interfaces to create families of related or dependent objects.
'''


from abc import ABC, abstractmethod

# Abstract Product A


class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self):
        pass

# Concrete Product A1


class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        return "ConcreteProductA1 operation_a"

# Concrete Product A2


class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        return "ConcreteProductA2 operation_a"

# Abstract Product B


class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self):
        pass

# Concrete Product B1


class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        return "ConcreteProductB1 operation_b"

# Concrete Product B2


class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        return "ConcreteProductB2 operation_b"

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

# Client


def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    result_a = product_a.operation_a()
    result_b = product_b.operation_b()

    print(result_a)
    print(result_b)


# Usage
factory1 = ConcreteFactory1()
factory2 = ConcreteFactory2()

client_code(factory1)
client_code(factory2)
