from typing import Dict

# Flyweight Interface


class FontFlyweight:
    def render_text(self, text):
        pass

# Concrete Flyweight


class ConcreteFontFlyweight(FontFlyweight):
    def __init__(self, font_name, font_size):
        self.font_name = font_name
        self.font_size = font_size

    def render_text(self, text):
        print(
            f"Rendering '{text}' with {self.font_name}, size {self.font_size}")

# Flyweight Factory


class FontFlyweightFactory:
    def __init__(self):
        self.fonts: Dict[str, FontFlyweight] = {}

    def get_font(self, font_name, font_size):
        key = f"{font_name}_{font_size}"
        if key not in self.fonts:
            self.fonts[key] = ConcreteFontFlyweight(font_name, font_size)
        return self.fonts[key]

# Client Code (Text Editor)


class TextEditor:
    def __init__(self, font_factory):
        self.font_factory = font_factory

    def set_text(self, text, font_name, font_size):
        font = self.font_factory.get_font(font_name, font_size)
        font.render_text(text)


# Application
if __name__ == "__main__":
    font_factory = FontFlyweightFactory()

    editor = TextEditor(font_factory)
    editor.set_text("Hello, World!", "Arial", 12)

    another_editor = TextEditor(font_factory)
    another_editor.set_text("Flyweight Pattern", "Arial", 12)


# -------------------------------------------------------------------------------------------------
print("\n\n")

# Flyweight Interface


class Shape:
    def draw(self, x, y):
        pass

# Concrete Flyweight


class Circle(Shape):
    def __init__(self, color):
        self.color = color

    def draw(self, x, y):
        print(f"Drawing a {self.color} circle at ({x}, {y})")

# Flyweight Factory


class ShapeFactory:
    def __init__(self):
        self.circle = {}

    def get_circle(self, color):
        if color not in self.circle:
            self.circle[color] = Circle(color)
        return self.circle[color]

# Client Code


class DrawingApp:
    def __init__(self, shape_factory):
        self.shape_factory = shape_factory
        self.shapes = []

    def add_circle(self, color, x, y):
        circle = self.shape_factory.get_circle(color)
        self.shapes.append((circle, x, y))

    def draw_shapes(self):
        for shape, x, y in self.shapes:
            shape.draw(x, y)


# Application
if __name__ == "__main__":
    shape_factory = ShapeFactory()

    drawing_app = DrawingApp(shape_factory)
    drawing_app.add_circle("Red", 10, 10)
    drawing_app.add_circle("Blue", 20, 20)
    drawing_app.add_circle("Red", 30, 30)

    drawing_app.draw_shapes()
