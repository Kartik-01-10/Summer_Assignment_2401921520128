# =========================================
# 📌 What is Custom Exception Handling?
# =========================================

# Custom exception handling allows you to define your own error types
# by creating new exception classes. This is useful when built-in exceptions
# (like ValueError or FileNotFoundError) don't clearly describe the error
# situation in your specific application.

# =========================================
# 📌 Why Do We Use Custom Exceptions?
# =========================================

# ✅ To make error messages more meaningful and specific to the application.
# ✅ To handle domain-specific errors (e.g., InvalidAgeError, InsufficientBalanceError).
# ✅ To improve code readability and debugging.
# ✅ To enforce business rules or validation logic.
# ✅ To separate application-level errors from system-level errors.

# =========================================
# 📌 How to Create a Custom Exception
# =========================================

# - Define a new class that inherits from the built-in Exception class.
# - Optionally, override the __init__ and __str__ methods for custom behavior.

# Syntax:
# class CustomError(Exception):
#     def __init__(self, message):
#         super().__init__(message)


# =========================================
# ✅ Example 1: Invalid Age Exception
# =========================================

class InvalidAgeError(Exception):
    """Raised when the age is not within the valid range."""
    def __init__(self, age, message="Age must be between 18 and 60."):
        self.age = age
        self.message = message
        super().__init__(self.message)                                           #   - super() is a built-in Python function that gives access to methods of a parent (or superclass).
                                                                                 #    In this case, the parent class is Exception
               
def validate_age(age):
    try:
        if age < 18 or age > 60:
            raise InvalidAgeError(age)
        print("Age is valid:", age)
    except InvalidAgeError as e:
        print(f"InvalidAgeError: {e}")
    finally:
        print("Age validation completed.\n")

# Test cases
validate_age(25)   # Valid age
validate_age(15)   # Invalid age
validate_age(70)   # Invalid age


# method 2 :
class valid_age (Exception):

    def __init__(self , msg):
        self.msg = msg

def valid_age (age) :
    if age < 0 :
        raise valid_age("entered age is negative ")
    elif age > 200 :
        raise valid_age("entered age is very high ")
    else :
        print ("age is valid ")
try :
    age = int (input("enter age "))
    valid_age(age)
except valid_age as e:
    print(e)

# basic difference between them is :
# ✅ InvalidAgeError:
# - Follows naming conventions (PascalCase)
# - Has a docstring and structured constructor
# - Separates validation logic from exception class
# - Uses try-except-finally inside the function
# - Clean, reusable, and assignment-ready

# ❌ valid_age:
# - Class and function share same name (confusing)
# - No docstring or structured error message
# - try-except block is outside the function
# - Not modular or maintainable

# =========================================
# ✅ Example 2: Insufficient Balance Exception
# =========================================

class InsufficientBalanceError(Exception):
    """Raised when withdrawal amount exceeds balance."""
    def __init__(self, balance, amount):
        self.message = f"Insufficient balance. Available: ₹{balance}, Requested: ₹{amount}"
        super().__init__(self.message)

def withdraw(balance, amount):
    try:
        if amount > balance:
            raise InsufficientBalanceError(balance, amount)
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: ₹{balance}")
    except InsufficientBalanceError as e:
        print(f"InsufficientBalanceError: {e}")
    finally:
        print("Transaction completed.\n")

# Test cases
withdraw(5000, 3000)   # Valid withdrawal
withdraw(5000, 6000)   # Invalid withdrawal

# =========================================
# ✅ Example 3: Custom Validation Error
# =========================================

class ValidationError(Exception):
    """Raised when input fails custom validation rules."""
    pass

def validate_username(username):
    try:
        if not username.isalnum():
            raise ValidationError("Username must be alphanumeric.")
        print("Username is valid:", username)
    except ValidationError as e:
        print(f"ValidationError: {e}")
    finally:
        print("Username validation completed.\n")

# Test cases
validate_username("Kartik123")   # Valid
validate_username("Kartik@123") # Invalid

# =========================================
# 📌 Summary
# =========================================

# - Custom exceptions help define application-specific error types.
# - They improve clarity, debugging, and enforce business logic.
# - Always inherit from Exception class and provide meaningful messages.
# - Use them with try-except blocks just like built-in exceptions.

# ➤ Explanation of Keywords:
# - try: Wraps code that might raise an error
# - except: Catches and handles specific exceptions
# - finally: Executes cleanup code regardless of exceptions
# - raise: Used to manually trigger an exception