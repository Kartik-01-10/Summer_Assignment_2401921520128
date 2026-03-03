# Object-Oriented Programming (OOP) in Python

# Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects",
# which can contain data and code: data in the form of fields (attributes or properties),
# and code in the form of methods (functions).


# -----------------------------------------------------------
# What We Achieve Using OOP
# -----------------------------------------------------------
# 1. **Modularity**: Code is organized into classes, making it easier to manage and understand.
# 2. **Reusability**: Classes and objects can be reused across programs, reducing code duplication.
# 3. **Extensibility**: New features can be added easily by extending existing classes.
# 4. **Maintainability**: Code is easier to update and maintain due to clear structure and encapsulation.
# 5. **Data Hiding**: Encapsulation allows hiding internal object details, exposing only what is necessary.
# 6. **Polymorphism**: Enables using a common interface for different data types, making code flexible and extensible.
# 7. **Abstraction**: Focuses on essential qualities of an object, hiding unnecessary details.

# OOP helps in building complex, scalable, and robust applications. 


# -----------------------------------------------------------
# 1. Class
# -----------------------------------------------------------
# A class is a blueprint for creating objects. It defines a set of attributes and methods
# that the created objects (instances) will have.

# Syntax for creating a class in Python

# class ClassName:
#     def __init__(self, parameters):
#         # initialization code (attributes)
#         self.attribute = value

#     def method_name(self, parameters):
#         # method code
#         pass

# constructors: __init__ method is a special method that is called when an object is instantiated.
# It initializes the object's attributes.
# if we dont define __init__ method then python creates automatically a default constructor. 
# and if we define our own constructor then default constructor is ignored.
# in that we use self keyword to represent the instance of the class. this is the compulsory parameter which we have to pass in every method of class.

# Example:
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")




class Dog:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute

    def bark(self):       # method
        return self.name + " says woof!"
    
a = Dog("Buddy", 3)
print(a.bark(), a.age)  # Output: Buddy says woof! 3

# two types of constructor:
# 1. default constructor : we 1 parameter only self then it is called default constructor   
# 2. parameterized constructor : if we have more than 1 parameter then it is called parameterized constructor

# in python we cannot have multiple constructors like java or c++ but we can achieve that using default parameters in python.
# so we can have only one __init__ method in a class.

# -----------------------------------------------------------
# 2. Object (Instance)
# -----------------------------------------------------------
# An object is an instance of a class. It is created using the class as a blueprint.

my_dog = Dog("Buddy", 3)
my_dog.bark()  # Output: Buddy says woof!

# different types of attributes:
# 1. Instance Attributes: Attributes that are specific to an instance of a class.
# 2. Class Attributes: Attributes that are shared across all instances of a class.
class Student:
    class_name = "Data Science"  # class attribute
    pi = 3.1
    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age # instance attribute
        self.pi = 3.14 # instance attribute

stud1 = Student("Alice", 20)
stud2 = Student("Bob", 22)

print(stud1.name, stud1.age, stud1.class_name)  # Output: Alice 20 Data Science
print(stud2.name, stud2.age, stud2.class_name)  # Output: Bob 22 Data Science
print(stud1.pi, stud2.pi)  # Output: 3.14 3.14  -> here instance attribute pi overrides class attribute pi


# instance, class, and static methods:
# 1. Instance Methods: Methods that operate on an instance of the class and can access instance attributes.
# in this 1st parameter is always self and we can access class and instance attributes using self keyword.

# 2. Class Methods: Methods that operate on the class itself and can access class attributes. They are defined using the @classmethod decorator.
# in this 1st parameter is always cls and we can access class attributes using cls keyword and we cannot access instance attributes using cls keyword.
# here we also use decorator @classmethod to define class method.

# 3. Static Methods: Methods that do not operate on an instance or class and do not have access to instance or class attributes. They are defined using the @staticmethod decorator.
# here we dont have self or cls parameter.
# here we also use decorator @staticmethod to define static method.
# we cannot access instance or class attributes in static method.

# Example: instance method 
class Laptop:
    storage_type = "SSD"  # class attribute
    def __init__(self, RAM, storage):
        self.RAM = RAM          # instance attribute
        self.storage = storage  # instance attribute
    def get_info(self):  # instance method
        print(f"RAM: {self.RAM}, Storage: {self.storage}, Storage Type: {Laptop.storage_type}")
        # here we can also use self.storage_type to access class attribute
l1 = Laptop("16GB", "512GB")
l2 = Laptop("8GB", "256GB")
l1.get_info()  # Output: RAM: 16GB, Storage: 512GB, Storage Type: SSD

# Example: class method
class Laptop2:
    storage_type = "SSD"  # class attribute
    def __init__(self, RAM, storage):
        self.RAM = RAM          # instance attribute
        self.storage = storage  # instance attribute

    @classmethod
    def get_storage_type(cls):  # class method
        return cls.storage_type

l1 = Laptop2("16GB", "512GB")
l2 = Laptop2("8GB", "256GB")
print(l1.get_storage_type())  # Output: SSD

# Example: static method
class Laptop3:
    storage_type = "SSD"  # class attribute
    def __init__(self, RAM, storage):
        self.RAM = RAM          # instance attribute
        self.storage = storage  # instance attribute
    @staticmethod
    def calc_dis(price, discount):
        final_price = price - (price * discount / 100)
        return final_price

print(Laptop3.calc_dis(1000, 10))  # Output: 900.0

# ques product store 
# design & create an online store for products (name, price) track total products being created 
# create static method to apply discount on product price based on a % parameter

class Product:
    count = 0  # class attribute to track total products
    def __init__(self, name, price):
        self.name = name  # instance attribute
        self.price = price  # instance attribute
        Product.count += 1  # increment product count
    def get_info(self):
        return f"Product Name: {self.name}, Price: {self.price}"
    @classmethod
    def get_count(cls):
        return cls.count
    @staticmethod
    def calc_dis(price, discount):
        final_price = price - (price * discount / 100)
        return final_price  
# Testing the Product class
p1 = Product("Laptop", 1000)
p2 = Product("Phone", 500)
print(p1.get_info())  # Output: Product Name: Laptop, Price: 1000
print(Product.get_count())  # Output: 2
print(Product.calc_dis(1000, 10))  # Output: 900.0

    
# we have 3 types :
# public, protected, private
# public : can be accessed from anywhere
# protected : can be accessed within class and its subclasses (convention: single underscore _)
# private : can be accessed only within class (convention: double underscore __)

# -----------------------------------------------------------
# 3. Inheritance
# -----------------------------------------------------------
# Inheritance allows a class to inherit attributes and methods from another class.

class Animal:
    def eat(self):
        print("Eating...")

class Cat(Animal):
    def meow(self):
        print("Meow!")

# -----------------------------------------------------------
# 4. Encapsulation
# -----------------------------------------------------------
# Encapsulation is the concept of hiding the internal state of an object and requiring
# all interaction to be performed through an object's methods.

class Person:
    def __init__(self, name):
        self.__name = name  # private attribute. using double underscore __ makes it private
        self._age = 30      # protected attribute. using single underscore _ makes it protected
    def get_name(self):
        return self.__name
    
# getter and setter methods : used to access and update private attributes

    def get_age(self,name): # getter method
        return self.__name
    
    def set_name(self, newname): # setter method
        self.__name = newname

p1 = Person("Alice")
print(p1.get_name())  # Output: Alice



# -----------------------------------------------------------
# 5. Polymorphism
# -----------------------------------------------------------
# Polymorphism allows different classes to be treated as instances of the same class
# through a common interface.

class Bird:
    def speak(self):
        print("Chirp!")

class Parrot(Bird):
    def speak(self):
        print("Squawk!")

def animal_sound(animal):
    animal.speak()

animal_sound(Bird())    # Output: Chirp!
animal_sound(Parrot())  # Output: Squawk!

# -----------------------------------------------------------
# Summary Table
# -----------------------------------------------------------
# | Concept        | Description                                      |
# |----------------|--------------------------------------------------|
# | Class          | Blueprint for objects                            |
# | Object         | Instance of a class                              |
# | Inheritance    | Deriving new classes from existing ones          |
# | Encapsulation  | Hiding internal details                          |
# | Polymorphism   | Same interface, different implementations        |

# OOP helps organize code, makes it reusable, and easier to maintain.
