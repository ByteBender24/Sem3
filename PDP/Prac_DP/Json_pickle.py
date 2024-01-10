# -----------------------------------------PICKLING------------------------------
import pickle

# Example class to pickle


class ExampleClass:
    def __init__(self, name):
        self.name = name

# Pickling (serialization)


def pickle_object(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)

# Unpickling (deserialization)


def unpickle_object(filename):
    with open(filename, 'rb') as file:
        obj = pickle.load(file)
    return obj


# Example Usage
# Create an object
original_object = ExampleClass("ExampleObject")

# Pickle the object to a file
pickle_object(original_object, 'example.pickle')

# Unpickle the object from the file
unpickled_object = unpickle_object('example.pickle')

# Check if unpickled object is equal to the original
print("Original Object:", original_object.name)
print(original_object)
print(unpickled_object)
print("Unpickled Object:", unpickled_object.name)
print("Objects are equal:", original_object == unpickled_object)

# -----------------------------------------------------------dict - object conversions----------------------------------------------------
# conversion of dict to object and object to dict

data_dict = {'name': 'John', 'age': 25, 'city': 'New York'}


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


# Create an instance of the class using the JSON data
person_instance = Person(**data_dict)

# Convert the class instance to a dictionary
person_dict = vars(person_instance)
print(person_dict)
