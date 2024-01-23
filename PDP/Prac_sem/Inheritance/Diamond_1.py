# USE OF MRO ALGORITHM

class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print("Calling method on BaseClass")
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on LeftSubclass")
        self.num_left_calls += 1


class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on RightSubclass")
        self.num_right_calls += 1


class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        self.num_sub_calls += 1


subclass = Subclass()
subclass.call_me()

print(Subclass.mro())

print(subclass.num_sub_calls, subclass.num_left_calls,
      subclass.num_right_calls, subclass.num_base_calls)

print(Subclass.num_sub_calls, LeftSubclass.num_left_calls,
      RightSubclass.num_right_calls, BaseClass.num_base_calls)




"""
OUTPUT:
Calling method on BaseClass
Calling method on RightSubclass
Calling method on LeftSubclass
Calling method on Subclass
1 1 1 1
0 0 0 0
(<class '__main__.Subclass'>,
 <class '__main__.LeftSubclass'>,
 <class '__main__.RightSubclass'>,
 <class '__main__.BaseClass'>,
 <class 'object'>)
 """


# -------------------------------------------------------------------------------------------------
print("\n\n")


class A:
    def rk(self):
        print("In class A")


class B(A):
    def rk(self):
        print("In class B")


class C(A):
    def rk(self):
        print("In class C")


class D(B, C):
    pass


# Create an instance of class D
r = D()
r.rk()

'''
In class B
'''

# -------------------------------------------------------------------------------------------------
print("\n\n")
class A:
    def rk(self):
        print("In class A")


class B(A):
    def rk(self):
        super().rk()
        print("In class B")


class C(A):
    def rk(self):
        print("In class C")


class D(B, C):
    pass


# Create an instance of class D
r = D()
r.rk()

'''In class C
In class B'''

#-------------------------------------------------------------------------------------------------
print("\n\n")

class A:
    def rk(self):
        print("In class A")


class B(A):
    def rk(self):
        super().rk()
        print("In class B")


class C(A):
    def rk(self):
        super().rk()
        print("In class C")


class D(B, C):
    pass


# Create an instance of class D
r = D()
r.rk()

'''
In class A
In class C
In class B
'''