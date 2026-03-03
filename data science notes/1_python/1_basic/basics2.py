a= "kartik"
print (a+"yadav") #concatenating string with + operator ---> kartikyadav
print (a*3) #repeating string with * operator ---> kartikkartikartik
#print (a+1) #this will give error as we cannot concatenate string with integer
print (a+str(1)) #this will concatenate string with integer after converting integer to string ---> kartik1
# so this is how we can concatenate string with integer by doing type conversion
print (a*0) #this will give empty string as we are repeating string 0 times ---> ""
#print (a/1) #this will give error as we cannot divide string by integer i.e divide is not the valid operation for strings
b = "yadav"
#print (a-b) #this will give error as we cannot subtract one string from another


#a= ' don't do that' #this will give error as we cannot use single quote inside single quote
#a= "don't do that" #this will work as we are using double quotes outside and vice versa
a = 'don\'t do that' #this will work as we are using escape character


# 🧠 Python’s Type Conversion Rules
# Python tries to be flexible, but it has boundaries. Here’s how to know when it will automatically convert types and when it will raise an error:

# ✅ Python Will Do Type Conversion When:
# | Operation   | Example           | Result            | 
# | int + float | 5 + 2.5           | 7.5 (int → float) | 
# | bool + int  | True + 3          | 4 (True is 1)     | 
# | str + str   | 'hello' + 'world' | 'helloworld'      | 
# | list + list | [1, 2] + [3, 4]   | [1, 2, 3, 4]      | 

 
# Python will promote types when it makes sense — like turning an int into a float or treating True as 1.

# ❌ Python Will Raise an Error When:
# | Operation | Example     | Error Type | 
# | int + str | 5 + '5'     | TypeError | 
# | list + int | [1, 2] + 3 | TypeError | 
# | str - str | 'a' - 'b'   | TypeError | 
# | None + int | None + 1   | TypeError | 

x = "value"
if isinstance(x, str):
    x = int(x)
#  What It Means:
# - isinstance(x, str) checks if the variable x is of type str (a string).
# - If it is a string, then x = int(x) converts it to an integer using the int() function.
x = '42'

if isinstance(x, str):
    x = int(x)

print(x)  # Output: 42 (as an integer)
# ⚠️ Important Notes:
# - This only works if the string contains a valid integer (like '42', '0', '-7').
# - If the string contains non-numeric characters (like 'abc' or '4.5'), it will raise a ValueError.
x = 'abc'
if isinstance(x, str):
    x = int(x)  # ❌ ValueError: invalid literal for int()

# -------------------------------
# 🔄 TYPE CONVERSION (IMPLICIT)
# -------------------------------

# Python automatically converts int to float
x = 5       # int
y = 2.5     # float
z = x + y   # int is converted to float
print(z)    # Output: 7.5

# Boolean is treated as integer (True = 1, False = 0)
a = True
b = 3
print(a + b)  # Output: 4

# -------------------------------
# ❌ IMPLICIT CONVERSION FAILS
# -------------------------------

# Mixing incompatible types causes error
x = 5
y = '5'
# print(x + y)  # ❌ TypeError: unsupported operand type(s) for +: 'int' and 'str'

# -------------------------------
# 🔧 TYPE CASTING (EXPLICIT)
# -------------------------------

# Convert string to integer
x = '42'
x = int(x)
print(x)  # Output: 42

# Convert integer to string
y = 100
y = str(y)
print(y)  # Output: '100'

# Convert float to integer (truncates decimal)
z = 3.99
z = int(z)
print(z)  # Output: 3

# Convert list of characters to string
chars = ['k', 'a', 'r', 't', 'i', 'k']
name = ''.join(chars)
print(name)  # Output: 'kartik'

# Convert string to list of characters
name = 'kartik'
char_list = list(name)
print(char_list)  # Output: ['k', 'a', 'r', 't', 'i', 'k']

# -------------------------------
# 🛡️ SAFE TYPE CASTING
# -------------------------------

# Check type before casting
x = '123'
if isinstance(x, str):
    x = int(x)
print(x)  # Output: 123

# Handle invalid conversion with try-except
user_input = 'abc'
try:
    num = int(user_input)
except ValueError:
    print("Cannot convert to integer.")  # Output: Cannot convert to integer.

# -------------------------------
# 🧪 BONUS: Casting Other Types
# -------------------------------

# Convert list to tuple
lst = [1, 2, 3]
tpl = tuple(lst)
print(tpl)  # Output: (1, 2, 3)

# Convert number to boolean
print(bool(0))    # Output: False
print(bool(42))   # Output: True

# Convert boolean to integer
print(int(True))  # Output: 1
print(int(False)) # Output: 0



# some inbuilt functions in python for strings
####### BUT WE DONT HAVE TO REMEMORISE THESE INBUILT FUNCTIONS AS WE CAN USE THEM DIRECTLY ########


x = "this is a string class"
print (len(x)) #printing length of string x and here indexing starts from 0 and goes to n-1 where n is length of string
print (x.upper()) #printing string x in upper case
print (x.lower()) #printing string x in lower case
print (x.title()) #printing string x in title case
print (x.split()) #printing string x as list of words
print (x.replace("is", "was")) #replacing is with was in string x
print (x.find("is")) #finding first occurrence of is in string x and it doesnot find then it returns -1
print (x.index("is")) #finding first occurrence of is in string x and it does
print (x.count("is")) #counting number of occurrences of is in string x
print (x.startswith("this")) #checking if string x starts with this by giving value True or False
print (x.endswith("class")) #checking if string x ends with class by giving value True or False
print (x.strip()) #removing leading and trailing whitespaces from string x here whitespaces are extra spaces, tabs, newlines etc.
print (x.strip("this")) #removing leading and trailing characters(this) from string x
print (x.isalpha()) #checking if string x contains only alphabets by giving value True or False
print (x.isalnum()) #checking if string x contains only alphanumeric characters by giving value True or False
print (x.isdigit()) #checking if string x contains only digits by giving value True or False
print (x.isnumeric()) #checking if string x contains only numeric characters by giving value True or False
print (x.islower()) #checking if string x is in lower case by giving value True or False
print (x.isupper()) #checking if string x is in upper case by giving value True or False
print (x.isspace()) #checking if string x contains only whitespace characters by giving value True or False
print (x.capitalize()) #capitalizing first letter of string x
print (x.swapcase()) #swapping case of string x i.e upper case to lower case and lower case to upper case



#**************************************************************************************************************************#

a = [1, 2, 3, 4, 5]
a.sort()
print (a) # Output: [1, 2, 3, 4, 5]
# but we do directly write ----> print (a.sort()) as it will return None bcz sort function does not return anything
# it just sorts the list in place

a.sort() # sorting list a in ascending order or we can use a[::1] to sort in ascending order 
#we can also use a.sort(reverse=True) to sort in descending order
print (a) # printing list a after sorting 
a.reverse() # reversing list a or we can also use a[::-1] to reverse the list
print (a) # printing list a after reversing 
# but basic difference between reverse and slicing is that reverse will change the original list
# but slicing will not change the original list

b= [1, 2, 3, 'kartik']
#b.sort() # this will give error as we cannot sort list with different data types
# we can only sort list with same data types like all integers or all strings etc.
c=['aa', 'ab', 'bcc', 'a', 'b']
c.sort() # this will sort the list c in ascending order
print (c) # printing list c after sorting ---> ['a', 'aa', 'ab', 'b', 'bcc']
c.index('aa') # this will return the index of 'aa' in list c ---> 1 bcz we have use index function after sorting the list 
# and sort make change in orginal list

c.count('aa') # this will return the count of 'aa' in list c ---> 1


###### MUTABLE DATA TYPES ######
# mutable data types are those which can be changed or modified after creation EXAMPLES
# 1. LISTS
# 2. DICTIONARIES
# 3. SETS
# 4. BYTEARRAYS
# 5. USER DEFINED CLASSES

####### IMMUTABLE DATA TYPES ######
# immutable data types are those which cannot be changed or modified after creation EXAMPLES
# 1. TUPLES
# 2. STRINGS
# 3. FROZEN SETS
# 4. NUMBERS
# 5. BYTE STRINGS


s= "kartik"
##s[0] = 'K' # this will give error as strings are immutable
s = "K" + s[1:] # this will change the first letter of string --> Kartik
s = s.replace('k', 'K') # this will change all occurrences of 'k' to 'K' in string .... so syntax is variable_name.replace(old_value, new_value) 
# but how to is possible to change string if it is immutable?
# it is possible by creating a new string with the changes and assigning it to the same variable name
# so we are not changing the original string but creating a new string with the changes and assigning it to the same variable name


l=[1, 2, 3, 4]
l[0] = 10 # this will change the first element of list to 10 as lists are mutable
print(l) # Output: [10, 2, 3, 4]
#l[0]= 'k' # this will change the first element of list to 'k' as lists are mutable
print(l) # Output: ['k', 2, 3, 4]



t= (1, 2, 3, True, 'kartik',[1,2]) # this is a tuple i.e it can contain different data types
#t[0] = 10 # this will give error as tuples are immutable
# we cannot change the elements of tuple after creation
# here we can use slicing bcz it also store in indexing like lists but we cannot change the elements of tuple after creation
# we can only access the elements of tuple using indexing or slicing and we can use all concepts of indexing and slicing
print (type(t)) # Output: <class 'tuple'>
t.count(1) # this will return the count of 1 in tuple t ---> 1 
t.index(2) # this will return the index of 2 in tuple t ---> 1
# we can also use t.index(2, 1) to find the index of 2 in tuple t starting from index 1
# but we cannot use t.index(2, 1, 3) to find the index of 2 in tuple t starting from index 1 to index 3
# here in both count and index we give the value we want to count or find the index of





s3 =  {1,2,'kartik', True, 1.5} # this is a set i.e it can contain different data types but it cannot contain duplicate values
print (type(s3)) # Output: <class 'set'>
# here if we put tuple in set then it will allow it but if we put list in set then it will give error as list is mutable and set can only
# contain immutable data types
# set is unordered collection of unique elements and it does not allow duplicate values and it is mutable
# in this we cannot use indexing or slicing as it is unordered collection of unique elements
# print (s3[0]) or print ([::1]) # this will give error as we cannot use indexing or slicing in set
# we can use set to remove duplicate values from a list or any other iterable by converting it to set
# how to create a set from a list?
l = [1, 2, 3, 4, 5, 1, 2, 3]
s4 = set(l) # this will create a set from list l and remove duplicate values
print (s4) # Output: {1, 2, 3, 4, 5}

# some set inbuilt functions 
# here we only give value we want to add or remove from set
s3.add(6) # adding 6 to set s3
print (s3) # Output: {1, 2, 3, 4, 5, 6, 'kartik', True, 1.5}
s3.remove(1) # removing 1 from set s3
print (s3) # Output: {2, 3, 4, 5, 6, 'kartik', True, 1.5}
s3.discard(2) # removing 2 from set s3
print (s3) # Output: {3, 4, 5, 6, 'kartik', True, 1.5}
s3.pop() # removing last element from set s3
print (s3) # Output: {4, 5, 6, 'kartik', True, 1.5}
s3.clear() # removing all elements from set s3
print (s3) # Output: set()

# 🔍 remove() vs discard() in Python Sets
# | Function   | Removes Element  | Raises Error if Element Not Found  | Use Case | 
# | remove(x)  | ✅ Yes          | ❌ Yes → Raises KeyError           | Use when you're sure the element exists | 
# | discard(x) | ✅ Yes          | ✅ No → Silently does nothing      | Use when you're unsure if the element exists | 


# 🧪 Example
# s = {1, 2, 3}

# s.remove(2)     # Removes 2 → s becomes {1, 3}
# s.discard(3)    # Removes 3 → s becomes {1}
# s.remove(4)     # ❌ Raises KeyError: 4 not in set
# s.discard(4)    # ✅ No error → s remains {1}
# 💡 Tip
# If you're writing code where the presence of an element is uncertain, discard() is safer. But if you want to catch mistakes or 
# enforce that an element must be present, remove() is more strict.



s1={}
s2 = {"key1": "value1", "key2": "value2", "key3": "value3"}
print (type(s2)) # Output: <class 'dict'>
print (type(s1)) # Output: <class 'dict'>   *** it will not give set 
# this is a dictionary i.e it is a collection of key-value pairs
# here we can use indexing but we cannot use slicing as it is unordered collection of key-value pairs
# we can access the value of a key using indexing like s2["key1"] will return "value1"
# we can also use s2.get("key1") to get the value of key "key1" in dictionary s2
# we can also use s2.keys() to get the keys of dictionary s2
# we can also use s2.values() to get the values of dictionary s2
# we can also use s2.items() to get the key-value pairs of dictionary s2
# here keys can be of any immutable data type like string, integer, tuple, boolean etc.
# but values can be of any data type like string, integer, list, tuple, set i.e both immutable and mutable
# keys must be unique in dictionary but values can be duplicate
s2["key4"] = "value4"  # Adding a new key-value pair to the dictionary
print(s2)  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
s2["key1"] = "new_value1"  # Updating the value of an existing key
print(s2)  # Output: {'key1': 'new_value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

del s2["key2"]  # Deleting a key-value pair from the dictionary
print(s2)  # Output: {'key1': 'new_value1', 'key3': 'value3', 'key4': 'value4'}

s2.pop("key3")  # Removing a key-value pair and returning the value and this if we do not give key then it
#will give error i.e argument is required
print(s2)  # Output: {'key1': 'new_value1', 'key4': 'value4'}
print (s2["key4"])  # Accessing the value of key "key4" in dictionary s2 --> value4

# 🆚 pop() vs del in Python Dictionaries
# | Feature                            | pop()                                    | del | 
# | Removes item                       | ✅ Yes                                  | ✅ Yes | 
# | Returns value                      | ✅ Yes → returns the value removed      | ❌ No → does not return anything | 
# | Raises error if key not found      | ✅ Yes → KeyError                       | ✅ Yes → KeyError | 
# | Can be used with default value     | ✅ Yes → pop(key, default)              | ❌ No default handling | 
# | Syntax                             | dict.pop(key) or dict.pop(key, default) | del dict[key] | 

student = {"name": "Ravi", "age": 21, "score": 88}
# Just delete the key-value pair
del student["score"]
print(student)  # Output: {'name': 'Ravi', 'age': 21}
# Avoid KeyError by providing a default value
score = student.pop("score", "Not Found")
print(score)  # Output: Not Found



s2.clear()  # Removing all key-value pairs from the dictionary
print(s2)  # Output: {}

#s2[True] = 27  # Adding a key-value pair with boolean key
#print (s2[1])  #** Accessing the value of key True in dictionary s2 --> 27 

s3 = {'name': 'kartik', 'name': 'yadav'}
print (s3['name']) # ** Output: yadav bcz keys must be unique in dictionary so it will take the last value of 
# key 'name' i.e 'yadav' due to overwriting

s4 = {'name': 'kartik', 'char': ['a', 'b', 'c'], 'assignment': (1, 2, 3, 4)}
print (s4['char'])  # Accessing the value of key 'char' in dictionary s4 --> ['a', 'b', 'c']
s4['char'].append('d')  # Adding 'd' to the list value
print (s4['char'])  # Output: ['a', 'b', 'c', 'd']
print (s4['char'][0])  # Accessing the first element of the list value --> 'a'

s4['char'][0] = 'A'  # Changing the first element of the list value
print (s4['char'])  # Output: ['A', 'b', 'c', 'd']
# here we can see that we can change the list value in dictionary but we cannot change the key or value of dictionary
# we can only change the value of key in dictionary but not the key itself

s4['assignment'] = (5, 6, 7, 8)  # Changing the tuple value
print (s4['assignment'])  # Output: (5, 6, 7, 8)
# here we can see that we can change the tuple value in dictionary but we cannot change the key or value of dictionary

#s4['assignment'][0] = 10  # This will give error as tuples are immutable and we cannot change the elements of tuple after creation
#print (s4['assignment'][2]) # Accessing the third element of the tuple value --> 7 

s4.keys()  # Getting the keys of dictionary s4 --> dict_keys(['name', 'char', 'assignment'])
s4.values()  # Getting the values of dictionary s4 --> dict_values(['kartik', ['A', 'b', 'c', 'd'], (5, 6, 7, 8)])
s4.items()  # Getting the key-value pairs of dictionary s4 --> dict_items([('name', 'kartik'), ('char', ['A', 'b', 'c', 'd']), 
# ('assignment', (5, 6, 7, 8))])
list(s4.items())  # Converting the key-value pairs of dictionary s4 to a list
# Output: [('name', 'kartik'), ('char', ['A', 'b', 'c', 'd']), ('assignment', (5, 6, 7, 8)))]


# we can also create a nested dictionary like this
nested_dict = {
    'outer_key1': {
        'inner_key1': 'inner_value1',
        'inner_key2': 'inner_value2'
    },
    'outer_key2': {
        'inner_key3': 'inner_value3',
        'inner_key4': 'inner_value4'
    }
}
# Accessing values in a nested dictionary
print(nested_dict['outer_key1']['inner_key1'])  # Output: inner_value1
print(nested_dict['outer_key2']['inner_key4'])  # Output: inner_value4


# Sample dictionary
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

# Loop through keys
for name in student_scores:
    print(name)

# Loop through values
for score in student_scores.values():
    print(score)

# Loop through key-value pairs
for name, score in student_scores.items():
    print(f"{name} scored {score}")

# Dictionary comprehension: Add 5 bonus points to each score
updated_scores = {name: score + 5 for name, score in student_scores.items()}
print(updated_scores)

# Define a nested dictionary where each student has subject-score pairs
students = {
    "Alice": {"math": 85, "science": 90},
    "Bob": {"math": 78, "science": 82},
    "Charlie": {"math": 92, "science": 88}
}

# Loop through the outer dictionary to access each student's name and their subjects
for name, subjects in students.items():
    print(f"Student: {name}")  # Print the student's name

    # Loop through the inner dictionary to access each subject and score
    for subject, score in subjects.items():
        print(f"  {subject}: {score}")  # Print the subject and corresponding score
# output
# Student: Alice
#   math: 85
#   science: 90
# Student: Bob
#   math: 78
#   science: 82
# Student: Charlie
#   math: 92
#   science: 88

# here what is the use of f inside print
# What is f in print(f"...")?
# - The f stands for formatted string literal.
# - It allows you to embed variables or expressions inside {} directly in the string.
# - It makes your code cleaner, faster, and easier to read.

# Define some variables
name = "Ravi"
age = 25
score = 88

# Using f-string to insert variables directly into the string
print(f"My name is {name} and I am {age} years old.")  
# Output: My name is Ravi and I am 25 years old.

# You can also include expressions inside the curly braces
print(f"My score plus 10 is {score + 10}")  
# Output: My score plus 10 is 98

# Using f-string with multiple variables and formatting
print(f"{name} scored {score} in the test.")  
# Output: Ravi scored 88 in the test.