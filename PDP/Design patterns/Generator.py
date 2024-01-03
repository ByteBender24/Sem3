'''
A generator in Python is a special type of iterable, created using a function with the yield keyword.
Generators allow you to iterate over a potentially infinite sequence of elements, 
and they provide a concise and memory-efficient way to generate values on-the-fly.

Lazy Evaluation: Values are generated on-demand, one at a time. 
This is beneficial for large datasets or potentially infinite sequences.

Memory Efficiency: Generators don't store the entire sequence in memory; 
they generate values as needed, making them memory-efficient.

Simplified Syntax: The use of the yield keyword simplifies the creation of iterators 
compared to implementing the entire iterator protocol.

'''

def simple_generator():
    yield 1
    yield 2
    yield 3


# Usage
gen = simple_generator()
for value in gen:
    print(value)
