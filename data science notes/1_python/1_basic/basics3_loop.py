####### IF ELIF ELSE STATEMENTS #########

a= float (input("Enter marks out of 100: "))
if a==100:
    print("Perfect Score!")
elif a >= 90:
    print("Grade A")
elif a >= 80:
    print("Grade B")
elif a >= 70:
    print("Grade C")
elif a >= 60:
    print("Grade D")
else:
    print("Grade F")
# in python we use "and" ,  "or" to input multiple conditions
# and is used when both conditions should be true
# or is used when either condition should be true
# for example
# if a > 10 and/or a < 20:

price = 100
if price > 50:
    print("Expensive")
    if price >= 100:
        print("Very Expensive")
    else:
        print("Moderately Expensive")
else:
    print("Cheap")
# o/p : 
# Expensive
# Very Expensive

####### FOR LOOP  #########

# wap to take list input and add 1 to each element
l = [1, 2, 3, 4]
l = [x + 1 for x in l]
print(l)  
# second method 
l = [1, 2, 3, 4]
for i in range(len(l)):
    l[i] +=1
    print (l[i])
# third method
l = [1, 2, 3, 4]
for i in l:
    i += 1
    print(i)
# fourth method
l = [1, 2, 3, 4]
for i in range(len(l)):
    l[i] += 1
    print(l[i])

# 🟢 for i in x
# - This means: loop through each item in x.
# - x can be a list, string, set, etc.
# - You get the actual values from x.
names = ["Ravi", "Amit", "Neha"]
for name in names:
    print(name)  # Prints each name



# 🔵 for i in range(x)
# - This means: loop from 0 to x-1.
# - x is a number.
# - You get index numbers, not value
for i in range(3):
    print(i)  # Prints 0, 1, 2
    #or
x=4 
for i in range (x):
    print (x)

# wap to convert all elements of a list to uppercase
# first method
l1 = ['kk', 'll', 'mm', 'nn']
l2= []
for i in l1:
    l2.append(i.upper())
for i in l2:
    print(i)
# second method using list comprehension
l1 = ['kk', 'll', 'mm', 'nn']
l2 = [i.upper() for i in l1]
for i in l2:
    print(i)  #---> KK /n LL /n MM /n NN
# third method using map function
l1 = ['kk', 'll', 'mm', 'nn']
l2 = list(map(str.upper, l1))
for i in l2:
    print(i)  #---> KK /n LL /n MM /n NN    here /n is newline character 


# wap to create a two new list one for integer and another for string from a mixed list
mixed_list = [1, 'apple', 2, 'banana', 3, 'cherry', 3.14]
no_list = []
str_list = []
for i in mixed_list:
    if type(i) == int or type(i) == float:
        no_list.append(i)
    elif type(i) == str:
        str_list.append(i)
print(no_list)  #---> [1, 2, 3, 3.14]
print(str_list)  #---> ['apple', 'banana', 'cherry']



####### FOR ELSE LOOP #########

l3 = [1, 2, 3, 4]                                   # output will be :  1 /n 2 /n 3 /n 4 /n Loop completed successfully
for i in l3:
    print(i)
else:
    print("Loop completed successfully")


# we have similar concept of break and continue in python as in C++
for i in l3:
    if i == 3:
        break  # this will stop the loop when i is 3
    print(i)  # output will be : 1 /n 2
else :
    print("Loop completed") 
# now output will be : 1 /n 2 it means that else statement will only execute if "for" loop  completely exhaust itself.

for i in l3:
    if i == 3:
        continue  # this will skip the iteration when i is 3
    print(i)  # output will be : 1 /n 2 /n 4
else :
    print("Loop completed") 
# output --> 1 /n 2 /n 4 /n Loop completed


# range is the generator function in python which generates a sequence of numbers
# it is used in for loop to iterate over a sequence of numbers
# for example range (5) will generate a sequence of numbers from 0 to 4 means excluding 5
# range (1, 5) will generate a sequence of numbers from 1 to 4 means excluding 5
# range (1, 10, 2) will generate a sequence of numbers from 1 to 9 means excluding 10 with a step of 2
for i in range(5):  # this will print numbers from 0 to 4
    print(i)  # output will be : 0 /n 1 /n 2 /n 3 /n 4

# syntax of range is range(start, stop, step)

list (range(-10,0)) # --> [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
# wap to print list in reverse order 
list = [1, 2, 3, 4, 5]
for i in range(len(list)-1, -1, -1):  # this will print list in reverse order
    print(list[i])  # output will be : 5 /n 4 /n 3 /n 2 /n 1

# second method
for i in range (len(list)):
    print(list[-(i+1)])  # output will be : 5 /n 4 /n 3 /n 2 /n 1
# third method
for i in range (len(list)-1,0 , -1):
    print(list[i])  # output will be : 5 /n 4 /n 3 /n 2 /n 1

# use inbuilt function
sum(list) #--> 15     
max(list) #--> 5
min(list) #--> 1
# or use manual method
sum = 0
for i in list :
    sum+=i
print(sum)  # output will be : 15

d= {'a': 1, 'b': 2, 'c': 3}
for i in d:
    print(i)  # this will print keys of the dictionary, output will be : a /n b /n c
# to print values of the dictionary
for i in d:
    print(d[i])  # output will be : 1 /n 2 /n 3
# to print both keys and values of the dictionary
for key, value in d.items():
    print(f"{key}: {value}")  # output will be : a: 1 /n b: 2 /n c: 3   


####### WHILE LOOP #########
# wap to print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)  # output will be : 1 /n 2 /n 3 /n 4 /n 5 /n 6 /n 7 /n 8 /n 9 /n 10
    i += 1

# wap to find factorial of a number
num = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print (factorial)  # output will be the factorial of the number entered by the user

# wap to reverse the string 
s = "kartik"
print (s[::-1]) # --> kitrak
reverse=""
length = len(s)
while length >0:
    reverse += s[length -1]
    length -=1
print (reverse) # ---> kitrak


n=5
i=1
while i<n:
    print (i)
    i+=1
else:
    print ("this will be executed once your while loop will complete successfully")
# ---> 1 /n 2 /n 3 /n 4 /n this will be executed once your while loop will complete successfully
# same concept as for else i.e if  we use break then else will not work

# day months year calculator
days = int(input("Enter number of days: "))
years = days // 365
days = days % 365
months = days // 30
days = days % 30
print(f"{years} years, {months} months, {days} days")  



triplets = [(x, y, z) for x in range(1, 100) 
                      for y in range(x + 1, 100)
                      for z in range(y + 1, 100)
                      if x ** 2 + y ** 2 == z ** 2]
print(triplets)  #--> [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (12, 16, 20), (15, 20, 25), (20, 21, 29)]

triplets = []
for x in range(1, 100):
    for y in range(x + 1, 100):
        for z in range(y + 1, 100):
            if x ** 2 + y ** 2 == z ** 2:
                triplets.append((x, y, z))
print(triplets)  #--> [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (12, 16, 20), (15, 20, 25), (20, 21, 29)]
# both method are same but first one is using list comprehension which is more pythonic way of writing code.


L = [y - x for x in [1, 2, 3] for y in [3, 4, 5] if y > x]
print(L)  #--> [2, 3, 3, 4, 4]
L = [ ]
for x in [1, 2, 3]:
    for y in [3, 4, 5]:
        if y > x:
            L.append(y - x)
print(L)  #--> [2, 3, 3, 4, 4]  
# both method are same but first one is using list comprehension which is more pythonic way of writing code.