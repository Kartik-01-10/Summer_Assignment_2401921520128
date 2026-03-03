## comprehension ####
# it simply means shortcut i.e smaller code to write bigger code for example
l = [1,2,3,4]
l1 = []
for i in l:
    l1.append(i**2)
print("Using loop:", l1)

# shorter way to write this code is
l2 = [i**2 for i in l]
print("Using comprehension:", l2) 

d = {"key1": "value1", "key2": "value2", "key3": "value3"}
for k, v in d.items():
    print (k ,v)



########### FUNCTIONS IN PYTHON ###########

# What is a function?
# A function is a block of reusable code that performs a specific task.
# Functions help make programs modular, easier to read, and maintain.

#syntax.....
# def function_name(parameters):
#     """Optional docstring"""
#     # code block
#     return value

# 1. Defining a Function
def greet(name):
    """This function greets the person passed as a parameter."""
    print("Hello,", name)

greet("Alice")  # Output: Hello, Alice
greet() + "kk" # --> error bcz function is 'nonetype' and we cannot do opeeration on different type



# 2. Function with Return Value
def add(a, b):
    """This function returns the sum of two numbers."""  # <--- this is known as docstring
    return a + b                                         # means it show this text in detailing the func

result = add(2, 3)
print("Sum:", result)  # Output: Sum: 5

result = add([1,2,3],[4,5,6])
print (result) #---> [1, 2, 3, 4, 5, 6]

result = add([1,2,[1,2], 'kartik'],[4.5,"5",{1:'a'}])
print (result) # ---> [1, 2, [1, 2], 'kartik', 4.5, '5', {1: 'a'}]



# 3. Function with Default Parameter
def greet_user(name="User"):
    """This function greets a user with a default name."""
    print("Hello,", name)

greet_user()         # Output: Hello, User
greet_user("Bob")    # Output: Hello, Bob



# 4. Function with Multiple Parameters
def multiply(a, b, c):
    """This function multiplies three numbers."""
    return a * b * c

print("Product:", multiply(2, 3, 4))  # Output: Product: 24



# 5. Keyword Arguments
def divide(a, b):
    """This function divides a by b."""
    return a / b

print("Division:", divide(b=2, a=10))  # Output: Division: 5.0



# 6. Variable-Length Arguments (*args)
def print_numbers(*args):  # *args by using this we can pass n number of data of different type also
    """This function prints all numbers passed as arguments."""
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4)  # Output: 1/n 2 /n 3 /n 4
print_numbers([1,2,[1,2], 'kartik'],[4.5,"5",{1:'a'}],"kartik") # -->[1, 2, [1, 2], 'kartik'] /n [4.5, '5', {1: 'a'}] /n kartik

# most imp point args is just the name, instead of that we can also use any name for e.g

def test(*kartik):
    return kartik
test([1,2,[1,2], 'kartik'],[4.5,"5",{1:'a'}],"kartik") # -->[1, 2, [1, 2], 'kartik'] /n [4.5, '5', {1: 'a'}] /n kartik
# so synatx of this is *any_name

def test1(*args, a):
    return args,a 
test1(1,2,3,4) # --> now we get error bcz it is getting confuse so avoid such problem we do
test1(1,2,3,a=4) # ---> now we donot get error output: ((1,2,3),4)
print (test1()) #--> tuple
print (test1) #--> function



# 7. Variable-Length Keyword Arguments (**kwargs)
def print_info(**kwargs):
    """This function prints key-value pairs passed as keyword arguments."""
    for key, value in kwargs.items():
        print(key, ":", value)

print_info(name="Alice", age=25)  # Output: name : Alice  age : 25
# here is we check typr of func we get  dict
# for e.g
def test2(**kwargs):
    return kwargs
test2(a=1,b=[1,2],c="kartik",d=4.4) # --> {'a': 1, 'b': [1, 2], 'c': 'kartik', 'd': 4.4}
# here also kwargs is not imp to write, we can write anything but imp is ' ** ' to use 



# 8. Docstrings
def square(n):
    """Returns the square of a number."""
    return n ** 2

print(square(5))  # Output: 25
print(square.__doc__)  # Output: Returns the square of a number.

# 9. Pass Statement (Empty Function)
def todo():
    """This function does nothing (yet)."""
    pass

# Summary:
# - Use 'def' to define a function.
# - Use 'return' to send a value back.
# - Use default, keyword, *args, and **kwargs for flexible arguments.
# - Use docstrings
 
# What do you mean by *args and **kwargs in Python?

# *args allows a function to accept any number of positional arguments.
# Inside the function, args is a tuple of all the extra positional arguments.

def show_args(*args):
    print("Positional arguments (args):", args)

show_args(1, 2, 3)
# Output: Positional arguments (args): (1, 2, 3)

# **kwargs allows a function to accept any number of keyword arguments.
# Inside the function, kwargs is a dictionary of all the extra keyword arguments.

def show_kwargs(**kwargs):
    print("Keyword arguments (kwargs):", kwargs)

show_kwargs(name="Alice", age=25)
# Output: Keyword arguments (kwargs): {'name': 'Alice', 'age': 25}

# You can use both *args and **kwargs together to accept all types of arguments.

def show_all(a, *args, **kwargs):
    print("First argument:", a)
    print("Other positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

show_all(10, 20, 30, name="Bob", city="Delhi")
# Output:
# First argument: 10
# Other positional arguments (args): (20, 30)
# Keyword arguments (kwargs):



def test () :
    return "kk", 1,2,[1,2.2]
test() # calling, output --> "kk", 1,2,[1,2.2]
#if do like this 
a,b,c,d = test()
print (a) #---> kk
print (d) #--> [1,2.2]

a=1 
b=2
#or
a,b= 1,2
# these both are same and this the reason of above func code is correct 


