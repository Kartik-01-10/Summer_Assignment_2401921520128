# Lambda functions in Python are small anonymous functions.
# They are defined using the 'lambda' keyword.

# Syntax:
# lambda arguments: expression

# Example 1: A lambda function that adds 10 to the input
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15
add_ten = lambda x,y: x + y
print(add_ten(5,5))  # Output: 10


# Example 2: A lambda function that multiplies two numbers
multiply = lambda a, b: a * b
print(multiply(3, 4))  # Output: 12

# Example 3: Using lambda with the 'map' function
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# Example 4: Using lambda with the 'filter' function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]


# Example 5: Lambda function to convert Celsius to Fahrenheit
c_to_f = lambda c: (c * 9/5) + 32
print(c_to_f(0))    # Output: 32.0
print(c_to_f(25))   # Output: 77.0


# Example 6: Lambda function to find the maximum of two numbers
max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))  # Output: 20
print(max_num(50, 30))  # Output: 50


# Example 7: Lambda function to find the length of a string or list
find_length = lambda x: len(x)
print(find_length("hello"))  # Output: 5
print(find_length([1, 2, 3, 4]))  # Output: 4




# Lambda functions are useful for short, simple functions that are used only once or temporarily.
# For more complex functions, use 'def' to define a regular function.