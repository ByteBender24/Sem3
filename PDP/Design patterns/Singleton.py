'''
The Singleton Pattern is a design pattern that ensures a class has only one instance and provides a 
global point of access to that instance. This pattern is useful when you want to control access to a single
instance of a class and prevent multiple instances from being created. 
It is often used for logging, database connections, and configuration settings.
'''

class Singleton:
    _instance = None  # Private variable to hold the single instance

    def __new__(cls):
        # Override __new__ to control the instance creation
        if not cls._instance:
            # If the instance doesn't exist, create one
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = None  # Optional: Initialize instance variables
        return cls._instance

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

# Example usage:


# Create two instances of Singleton
singleton1 = Singleton()
singleton2 = Singleton()

# Check if both instances are the same
print(singleton1 is singleton2)  # Output: True

# Set a value in one instance
singleton1.set_value(42)

# Retrieve the value from the other instance
print(singleton2.get_value())  # Output: 42
