# What is a Generator Function in Python?
# ---------------------------------------
# A generator function is a special type of function that returns an iterator, called a generator.
# Instead of returning a single value, it can yield (produce) a series of values, one at a time, as you loop over it. e.g range func

# How to create a generator function?
# -----------------------------------
# - Use the 'def' keyword like a normal function.
# - Use the 'yield' keyword instead of 'return' to produce a value.
# - Each time the function is called, it resumes where it left off after the last 'yield'.

# Example:
def my_generator():
    yield 1
    yield 2
    yield 3

# Using the generator:
gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# Or use a loop:
for value in my_generator():
    print(value)  # Output: 1, then 2, then 3

# Why use generator functions?
# ----------------------------
# - They are memory efficient. They generate values one by one, so you don't need to store all values in memory.
# - Useful for working with large data or infinite sequences.

# Key points:
# -----------
# - 'yield' pauses the function and saves its state for next time.
# - Generator functions return a generator object, not the actual values.
# - You can use 'next()' to get the next value, or use a 'for' loop.

# Example: Generator for even numbers up to n
def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)  # Output: 0, 2, 4, 6, 8,



def test_fib(n):
    a,b =0,1
    for i in range (n):
        yield a
        a,b =b ,a+b
test_fib(4) # ---> it say that generator object 
# but if we use in loop
for i in test_fib(4):
    print(i)   #----> 0 /n 1 /n 1 /n 2 

# second method 
def test_fibo(n):
    a,b=0,1
    while True:
        yield a
        a,b = b, a+b
fib = test_fibo(10)       # type(fib) ---> generator
for i in range (4):
    print (next(fib))  #--> 0 /n 1 /n 1 /n 2 
# why we have use next inbuilt func 
# by default string is not an iterator but it is iterable, next will only work if we have iterator. so to create string an iterator 

# s="kartik"
# next(s)  ---> error # TypeError: 'str' object is not an iterator
# so we have to convert it into iterator using iter() inbuilt func

# s="kartik"
# s1=iter(s)    now we can use next func    ..... type of s1 --> str_iterator
# next(s)---> k 
#next (s)---> a
# so this is the mechanism behind the for loop  i.e take data convert it in iterator and then next ahain and again till given times

# string is iterable but not iterator and integer is neither iterable nor iterator so next will not work on it and
# also we cannot convert integer into iterator using iter() func

## iterable and iterater is imp ##########******
# in simple word 
#iterable ----> visa data jise haam iterator ma convert kar sake 
#iterator ---> jise next next ma haam ja sake or data nikal sake 


# Iterable and Iterator in Python
# ------------------------------

# Iterable:
# ---------
# An iterable is any Python object that can return its elements one at a time.
# Examples: list, tuple, string, set, dictionary, etc.
# You can loop (for loop) over an iterable.
# Internally, Python calls iter() on the object to get an iterator.

# Example of an iterable:
my_list = [1, 2, 3]
for item in my_list:
    print(item)  # Output: 1, 2, 3

# Iterator:
# ---------
# An iterator is an object that represents a stream of data; it returns one element at a time.
# It remembers its position during iteration.
# It implements two methods: __iter__() and __next__().
# You get an iterator from an iterable by using iter().

# Example of getting an iterator:
my_list = [1, 2, 3]
my_iter = iter(my_list)  # my_iter is now an iterator

print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
# print(next(my_iter))  # This will raise StopIteration error because no more items

# Key Points:
# -----------
# - All iterators are also iterables, but not all iterables are iterators.
# - Iterable: Can be looped over (for loop), but does not remember position.
# - Iterator: Remembers position, gives next item with next(), raises StopIteration when done.

# Custom Example:
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 3:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

nums = MyNumbers()
it = iter(nums)
print(next(it))  # Output: 1
print(next(it))  # Output: 2
print(next(it))  # Output: 3

# Summary Table:
# --------------
# | Term      | Can use for loop | Can use next() | Remembers position |
# |-----------|------------------|----------------|--------------------|
# | Iterable  | Yes              | No             | No                 |
# | Iterator  | yes              | yes            | yes                |