class Person:
    total_persons = 0  # class data member

    def __init__(self, name, age):
        self.name = name  # instance data member
        self.age = age  # instance data member
        Person.total_persons += 1  # accessing class data member

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    @classmethod
    # using cls keyword to access class data member
    def display_total_persons(cls):
        print("Total Persons:", cls.total_persons)


# Creating instances of the Person class
person1 = Person("John", 25)
person2 = Person("Alice", 30)

# Accessing instance attributes and calling the display method
person1.display()
person2.display()

# Accessing class data member through class method
Person.display_total_persons()

# Accessing class data member through an instance (not recommended)
print(person1.total_persons)

# Accessing class data member through the class name
print(Person.total_persons)

'''
the following is not recommended
as it is just making the class attr value change for only that object, and if we print if for
class.attr it is not changed, so do not access class attributes by objects
'''

person1.total_persons += 1
# Accessing class data member through an instance (not recommended)
print(person1.total_persons)

# Accessing class data member through the class name
print(Person.total_persons)


person1.display_total_persons()
