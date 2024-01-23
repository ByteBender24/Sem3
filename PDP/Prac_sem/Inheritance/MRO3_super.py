# MULTIPLE INHERITANCE AND POLYMORPHISM
class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def test(self):
        # super().test()
        print("Contact")


class AddressHolder():
    def __init__(self, street):
        self.street = street

    def test(self):
        # super().test()
        print("Hello")


class Friend(Contact, AddressHolder):
    def __init__(self, phone, name, email, street):

        self.phone = phone
        # Contact.__init__(self,name,email)
        # AddressHolder.__init__(self,street)

    def test(self):
        super().test()
        print("Friend")


f1 = Friend("123", "John", "john@gmail.com", "street1")
f1.test()

# -------------------------------------------------------------------------------------------------
print("\n\n")

class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def test(self):
        super().test()
        print("contact")


class AddressHolder:
    def __init__(self, street):
        self.street = street

    def test(self):

        print("Hello")


class Friend(Contact, AddressHolder):
    def __init__(self, phone, name, email, street):

        self.phone = phone
        # Contact.__init__(self,name,email)
        # AddressHolder.__init__(self,street)

    def test(self):
        print("FRIEND")
        super().test()


f1 = Friend("123", "John", "john@gmail.com", "street1")
f1.test()

'''
How MRO Works in This Example:
Initialization of Object (f1):

An instance of the Friend class (f1) is created with arguments "123", "John", "john@gmail.com", and "street1".
The __init__ methods of the parent classes (Contact and AddressHolder) are not explicitly called.
Method Invocation (f1.test()):

The test method of the Friend class is invoked.
It prints "FRIEND" and then calls super().test(). This super() refers to the next class in the MRO, which is Contact.
Method in Contact Class (super().test()):

The test method in the Contact class is invoked.
It prints "contact" and calls super().test(). However, since Contact is the last class in the hierarchy, there is no superclass to call.
Method Resolution Order (MRO) Recap:

The MRO (Friend -> Contact -> AddressHolder -> object) explains the order in which classes are searched for methods.
In the case of the test method, it is resolved in the order: Friend -> Contact -> object.


Key Takeaways:
MRO defines the order in which base classes are searched when resolving methods.
super() refers to the next class in the MRO.
The MRO is determined by the order of base classes in the inheritance hierarchy.
'''

'''
OUTPUT:

Contact
Friend 
       
       
       
FRIEND 
Hello  
contact
'''