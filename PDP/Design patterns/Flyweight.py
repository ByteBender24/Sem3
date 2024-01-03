'''
The Flyweight Pattern is a structural design pattern that is used to minimize memory usage or computational e
xpenses by sharing as much as possible with related objects. 
It is particularly useful when a large number of similar objects 
need to be created, and memory efficiency is a concern.
'''


import random
class Character:
    def __init__(self, symbol, font, size):
        self.symbol = symbol
        self.font = font
        self.size = size

    def display(self):
        print(
            f"Character: {self.symbol}, Font: {self.font}, Size: {self.size}")


class CharacterFactory:
    _characters = {}

    def get_character(self, symbol, font, size):
        key = (symbol, font, size)
        if key not in self._characters:
            self._characters[key] = Character(symbol, font, size)
        return self._characters[key]


class Text:
    def __init__(self):
        self.characters = []

    def add_character(self, symbol, font, size):
        character = character_factory.get_character(symbol, font, size)
        self.characters.append(character)

    def display(self):
        for character in self.characters:
            character.display()


# Client code
character_factory = CharacterFactory()
text = Text()

text.add_character("A", "Arial", 12)
text.add_character("B", "Times New Roman", 14)
text.add_character("A", "Arial", 12)  # Reusing existing character

text.display()


class Circle:
    def __init__(self, color):
        self.color = color

    def draw(self, x, y, radius):
        print(
            f"Drawing a {self.color} circle at ({x}, {y}) with radius {radius}")


class CircleFactory:
    _circle_colors = {}

    def get_circle(self, color):
        if color not in self._circle_colors:
            self._circle_colors[color] = Circle(color)
        return self._circle_colors[color]


class Canvas:
    def __init__(self):
        self.circles = []

    def add_circle(self, color, x, y, radius):
        circle = circle_factory.get_circle(color)
        self.circles.append((circle, x, y, radius))

    def draw_circles(self):
        for circle, x, y, radius in self.circles:
            circle.draw(x, y, radius)


# Client code
circle_factory = CircleFactory()
canvas = Canvas()

# Adding circles with shared colors
canvas.add_circle("Red", 10, 20, 5)
canvas.add_circle("Blue", 30, 40, 8)
canvas.add_circle("Red", 50, 60, 6)  # Reusing color "Red"

# Drawing circles
canvas.draw_circles()

