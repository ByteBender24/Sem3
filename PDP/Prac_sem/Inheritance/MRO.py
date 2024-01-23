class Emailable():
    def __init__(self, email):
        self.email = email


class MailSender(Emailable):
    def send_mail(self, message):
        self.message = message
        print(f"Sending mail to {self.email=}")


class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return (f"{self.name}, {self.email}")


'''c_1 = Contact("Dusty", "dusty@example.com")
c_2 = Contact("Steve", "steve@itmaybeahack.com")'''


class EmailableContact(Contact, MailSender):
    pass


e = EmailableContact("John B", "johnb@sloop.net")
print(Contact.all_contacts)
print(dir(EmailableContact))
print(dir(e))
print(vars(e))
e.send_mail("Hello, test e-mail here")

'''
so you are saying that, when i inheritet two classes, the mro checks for first class 
and uses its init to initialise, it will not use the second classes init?

ChatGPT
Yes, that's correct. When a class inherits from multiple classes, the order in which those classes are listed in 
the inheritance tuple (class EmailableContact(Contact, MailSender):) determines the method resolution order (MRO).

During object instantiation, the __init__ method of the first class in the MRO is called. 
If that class doesn't have an __init__ method or if it doesn't accept the required arguments, 
the interpreter looks for the __init__ method in the next class in the MRO. 
This process continues until a suitable __init__ method is found and called.'''

"""
OUTPUT:
[EmailableContact('John B', 'johnb@sloop.net')]
Sending mail to self.email='johnb@sloop.net'
"""

print(EmailableContact.__mro__)  #returns a tuple
# or
print(EmailableContact.mro())  #returns a list



