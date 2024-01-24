def my_generator(n):
    value = 0

    while value < n:

        yield value
        value += 1


for value in my_generator(3):

    print(value)
# -------------------------------------

# squares_generator = (i * i for i in range(5))


# for i in squares_generator:
#     print(i)

# -------------------------------------------------------------------------------------------------
print("\n\n")


def fib(limit):
    a = 0
    b = 1
    while a < limit:
        yield a
        a = b
        b = a + b


x = fib(5)  # generator object

# Iterating using next
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# print(next(x))

# Iterating using for in loop.
print("\nUsing for in loop")
for i in fib(5):
	print(i)

