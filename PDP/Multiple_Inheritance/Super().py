class A:
    def m(self):
        print("A")

class X(A):

    def m(self):
        super().m()
        print ("X")

class Y(A):

    def m(self):
        super().m()
        print("Y")

class Z(X, Y):

    def m(self):
        super().m()

z = Z()
z.m()