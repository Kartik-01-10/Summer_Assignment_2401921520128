# map(), filter(), reduce() in Python

# 1. syntax: map(function, iterable)
# - Applies a function to every element in an iterable (like a list).
# - Returns a map object (convert to list for results).
# - Useful for transforming data quickly.

# Example: Add 1 to every element
nums = [1, 2, 3, 4]
plus_one = list(map(lambda x: x + 1, nums))
print(plus_one)  # Output: [2, 3, 4, 5]
# here if we dont use map func then we have to use for loop to add 1 to each element
# why we are using list bcuz map return map object not list

def sq(x):
    return x**2
list (map(sq,nums))  # output : [1, 4, 9, 16]


list (map(lambda x : x**2 , nums)) # o/p [1, 4, 9, 16]


l1 = [1,2,3,4]
l2 = [5,6,7,8]
print(list (map(lambda x, y : x*y , l1 , l2)) ) # [5,12,21,32]


s="kartik"
print (list (map(lambda s: s.upper(), s)) ) # ['K', 'A', 'R', 'T', 'I', 'K']




# 2. filter(function, iterable)
# - Filters elements based on a condition (function returns True/False).
# - Returns a filter object (convert to list for results).
# - Useful for selecting specific data.

# Example: Keep only odd numbers
nums = [1, 2, 3, 4]
odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)  # Output: [1, 3]

nums = [10, 15, 20, 25, 30]
greater_than_20 = list(filter(lambda x: x > 20, nums))
print(greater_than_20)  # Output: [25, 30]


# 3. reduce(function, iterable)
# - Repeatedly applies a function to pairs of elements, reducing the iterable to a single value.
# - ** Must import from functools: from functools import reduce, it will not directly accessable
# - Useful for cumulative operations (sum, product, GCD, etc.)

from functools import reduce # <-- this the method to import reduce

# Example: Find the sum of all elements
nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums) # here we cannot use 3 args in lambda func because reduce take only 2 args at a time
print(total)  # Output: 10

total = reduce(lambda x, y: x + y, [])
print (total)  # Output: error because empty list has no value to reduce

total = reduce(lambda x, y: x + y, [1])
print (total)  # Output: 1 because only one element is present. this is the exception case thats why it return that element itself

# Example: Find the maximum element
nums = [3, 1, 4, 1, 5, 9, 2]
maximum = reduce(lambda x, y: x if x > y else y, nums)
print(maximum)  # Output: 9

# Summary Table:
# | Function | Purpose        | Returns      | Example Use         |
# |----------|----------------|--------------|---------------------|
# | map      | Transform data | map object   | map(f, list)        |
# | filter   | Select data    | filter object| filter(f, list)     |
# | reduce   | Combine data   | single value | reduce(f, list)     |

# Tip: Always convert map/filter results to list for easy viewing.