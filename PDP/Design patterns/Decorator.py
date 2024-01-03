'''
The Decorator Pattern is a structural design pattern that allows behavior to be added to an individual object, 
either statically or dynamically, without affecting the behavior of other objects from the same class. This pattern is 
used to extend the functionalities of classes in a flexible and reusable way.
'''

from abc import ABC, abstractmethod

# Component Interface


class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

# Concrete Component


class SimpleCoffee(Coffee):
    def cost(self):
        return 5

# Decorator


class CoffeeDecorator(Coffee, ABC):
    def __init__(self, coffee):
        self._coffee = coffee

    @abstractmethod
    def cost(self):
        pass

# Concrete Decorators


class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2


class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1


# Client Code
simple_coffee = SimpleCoffee()
print("Cost of simple coffee:", simple_coffee.cost())

milk_coffee = MilkDecorator(simple_coffee)
print("Cost of milk coffee:", milk_coffee.cost())

sugar_milk_coffee = SugarDecorator(milk_coffee)
print("Cost of sugar milk coffee:", sugar_milk_coffee.cost())


#--------------------------------------------------------------------------------------------------------

# Component Interface

class TextFormatter(ABC):
    @abstractmethod
    def format_text(self):
        pass

# Concrete Component


class PlainTextFormatter(TextFormatter):
    def format_text(self):
        return "Plain Text"

# Decorator


class TextDecorator(TextFormatter, ABC):
    def __init__(self, text_formatter):
        self._text_formatter = text_formatter

    @abstractmethod
    def format_text(self):
        pass

# Concrete Decorators


class BoldTextDecorator(TextDecorator):
    def format_text(self):
        return f"<b>{self._text_formatter.format_text()}</b>"


class ItalicTextDecorator(TextDecorator):
    def format_text(self):
        return f"<i>{self._text_formatter.format_text()}</i>"


# Client Code
plain_text = PlainTextFormatter()
print("Original Text:", plain_text.format_text())

bold_text = BoldTextDecorator(plain_text)
print("Bold Text:", bold_text.format_text())

italic_bold_text = ItalicTextDecorator(bold_text)
print("Italic Bold Text:", italic_bold_text.format_text())
