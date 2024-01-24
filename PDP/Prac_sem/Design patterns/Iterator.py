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


from typing import Iterable, Iterator
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

# -------------------------------------------------------------------------------------------------
print("\n\n")

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
# -------------------------------------------------------------------------------------------------
print("\n\n")


class student:

    def __init__(self, name, mark, club):
        self.name = name
        self.mark = mark
        self.club = club

    def __str__(self):
        # result=''
        result = self.name+'\n'+str(self.mark)+'\n'+self.club
        return result


class iterable_student(Iterable):

    def __init__(self, *args):
        self.student_list = [*args]

    def append(self, obj):
        self.student_list.append(obj)

    def __iter__(self):
        return iterator_student(self.student_list)


class iterator_student(Iterator[str]):

    def __init__(self, iterable_list):
        self.iterator_list = [x for x in iterable_list if x.club == 'nss']
        self.index = 0

    def __next__(self):
        if self.index < len(self.iterator_list):
            x = self.iterator_list[self.index]
            self.index += 1
            return x
        else:
            raise StopIteration


a = student('xyz1', 10, 'nss')
b = student('xyz2', 20, 'nso')
c = student('xyz3', 30, 'yrc')
d = student('xyz4', 40, 'nss')
e = student('xyz5', 50, 'nso')
# f=student('xyz6',60,'yrc')
# g=student('xyz7',70,'nss')
# h=student('xyz8',80,'nso')
# i=student('xyz9',90,'yrc')
# j=student('xyz10',100,'nss')

iterable_student_list = iterable_student(a, b, c, d)
iterable_student_list.append(e)
# iterable_student_list.append(f)
# iterable_student_list.append(g)
# iterable_student_list.append(h)
# iterable_student_list.append(i)
# iterable_student_list.append(j)


for i in iterable_student_list:
    print(i)


# -------------------------------------------------------------------------------------------------
print("\n\n")


# Define an iterable interface
class Iterable:
    def create_iterator(self):
        pass

# Define an iterator interface


class Iterator:
    def has_next(self):
        pass

    def next(self):
        pass

# Concrete implementation of an iterable


class ConcreteIterable(Iterable):
    def __init__(self):
        self._data = [1, 2, 3, 4, 5]

    def create_iterator(self):
        return ConcreteIterator(self)

# Concrete implementation of an iterator


class ConcreteIterator(Iterator):
    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0

    def has_next(self):
        return self._index < len(self._iterable._data)

    def next(self):
        if self.has_next():
            value = self._iterable._data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration("No more elements")


# Client code
iterable = ConcreteIterable()
iterator = iterable.create_iterator()

while iterator.has_next():
    value = iterator.next()
    print(value)
