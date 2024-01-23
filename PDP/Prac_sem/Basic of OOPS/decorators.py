'''
In Python, decorators are a powerful and flexible way to modify or 
extend the behavior of functions or methods without changing their code. 
They use the @decorator syntax and are applied to functions or methods to
enhance or wrap their functionality. Decorators are commonly used for tasks 
such as logging, timing, memoization, access control, and more.

What is a Decorator?
A decorator is a higher-order function that takes a function as input and 
returns a new function with extended or modified functionality.
'''


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        x = func()
        print("Something is happening after the function is called.")
        return x
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")
    return 10


# Calling the decorated function
x = say_hello()
print(x)


print("\n\n")


#--------------------decorators with arguments-------------

#TODO there is a problem with accessing and returning the values, view once again.
def dec_with_arg(arg):
    def dec_inside(func):
        print("decorator with arguments!")
        x = 10 + func()
        print(arg)
        return x
    return dec_inside

@dec_with_arg("Argument that was passed!")
def my_function():
    return 10


result = my_function
print(result)