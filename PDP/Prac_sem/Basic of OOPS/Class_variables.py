class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age


# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing class attribute
print(f"{dog1.name} belongs to the species {dog1.species}")
print(f"{dog2.name} belongs to the species {dog2.species}")

dog1.species = "Canum lupus"
print(dog1.species)
print(dog2.species)
print(Dog.species)

""" 
Output:

Buddy belongs to the species Canis familiaris
Max belongs to the species Canis familiaris
Canum lupus
Canis familiaris
Canis familiaris """


# Modifying class attribute
Dog.species = "Canis lupus familiaris"

# The class attribute is updated for all instances
print(f"Now, {dog1.name} belongs to the species {dog1.species}")
print(f"Now, {dog2.name} belongs to the species {dog2.species}")


'''
Output:
Now, Buddy belongs to the species Canum lupus
Now, Max belongs to the species Canis lupus familiaris

from this we can say, we can change class variables by:
class.attr 

but if obj.class_attr is changed, then even if class.attr is changed, no changes for that obj alone

'''
