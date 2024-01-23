# super() for multiple inheritance with multiple arguments and polymorphism

class A():
    def __init__(self, *args, **kwargs):
        kw_a = kwargs
        args_a = args
        super().__init__(*args, **kwargs)
        self.var1 = 50  # given a default value to check whether it can be changed permanently
        self.x = 30

    def fun(self):
        print("I'm function 1")


class B(A):
    def __init__(self, var2, *args, **kwargs):
        kw_b = kwargs
        args_b = args
        super().__init__(*args, **kwargs)
        self.var2 = var2

    def fun(self):
        super().fun()
        print("I'm function 2")


class C(A):
    def __init__(self, var3, *args, **kwargs):
        kw_c = kwargs
        args_c = args
        super().__init__(*args, **kwargs)
        self.var3 = var3
        self.var1 = 40  # changed var1 to 40

    def fun(self):
        super().fun()
        print("I'm function 3")


class D(B, C):
    def __init__(self, var4, *args, **kwargs):
        kw_d = kwargs
        args_d = args
        super().__init__(*args, **kwargs)
        self.var4 = var4

    def fun(self):
        super().fun()
        print("I'm function 4")


d = D(10, 20, 30)
print(D.__mro__)
print(vars(d))
print(d.var1, d.var2, d.var3, d.var4, d.x)


'''
If it;s super confusing, then remove var1 and x to make it simple
know this always
super always points to next class in mro (not the base class always)
'''


'''
D.__init__(self, var4, *args, **kwargs) - super().__init__(*args, **kwargs) (from class B):

class B.__init__(self, var2, *args, **kwargs) is called.
super().__init__(*args, **kwargs) invokes the __init__ method of the next class in MRO, which is class C.
class C.__init__(self, var3, *args, **kwargs) is called.
class C.__init__(self, var3, *args, **kwargs) - super().__init__(*args, **kwargs) (from class A):

class A.__init__(self, *args, **kwargs) is called.
super().__init__(*args, **kwargs) invokes the __init__ method of the next class in MRO, which is the base class object.
class A.__init__(self, *args, **kwargs):

self.var1 = 50 sets the value of var1 in the instance to 50.
self.x = 30 sets the value of x in the instance to 30.
class C.__init__(self, var3, *args, **kwargs) continues:

self.var3 = var3 sets the value of var3 in the instance to 30.
self.var1 = 40 changes the value of var1 in the instance to 40.
class B.__init__(self, var2, *args, **kwargs) continues:

self.var2 = var2 sets the value of var2 in the instance to 20.
class D.__init__(self, var4, *args, **kwargs) continues:

self.var4 = var4 sets the value of var4 in the instance to 10.
After these steps, the object d is fully initialized.
'''

d.fun()

a = A()  # created an other object for A class and printed the value of var1
print("var1 for object named as d", d.var1)
print("var1 for other object ", a.var1)


'''summary : an instance variable of inherited class (parent class) can be changed with in an object and
can't be changed permenantly but with in that object of the class it can be changed anytime and
follows last recently updated value  once an anthor object is created  for same parent class
it will regain its default value'''
