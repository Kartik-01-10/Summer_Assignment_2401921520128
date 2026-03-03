# ================================
# 📌 What is Exception Handling?
# ================================

# Exception handling is a programming technique used to manage errors that occur
# during the execution of a program. Instead of letting the program crash,
# Python allows us to catch and handle these errors using try-except blocks.

# ================================
# 📌 Why Use Exception Handling?
# ================================

# ✅ Prevents program crashes due to unexpected errors.
# ✅ Allows developers to define custom responses to errors.
# ✅ Improves user experience by providing meaningful error messages.
# ✅ Helps isolate faulty code and maintain control flow.
# ✅ Essential for debugging and writing robust applications.

# ================================
# 📌 Common Exceptions in Python
# ================================

# - ZeroDivisionError: Division by zero
# - FileNotFoundError: File not found
# - ValueError: Invalid value (e.g., converting 'abc' to int)
# - TypeError: Operation on incompatible types
# - IndexError: Accessing invalid index in a list
# - KeyError: Accessing missing key in a dictionary

# ================================
# 📌 Syntax of try-except
# ================================

# try:
#     # Code that might raise an exception
# except <ExceptionType>:
#     # Code to handle the exception
# else:
#     # Code that runs if no exception occurs
# finally:
#     # Code that always runs (cleanup, logging, etc.)

# ================================
# ✅ Example 1: Division by Zero
# ================================

def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid input type. Please enter numbers.")
    else:
        print("Division successful.")
    finally:
        print("Execution completed.\n")

# Test cases
divide(10, 2)     # Valid division
divide(10, 0)     # Division by zero
divide(10, 'a')   # Invalid type

# ================================
# ✅ Example 2: File Handling
# ================================

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Cannot read file.")
    else:
        print("File read successfully.")
    finally:
        print("File operation completed.\n")

# Test case
read_file("example.txt")  # Replace with a valid or invalid filename

# ================================
# ✅ Example 3: Value Conversion
# ================================

def convert_to_int(value):
    try:
        number = int(value)
        print("Converted number:", number)
    except ValueError:
        print("Error: Cannot convert to integer.")
    else:
        print("Conversion successful.")
    finally:
        print("Conversion attempt finished.\n")

# Test cases
convert_to_int("123")   # Valid
convert_to_int("abc")   # Invalid

# ================================
# 📌 Summary
# ================================

# - Use try-except to catch and handle runtime errors.
# - Use else for code that should run only if no exception occurs.
# - Use finally for cleanup actions that must run regardless of errors.
# - Exception handling makes your code more reliable and user-friendly.


# ================================
# 🔹 try block
# ================================

# The 'try' block contains code that might raise an exception.
# Python attempts to execute this code. If no error occurs, it proceeds normally.
# If an error occurs, Python immediately jumps to the matching 'except' block.

# ✅ Purpose:
# - To test code that may potentially fail.
# - To isolate risky operations like division, file access, or type conversion.

# Example:
try:
    x = 10 / 0  # This will raise ZeroDivisionError
    print("This line won't execute if error occurs above.")
except ZeroDivisionError:
    print("Caught division by zero.")

# ================================
# 🔹 except block
# ================================

# The 'except' block handles the error raised in the 'try' block.
# You can specify the type of exception to catch (e.g., ZeroDivisionError, ValueError).
# If the error matches, this block runs. If not, Python looks for another matching except.

# ✅ Purpose:
# - To prevent the program from crashing.
# - To provide a custom response or message when an error occurs.

# Example:
try:
    value = int("abc")  # Raises ValueError
except ValueError:
    print("Error: Invalid integer conversion.")

# ================================
# 🔹 else block
# ================================

# The 'else' block runs **only if no exception occurs** in the 'try' block.
# It is useful for code that should run only when everything goes smoothly.

# ✅ Purpose:
# - To separate successful logic from error-handling logic.
# - To keep code clean and readable.

# Example:
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division failed.")
else:
    print("Division successful. Result:", result)

# ================================
# 🔹 finally block
# ================================

# The 'finally' block runs **no matter what happens** — whether an exception occurs or not.
# It is typically used for cleanup actions like closing files, releasing resources, or logging.

# ✅ Purpose:
# - To ensure important final steps are always executed.
# - To maintain consistent program behavior.

# Example:
try:
    print("Trying risky operation...")
    risky = 10 / 0
except ZeroDivisionError:
    print("Caught error.")
finally:
    print("This always runs — cleanup, logging, etc.")



# if we don't know that which error will come then we use exception class so example

try :
    f=open ("abc.txt" , 'r')
except Exception as e :
    print ("this is my except block ", e) 
# o/p --> this is my except block [Errno 2] no such file or directory: 'abc.txt'


try :
    f=open ("abc.txt" , 'w')
    f.write("writeinto file")
    f.close()
except Exception as e :
    print ("this is my except block ", e) 
else : 
    print ("no error ")     # else will we exceute if try block exceute completely successful 



# there is also one more block named finally and it will execute always whether we arre getting error or not 

 
