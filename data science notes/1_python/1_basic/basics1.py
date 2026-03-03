# Python Basics

# for doing multiple line comments we can use triple quotes '''   ''' or """    """
# python is case sensitive language i.e it treats uppercase and lowercase letters differently
# for example 'a' is not same as 'A' in python
# indentation is very important in python i.e we have to use indentation to define blocks of code

# how to create variables in python
# variable_name = value 
# in python we directly assign value to variable without declaring type
# for example a = 5 means we are assigning value 5 to variable a
# we can use any name for variable but it should not start with number and should not contain special characters 
# except underscore(_)


# for example a = input("Enter a number: ") will take input from user and store it in variable a
# but it will store it as string so we have to convert it to integer or float if required
# for example a = int(input("Enter a number: ")) will take input from user and convert it to integer
# for float input we can use float(input("Enter a number: "))
# for string input we can use str(input("Enter a string: ")) but it is not necessary as input() will take string input by default
a=int (input("Enter first number: ")) #inputing no.
b=int (input("Enter second number: ")) #inputing no.
#for loop we can use while loop, for loop, etc.and in loop statement we end up with colon(:) 
# and then write the body of loop
#for example while a>b: means while a is greater than b
while a>b:
    print (a,b) #print syntax first print a and b and then change the lines i.e work of endl in C++
    a=a-1
    b=b+1
c=type(a) #checking type of a i.e inbuilt function
d=type(b) #checking type of b
print ("Type of a is", c)
print ("Type of b is", d)
print ("Final values are", a, b) #printing final values

# ☆*: .｡. o(≧▽≦)o .｡.:*☆ <--- this we can print by pressing win+ .(dot) 
# print ("hi", end=" @")  -->    hi @
print ("hi", "hi", sep= "#@#")   # o/p    hi#@#hi
print ("hello world", end="!")  # o/p   hello world! : now if we again use print it will be printed in same line
print (" welcome to python")  # o/p   hello world! welcome to python

x="kartik" #string
y='kartik' #string
#we can use both " and ' for strings
# but strings are stored in indexed format i.e first letter is at index 0, second letter is at index 1 and so on
print(x[0]) #printing first letter of string x-------> k
# it also stored in backward order i.e last letter is at index -1, second last letter is at index -2 and so on
print(x[-2]) #printing second last letter of string x-------> i
#we can also use slicing in strings
print(x[0:3]) #printing first three letters of string x-------> kar

# variable_name(start_index:end_index:step) is the syntax for slicing

print (x[0:5:2]) #printing letters from index 0 to 4 with step of 2-------> kri
print(x[-1:-4:-1]) #printing letters from last to fourth last with step of -1-------> kit
print(x[::1]) #printing letters from start to end with step of 1-------> kartik
print(x[1::2]) #printing letters from index 1 to end with step of 2-------> atk

print(x[::-1]) #printing letters from end to start with step of -1-------> kitrak
print(x[1:4:-1]) #printing letters from index 1 to 4 with step of -1------->"" #this will not print anything as step is -1 and 
#start index is less than end index
print(x[4:1:-1]) #printing letters from index 4 to 1 with step of -1-------> itr
print(x[-2:-4:1]) #printing letters from second last to fourth last with step of 1------->"" #this will not print anything as 
#step is 1 and start index is less than end index

x[:]         # Returns 'kartik' → full string
x[::]        # Same as above → full string
x[::-1]      # Returns 'kitrak' → full string in reverse
x[::2]       # Returns 'krtk' → every second character
x[1::]       # Returns 'artik' → from index 1 to end
x[:4:]       # Returns 'kart' → from start to index 3

# - start: where to begin (default is 0)
# - stop: where to end (default is len(x))
# - step: how to move (default is 1)


print(x[90]) #this will give error as index is out of range
print(x[0:100]) #this will print the string --> kartik   as it is as index is out of range but it will not give error
print(x[:-90]) # This will **not** give an error. It returns an empty string because -90 is out of range, but slicing handles it gracefully. 
print(x[0:-100]) #this will print the string as it is,  as index is out of range but it will not give error
print(x[0:-100:1]) #this will print the string as it is as index is out of range but it will not give error
print(x[0:-100:-1]) #this will print the string as it is as index is out of range but it will not give error
print(x[100:0:-1]) #this will print the string in reverse order as index is out of range but it will not give error
print(x[100:0:1]) #this will print the string as it is as index is out of range but it will not give error
print(x[0:100:-1]) #this will print the string as it is as index is out of range but it will not give error
print(x[0:100:1]) #this will print the string as it is as index is out of range but it will not give error
print (x[:-100:-1]) #this will print the string in reverse order as index is out of range but it will not give error


z=True #boolean i. e True or False and it is case sensitive 
# means false is not same as False, false is not a boolean
print ("Type of m is", type(z)) #printing type of z
a= True / False # or 1/0
print (a) # in this we get zerodivision error but in numpy we get infinity


v = 5+6j # complex number
print ("Type of v is", type(v)) # printing type of v
print (v.real) # printing real part of complex number
print (v.imag) # printing imaginary part of complex number

#  in case of string and list the slicing concept is the same — slicing a sequence — but the behavior differs slightly because of mutability and data type.

l = [1, 2, 3, 4, "kartik", True, 5+3j] # list
print ("Type of l is", type(l)) # printing type of l ---> <class 'list'>
# here also we can use slicing i.e stored in the indexed format with first element at index 0, second element at index 1 and so on
print (type(l[4])) # printing type of l[4] ---> <class 'str'>
print (type(l[5])) # printing type of l[5] ---> <class 'bool'>

print (l[0]) # printing first element of list l ---> 1
print (l[-1]) # printing last element of list l ---> (5+3j)
print (l[1:4]) # printing elements from index 1 to 4 of list l ---> [2, 3, 4]
print (l[::2]) # printing elements from start to end with step of 2 ---> [1, 3, "kartik", 5+3j]
print (l[::-1]) # printing elements from end to start with step of -1 ---> [5+3j, True, 'kartik', 4, 3, 2, 1]
print (l[1:4:2]) # printing elements from index 1 to 4 with step of 2 ---> [2, 4]
print (l[4:1:-1]) # printing elements from index 4 to 1 with step of -1 ---> ['kartik', 3, 2]
print (l[100]) # this will give error as index is out of range

s= "kartik" # string
#print (s+l) # this will give error as we cannot concatenate string and list
i= list(s) # converting string to list
print (i) # printing list i ---> ['k', 'a', 'r', 't', 'i', 'k']
print (i+l) # this will concatenate string and list as both are lists now ---> ['k', 'a', 'r', 't', 'i', 'k', 1, 2, 3, 4, 'kartik', True, (5+3j)]
print (l+i) # this will concatenate list and string as both are lists now ---> [1, 2, 3, 4, 'kartik', True, (5+3j), 'k', 'a', 'r', 't', 'i', 'k']
print (l+i[0:3]) # this will concatenate list and first three elements of string as both are lists now ---> [1, 2, 3, 4, 'kartik', True, (5+3j), 'k', 'a', 'r']

l1 = [1, 2, 3, 4] # another list
print (l+l1) # this will concatenate two lists ---> [1, 2, 3, 4, 'kartik', True, (5+3j), 1, 2, 3, 4]
print (l1+l) # this will concatenate two lists in reverse order ---> [1, 2, 3, 4, 1, 2, 3, 4, 'kartik', True, (5+3j)]
print (l1*2) # this will repeat list l1 two times ---> [1, 2, 3, 4, 1, 2, 3, 4]
print (l1*0) # this will give empty list as we are repeating list l1 zero times ---> []
#print (l1+2) # this will give error as we cannot concatenate list with integer
#print (l1/2) # this will give error as we cannot divide list by integer i.e divide is not the valid operation for lists
# You can perform division with a list in Python, but not on a list directly. 
# Lists don’t support arithmetic operations like division out of the box. However, you can divide each element in a list using a
# loop or a more elegant approach like list comprehension or NumPy.
numbers = [10, 20, 30, 40]
divided = [x / 2 for x in numbers]
print(divided)  # Output: [5.0, 10.0, 15.0, 20.0]

# second method  
import numpy as np

arr = np.array([10, 20, 30, 40])
result = arr / 2
print(result)  # Output: [ 5. 10. 15. 20.]


#we have some inbuilt functions in python for lists
# we can  append, extend, insert, remove, pop, clear, sort, reverse, count, index, copy etc. in lists
l.append(5) # appending 5 to list l
print (l) # printing list l after appending 5 ---> [1, 2, 3, 4, 'kartik', True, (5+3j), 5]
print (l.append("new")) # none as append function does not return anything
print (l) # printing list l after appending "new" ---> [1, 2, 3, 4, 'kartik', True, (5+3j), 5, 'new']

l.pop() # popping last element from list l ---> [1, 2, 3, 4, 'kartik', True, (5+3j)]
l.pop(2) # popping element at index 2 from list l ---> [1, 2, 4, 'kartik', True, (5+3j)] 
# its syntax is list_name.pop(index) where index is optional and if not provided it will pop last element

l1 = [1, 2, 3, 4]
l.extend(l1) # extending list l with list l1
print (l) # printing list l after extending with l1 ---> [1, 2, 3, 4, 'kartik', True, (5+3j), 5, 1, 2, 3, 4]
l.insert(2, "new") # inserting "new" at index 2 in list l
print (l) # printing list l after inserting "new" at index 2 ---> [1, 2, 'new', 3, 4, 'kartik', True, (5+3j), 5, 1, 2, 3, 4]

l.remove(5) # removing first occurrence of 5 from list l ---> [1, 2, 'new', 3, 4, 'kartik', True, (5+3j), 1, 2, 3, 4]
# its syntax is list_name.remove(value) where value is the element to be removed

l.clear() # clearing list l--> []

#we also create list inside list i.e nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # nested list
print (nested_list[0][1]) # printing second element of first list in nested list ---> 2
print (nested_list[1][2]) # printing third element of second list in nested list ---> 6
print (nested_list[2][0]) # printing first element of third list in nested list ---> 7
print (nested_list[0:2]) # printing first two lists in nested list ---> [[1, 2, 3], [4, 5, 6]]

#l.extend(4) # this will give error as we cannot extend list with integer bcz extend function takes iterable as argument
l.extend([4]) # this will extend list l with list [4] ---> [1, 2, 'new', 3, 4, 'kartik', True, (5+3j), 1, 2, 3, 4, 4]
print (l) # printing list l after extending with [4] ---> [1, 2, 'new', 3, 4, 'kartik', True, (5+3j), 1, 2, 3, 4, 4]

l.extend("kartik") # this will extend list l with string "kartik" i.e each character of string will be added to list
print (l) # printing list l after extending with "kartik" ---> [1, 2, 'new', 3, 4, 'kartik', True, (5+3j), 1, 2, 3, 4, 4, 'k', 'a', 'r', 't', 'i', 'k'] 

# so iterable means anything which can be iterated like string, list, tuple, set, dictionary etc. i.e jab data ke andar bhi data ho
l.extend ([1, 2, 3]) # - ---> [1, 2, 'new', 3, 4, 'kartik', True, (5+3j), 1, 2, 3, 4, 4, 'k', 'a', 'r', 't', 'i', 'k', 1, 2, 3]
# append and extend put data at the end of list but append takes single element and extend takes iterable

# to avoid this problem we can use insert function to insert element at specific index
# syntax for insert is list_name.insert(index, value)
l.insert(0, "start") # inserting "start" at index 0 in list l
print (l) # printing list l after inserting "start" at index 0 ---> ['start', 1, 2, 'new', 3, 4, 'kartik', True, (5+3j), 1, 2, 3, 4, 4, 'k', 'a', 'r', 't', 'i', 'k', 1, 2, 3]
l.insert(-1, "end") #**** inserting "end" at second last index in list l it means that it push the value of give index to right and insert the value at that index
print (l) # printing list l after inserting "end" at second last index ---> ['start', 1, 2, 'new', 3, 4, 'kartik', True, (5+3j), 1, 2, 3, 4, 4, 'k', 'a', 'r', 't', 'i', 'k', 'end', 1, 2, 3]




l2 = [4, 'kartik', [1, 2, 3, 4], True, 4] # another list
l2.remove(3) #**** this will give error as 3 is not in list l2
l2[2].remove(3) # this will remove 3 from list l2[2] i.e [1, 2, 3, 4] ---> [1, 2]
print (l2) # printing list l2 after removing 3 ---> [4, 'kartik', [1, 2, 4], True, 4]
# if we want to remove 4 which is at index -1 then we can't use remove function as it will remove first occurrence of 4
l2.remove(4) # this will remove first occurrence of 4 from list l2
print (l2) # printing list l2 after removing first occurrence of 4 ---> ['kartik', [1, 2, 4], True, 4]

# now try to remove 'tik' from 'kartik' in list l2 ----> we can't do this bcz string is immutable in python
# we can only remove whole string or character from string but not part of it
# to remove part of string we can convert string to list, remove part and then convert it back to string
l2[1] = list(l2[1]) # converting string 'kartik' to list
print (l2[1])  # --> [4, ['k', 'a', 'r', 't', 'i', 'k'], [1, 2, 3, 4], True, 4]
l2[1].remove('t') # removing 't' from list l2[1] i.e ['k', 'a', 'r', 't', 'i', 'k'] ---> ['k', 'a', 'r', 'i', 'k']
l2[1] = ''.join(l2[1]) # converting list back to string  --> [4, 'kartik', [1, 2, 3, 4], True, 4]
# - ''.join(...) takes all the elements in that list and joins them into a single string, with '' (empty string) as the separator.
# here we are using join function to join list elements with empty string as separator
' '.join(['k', 'a', 'r', 't', 'i', 'k'])  # Output: 'k a r t i k'
'-'.join(['k', 'a', 'r', 't', 'i', 'k'])  # Output: 'k-a-r-t-i-k'

name = input("what is your name ? ")
print (f"hello_{name}_hi")  # -->  hello_kartik_hi

# in c/c++ we have switch  case similar to that in python we have match case 
# syntax for match case is 
match name:
    case "kartik":
        print ("hello kartik")
    case "rahul":
        print ("hello rahul")
    case _:
        print ("hello unknown")
        


# different way for printing output in python
a = 10
b = 20
print("The value of a is:", a)
print("The value of b is:", b)
print(f"The value of a is: {a}")
print(f"The value of b is: {b}")
print("The value of a is: {}".format(a))
print("The value of b is: {}".format(b))
print("The value of a is: {0}, The value of b is: {1}".format(a, b))
print("The value of a is: {a}, The value of b is: {b}".format(a=a, b=b))
# using f'{500:>10}' we can print 500 with right alignment in 10 spaces
print(f'{500:>10}')  # Output: '       500' 
# using f'{500:<10}' we can print 500 with left alignment in 10 spaces
print(f'{500:<10}')  # Output: '500       '
#using f'{500:^10}' we can print 500 with center alignment in 10 spaces
print(f'{500:^10}')  # Output: '   500    ' 
#using f'{500:.2f}' we can print 500 with 2 decimal places here f stands for float
print(f'{500:.2f}')  # Output: '500.00'
#using f'{500:.0f}' we can print 500 with 0 decimal places here f stands for float
print(f'{500:.0f}')  # Output: '500'


#using print(f"{country_code}, {currency_code}, {exchange_rate:2.2f}")  # Output: 'US, USD, 1.23'
  
#print("{}, {}, {:2.2f}".format(country_code, currency_code, exchange_rate)) # Output: 'US, USD, 1.23'

#print("%s, %s, %2.2f"%(country_code, currency_code, exchange_rate))  # Output: 'US, USD, 1.23'
# here %s stands for string and %f stands for float