
# ➤ What are Exceptions?
# Exceptions are errors that occur during the execution of a program.
# Instead of crashing the program, Python allows you to handle these errors gracefully.

# ➤ Why Use Exceptions?
# - To prevent program crashes
# - To handle unexpected inputs or conditions
# - To provide meaningful error messages
# - To maintain control flow during runtime errors

# ➤ Basic Syntax of Exception Handling

try:
    # Code that might raise an exception
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)

except ZeroDivisionError:
    # Handles division by zero
    print("Error: Cannot divide by zero.")

except ValueError:
    # Handles invalid input (e.g., letters instead of numbers)
    print("Error: Invalid input. Please enter a number.")

except Exception as e:
    # Handles any other unexpected exception
    print("Unexpected error:", e)

finally:
    # This block always runs, whether an exception occurred or not
    print("Execution completed.\n")



# try : 
#     int ("kartik")
# except :
#     print ("this will catch an error ")  # o/p   --> this will catch an error

# try :
#     import kartik   
# except ImportError as e:
#     print (e)
# print (10/4)
# o/p   -->  no module named "kartik"  /n  2.5  i.e 2.5 ans means after error also code will not stop in mid 


try :
    "kartik".test()
except Exception as e :
    print (e) 




# ➤ Example 1: ZeroDivisionError
try:
    num = int(input("Enter a number to divide 10 by: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# ➤ Example 2: ValueError (invalid input)
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Error: Please enter a valid integer.")

# ➤ Example 3: IndexError (list index out of range)
try:
    my_list = [1, 2, 3]
    print("Element at index 5:", my_list[5])
except IndexError:
    print("Error: Index out of range.")

# ➤ Example 4: FileNotFoundError
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")

# ➤ Example 5: Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ValueError:
    print("Error: Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

#  Example: TypeError

# ➤ TypeError occurs when an operation is performed on incompatible types
#    For example: adding a string and an integer

try:
    result = "Age: " + 25  # ❌ Cannot concatenate str and int directly
    print(result)
except TypeError:
    print("Error: Cannot combine string and integer directly.")

# ✅ Correct way (for reference)
# result = "Age: " + str(25)
# print(result)



# ➤ Common Errors:
#    - ZeroDivisionError: Division by zero
#    - ValueError: Invalid type conversion (e.g., str to int)
#    - IndexError: Accessing invalid list index
#    - FileNotFoundError: Trying to open a missing file
# ➤ Multiple except blocks can be used to handle different errors



#  Example: Using multiple except blocks

def process_input(user_input):
    try:
        # Try converting input to integer
        number = int(user_input)

        # Try adding number to a string (will raise TypeError)
        result = "Your number is: " + number  # ❌ str + int → TypeError
        print(result)

    except ValueError:
        # Raised if int(user_input) fails (e.g., input is "abc")
        print("ValueError: Input must be a valid integer.")

    except TypeError:
        # Raised if incompatible types are used in operations
        print("TypeError: Cannot combine string and integer directly.")

# 🔍 Test cases
process_input("abc")   # Triggers ValueError
process_input("25")    # Triggers TypeError

# ➤ You can use multiple except blocks to handle different errors:
#    try:
#        risky_code()
#    except ValueError:
#        handle_value_error()
#    except TypeError:
#        handle_type_error()

# ➤ Python checks each except block in order and runs the first match.



# ➤ Case 1: General Exception first, then TypeError
#    TypeError is a subclass of Exception, so Exception catches it first.
#    The TypeError block becomes unreachable.

try:
    result = "Score: " + 100  # ❌ str + int → TypeError
except Exception:
    print("Caught by general Exception block.")  # ✅ This runs
except TypeError:
    print("Caught by TypeError block.")          # ❌ This is skipped

# ➤ Case 2: TypeError first, then General Exception
#    Python matches the specific error first and handles it correctly.

try:
    result = "Score: " + 100  # ❌ str + int → TypeError
except TypeError:
    print("Caught by TypeError block.")          # ✅ This runs
except Exception:
    print("Caught by general Exception block.")  # ❌ Not needed here

# ✅ Best Practice:
# ➤ Always list specific exceptions before general ones.
# ➤ This ensures accurate error handling and avoids unreachable code.

# ✅ Correct structure:
# try:
#     risky_code()
# except TypeError:
#     handle_type_error()
# except Exception:
#     handle_other_errors()

# ❌ Incorrect structure:
# try:
#     risky_code()
# except Exception:
#     handle_all_errors()            ## so we don't use superclass first 
# except TypeError:
#     # This will NEVER run




try:
    # ❌ Attempting to open a non-existent file
    with open("missing_file.txt", "r") as f:
        content = f.read()

except TypeError:
    # ❌ This block does NOT run because the error is not a TypeError
    print("Caught by TypeError block.")

except Exception:
    # ✅ This block runs because FileNotFoundError is a subclass of Exception
    print("Caught by general Exception block: File not found.")

# 🔍 Explanation:
# - FileNotFoundError is NOT a TypeError, so Python skips the TypeError block.
# - It matches the general Exception block and executes it.

# ✅ Best Practice:
# ➤ Always list specific exceptions first (e.g., FileNotFoundError, TypeError)
# ➤ Then use a general Exception block to catch anything else.

# ✅ Recommended structure:
# try:
#     risky_code()
# except FileNotFoundError:
#     handle_file_error()
# except TypeError:
#     handle_type_error()
# except Exception:
#     handle_other_errors()

# we can use more than 2 except also as per we required 
# and we can also use try except inside any function or class 

#********************************************************************************##
# in exception we general follow certain rules:
# use alway a specific exception ( i.e write errror type) with proper msg for e.g
try:
    10/0
except ZeroDivisionError as e:
    print ("i am trying to handle a zero division error", e)  #  o/p .. i am trying to handle a zero division error divsin by zero

# alway try to log your error

import logging
logging.basicConfig(filename= "error.log" , level= logging.ERROR)
try:
    10/0
except ZeroDivisionError as e:
    logging.ERROR ("i am trying to handle a zero division error {}", format(e) ) 

# alway avoid to write a multiple exception handling 
try:
    10/0
except FileNotFoundError as e:
    logging.ERROR ("i am trying to handle a file not found {}", format(e) ) 
except AttributeError as e:
    logging.ERROR ("i am trying to handle a attribute error {}", format(e) ) 
except ZeroDivisionError as e:
    logging.ERROR ("i am trying to handle a zero division error {}", format(e) ) 

# cleanup all the resources 