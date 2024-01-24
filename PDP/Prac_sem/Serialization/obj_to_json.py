import json


class Address:
    def __init__(self, city, zip_code):
        self.city = city
        self.zip_code = zip_code


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_json(self):
        return json.dumps(self, default=lambda obj: obj.__dict__ if hasattr(obj, '__dict__') else str(obj), indent=2)


# Create an instance of the class
address = Address("New York", "10001")
person = Person("John", 30, address)
print(str(person))
print(str(address))
# Convert the class object to JSON format
json_data = person.to_json()

# Print the JSON representation
print(json_data)

# -------------------------------------------------------------------------------------------------
print("\n\n")


class Address:
    def __init__(self, city, zip_code):
        self.city = city
        self.zip_code = zip_code

    def to_dict(self):
        return self.__dict__


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address.to_dict()  # Convert nested object to a dictionary
        }


# Create an instance of the classes
address = Address("New York", "10001")
person = Person("John", 30, address)

# Convert the class object to a dictionary
person_dict = person.to_dict()

# Convert the dictionary to JSON format
json_data = json.dumps(person_dict, indent=2)

# Print the JSON representation
print(json_data)


