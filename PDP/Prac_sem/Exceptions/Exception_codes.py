""" '''Raising an exception'''

class EvenOnly(list):
    def append(self, value):
        if not isinstance(value, int):
            raise TypeError("Only integers can be added")
        if value % 2 != 0:
            raise ValueError("Only even numbers can be added")
        super().append(value)


e = EvenOnly()
e.append(10)
print(e)
# e.append(13)
e.append('a')
print(e)

# -------------------------------------------------------------------------------------------------
print("\n\n")

class CustomError(Exception):
    def __init__(self, message="A custom error occurred"):
        super().__init__(message)


def some_function(x):
    if x < 0:
        raise CustomError("Input value should be non-negative")


try:
    some_function(-5)
except CustomError as ce:
    print(f"Custom Error: {ce}")
else:
    print("No error occurred")
 """
# -------------------------------------------------------------------------------------------------
print("\n\n")


'''IN BUILT ERRORS IN PYTHON'''

# print "hi"        #--> Syntax error

# x=10/0        #--> ZeroDivisionError

lst = [1, 2, 3]
# print(lst[5])            # --> IndexError

# lst+1             # --> TypeError

# lst.add            # --> AttributeError

x = {'a': 'hi'}
# print(x['b'])                   #--> KeyError

# print(hi)               #NameError : hi is not defined

# -------------------------------------------------------------------------------------------------
print("\n\n")

'''STOP ITERATION ERROR

only handled inside __next__ block in iterator class
'''

y = [1, 2, 3]
x = iter(y)
print(x.__next__())
print(x.__next__())
print(x.__next__())
# print(x.__next__())

# -------------------------------------------------------------------------------------------------
print("\n\n")


def funniest_division(divisor):
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divisor
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        return ("divisor does not match")
    except ValueError:
        print("13!")
        return ("divisor doe not match")


result = funniest_division(13)
print(result)

# -------------------------------------------------------------------------------------------------
print("\n\n")

'''Handling an exception'''


class EvenOnly(list):
    def append(self, value):
        try:
            if isinstance(value, int):
                pass
            if value % 2 != 0:
                pass
        except:
            print("type error occured")
        try:
            if value % 2 != 0:
                pass
        except:
            print("Value error occured")
        super().append(value)


e = EvenOnly()
e.append(10)
print(e)
e.append(13)
print(e)
e.append('a')
# print(type('a'))
print(e)

# -------------------------------------------------------------------------------------------------
print("\n\n")

# Add the exception types you want to raise
some_exceptions = [ValueError, TypeError, None, Exception]

for choice in some_exceptions:
    try:
        print(f"\nRaising {choice}")
        if choice:
            raise choice("An error")
        else:
            print("no exception raised")
    except ValueError:
        print("Caught a ValueError")
    except TypeError:
        print("Caught a TypeError")
    except Exception as e:
        print(f"Caught some other error: {e.__class__.__name__}")
    else:
        print("This code called if there is no exception")
    finally:
        print("This cleanup code is always called")

'''
In Python, the try, except, else, and finally blocks are used for exception handling. They provide a way to structure code that might raise exceptions and handle those exceptions gracefully. Here's an overview of each block:

try Block:

The try block is used to enclose a section of code that might raise an exception.
If an exception occurs within the try block, the control immediately moves to the corresponding except block.
If no exception occurs, the except block is skipped.
python
Copy code
try:
    # Code that might raise an exception
    result = perform_operation()
except SomeException as e:
    # Handle the exception
    print(f"An error occurred: {e}")
except Block:

The except block is used to handle specific exceptions that might occur within the corresponding try block.
Multiple except blocks can be used to handle different types of exceptions.
If an exception occurs, the first matching except block is executed, and then control moves to the next block after the try-except structure.

try:
    result = perform_operation()
except ValueError as ve:
    # Handle ValueError
    print(f"ValueError: {ve}")
except TypeError as te:
    # Handle TypeError
    print(f"TypeError: {te}")
else Block:

The else block is executed if no exception occurs in the corresponding try block.
It is often used for code that should run only when there is no exception.
python
Copy code
try:
    result = perform_operation()
except ValueError as ve:
    # Handle ValueError
    print(f"ValueError: {ve}")
else:
    # Code to run when there is no exception
    print("Operation successful.")
finally Block:

The finally block is used to define cleanup code that should be executed regardless of whether an exception occurs or not.
It is commonly used for releasing resources, closing files, or any other cleanup operations.
python
Copy code
try:
    result = perform_operation()
except ValueError as ve:
    # Handle ValueError
    print(f"ValueError: {ve}")
finally:
    # Cleanup operations
    cleanup()
These blocks can be combined to create a comprehensive exception-handling structure.
 The order is typically try, except, else, and finally. 
 However, not all blocks are mandatory; you can use only the ones that are necessary for your specific requirements.
'''