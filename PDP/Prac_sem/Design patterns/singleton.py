class Singleton2:

  __instance = None

  def __new__(cls):

    if (cls.__instance is None):

      cls.__instance = super(Singleton2, cls).__new__(cls)

    return cls.__instance


s1 = Singleton2()
print(s1)
s2 = Singleton2()
print(s2)

s1.x = 5
print(s1.x)

s2.x = 15
print(s2.x)

print(s1.x)

# -------------------------------------------------------------------------------------------------
print("\n\n")


class Singleton1:

  instance = None

  def __init__(self):
    if Singleton1.instance != None:
       raise Exception("Singleton object already created!")
    else:
       Singleton1.instance = self


s3 = Singleton1()
print(s3)
s1 = Singleton1()
print(s1)

# -------------------------------------------------------------------------------------------------
print("\n\n")


class Singleton1:

  instance = None

  def __init__(self):
    if Singleton1.instance != None:
       raise Exception("Singleton object already created!")
    else:
       Singleton1.instance = self

  @staticmethod
  def getInstance():
    if Singleton1.instance == None:
      Singleton1()
    return Singleton1.instance


s1 = Singleton1.getInstance()
print(s1)
s2 = Singleton1.getInstance()
print(s2)

s1.x = 5
print(s1.x)
s2.x = 10
print(s2.x)
print(s1.x)

# s3=Singleton1()

# -------------------------------------------------------------------------------------------------
print("\n\n")

'''
static method
'''


class Subject():

    sub_name = 'PDP'  # class attribute

    def __init__(self):
        self.code = 12345  # instance attribute

    @staticmethod
    def display():
       sub_name = 'DS'
       sub_code = 1111
       print(sub_name, sub_code)


sub = Subject.display()

subj = Subject()
subj.display()

# -------------------------------------------------------------------------------------------------
print("\n\n")

'''
class method
'''


class Subject():

    sub_name = 'PDP'  # class attribute

    def __init__(self):
        self.code = 12345  # instance attribute

    @classmethod
    def display(cls):
        print('Subject Name is:', cls.sub_name)


sub = Subject()
sub1 = Subject()
sub.display()
print(sub.code)
print(sub)
print(sub1)
