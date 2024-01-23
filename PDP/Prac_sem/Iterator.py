'''
ITERABLE:
An iterable is typically a container that holds all the elements that are to be
iterated over. For example, a list or a tuple in Python. The elements of the
iterable are stored in memory.

ITERATOR:
• An iterator is an object that generates the elements of the iterable on the fly,
as they are requested. An iterator does not store all the elements of the
iterable in memory at once. Instead, it generates them one by one, only when
needed.

Iterators allow lazy evaluation, only generating the next element of an iterable
object when requested. This is useful for very large data sets.

• Lazy evaluation is a strategy whereby certain objects are only produced
when required. Consequently, certain developer circles also refer to lazy
evaluation as “call-by-need”

not all iterables are iterators
list = [1,2]
next(list) ---> error


Python automatically produces an iterator object whenever you attempt to
loop through an iterable object.

like
for iterator in iterable:
    print(iterator)

list ---> iterator (by iter func)
likewise using list function we can reverse
'''


class MyIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration


# Using the iterator
my_iterator = MyIterator(5)

for value in my_iterator:
    print(value)



'''RANGE CLASS

Creates a range object for a sequence of 10 million numbers and then calculates the sum of
the sequence.
• Even though the sequence has 10 million numbers, 
TODO 
    the range object only stores the
start, stop, and step values, and it generates each number on-the-fly as sum() iterates
over it.
• This saves a significant amount of memory compared to creating a list of 10 million
numbers, which would require a lot of memory to store in memory at once.

'''

myrange = range(10000)
print(sum(myrange))

'''GENERATORS

The most expedient alternative to implementing an iterator is to use a
generator.

• Although generators may look like ordinary Python functions, they are
different.
• For starters, a generator object does not return items. Instead, it uses
the yield keyword to generate items on the fly.
• Thus, we can say a generator is a special kind of function that
leverages lazy evaluation.
• Generators do not store their contents in memory as you would expect a
typical iterable to do.

Since we used the yield keyword instead of return, the function is not exited
after the run. In essence, we told Python to create a generator object
instead of a traditional function, which enables the state of the generator
object to be tracked.
• Consequently, it is possible to call the next() function on the lazy iterator to
show the elements of the series one at a time.
'''

# traditional way of iterable
def factors(n):
    factor_list = []
    for val in range(1, n+1):
        if n % val == 0:
            factor_list.append(val)
    return factor_list


print(factors(20))


#generator
def factors(n):
    for val in range(1, n + 1):
        if n % val == 0:
            yield val


factors_of_20 = factors(20)
print(factors_of_20)
print(next(factors_of_20))
print(next(factors_of_20))
print(next(factors_of_20))
print(next(factors_of_20))
print(next(factors_of_20))


'''
OUTPUT:
<generator object factors at 0x0000026DD6F4D7E0>
1
2
4
5
10
'''
