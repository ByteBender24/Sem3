class A():
    def __init__(self, a='a', *args, **kwargs):
        self.a = a 
        print(kwargs)

        super().__init__(*args, **kwargs)

class B():
    def __init__(self, b='b', *args, **kwargs):
        self.b = b
        print(kwargs)

        super().__init__(*args, **kwargs)

class C(A,B):
    def __init__(self, c='c', *args, **kwargs):
        self.c = c
        print(kwargs)
        super().__init__(*args  , **kwargs)

c_obj = C()
print(vars(c_obj))
d_obj=C(a='A',b='B',c='C')
print(vars(d_obj))
print(C.mro())


'''
use breakpoints and resolve how this works
this works exactly with kwargs, and mro

using mro - C --> A --> B 
when first it 
1) in C:
    c=C
    {'a': 'A', 'b': 'B'}

2) in A:
    a=A
    {'b': 'B'}

3) in B:
    b = B
    {}
'''
