'''
The @property decorator is used to define a getter method (radius in this case).
The @radius.setter decorator is used to define a setter method for the same property.
The @radius.deleter decorator is used to define a deleter method for the property.

In Python, the property decorator is a built-in decorator that allows you to define a 
method that can be accessed like an attribute. It provides a way to create read-only or 
read-write properties in a class. The property decorator is often used to encapsulate the 
access and modification of an object's attributes by providing getter, setter, and deleter methods.

refer those other two of codes related to property decorator
'''

class Circle:
    def __init__(self, radius):
        # Note: Prefixing with '_' is a convention for indicating a "protected" attribute
        self._radius = radius

    @property
    def radius(self):
        """Getter method for the radius property."""
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        """Setter method for the radius property."""
        if isinstance(new_radius, (int, float)) and new_radius > 0:
            self._radius = new_radius
        else:
            raise ValueError("Radius must be a positive number.")

    @radius.deleter
    def radius(self):
        """Deleter method for the radius property."""
        print("Deleting the radius.")
        del self._radius


# Creating an instance of Circle
my_circle = Circle(5)

# Accessing the radius property using the getter
print(my_circle.radius)  # Output: 5

# Modifying the radius property using the setter
my_circle.radius = 8
print(my_circle.radius)  # Output: 8

# Deleting the radius property using the deleter
del my_circle.radius  # Output: Deleting the radius.
# print(my_circle.radius)  
