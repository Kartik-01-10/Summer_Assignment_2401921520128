// OOPs Concepts in C++ – Complete Guide with Examples and Comments

#include <iostream>
using namespace std;

// 1. Class and Object
// A class is a blueprint for objects. Objects are instances of classes.
class Animal {
public:
    string name; // Attribute

    // 2. Constructor
    // Special function called when object is created
    Animal(string n) {
        name = n;
    }

    // 3. Method (Member Function)
    void speak() {
        cout << name << " makes a sound." << endl;
    }
};

// 4. Inheritance
// A class can inherit properties and methods from another class
class Dog : public Animal {
public:
    Dog(string n) : Animal(n) {} // Constructor calls base class constructor

    // Method overriding (Polymorphism)
    void speak() {
        cout << name << " barks." << endl;
    }
};

// 5. Encapsulation
// Using private members to hide data
class Person {
private:
    int age; // Private attribute

public:
    void setAge(int a) { // Setter
        age = a;
    }
    int getAge() { // Getter
        return age;
    }
};

// 6. Polymorphism
// Compile-time: Function overloading
class Math {
public:
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
};

// Run-time: Method overriding shown above in Dog class

// 7. Abstraction
// Using abstract class (with pure virtual function)
class Shape {
public:
    virtual void draw() = 0; // Pure virtual function
};

class Circle : public Shape {
public:
    void draw() {
        cout << "Drawing Circle" << endl;
    }
};

int main() {
    // Object creation and usage
    Animal a("GenericAnimal");
    a.speak();

    Dog d("Tommy");
    d.speak();

    // Encapsulation example
    Person p;
    p.setAge(25);
    cout << "Person age: " << p.getAge() << endl;

    // Polymorphism example
    Math m;
    cout << "Sum (int): " << m.add(2, 3) << endl;
    cout << "Sum (double): " << m.add(2.5, 3.5) << endl;

    // Abstraction example
    Shape* s = new Circle();
    s->draw();
    delete s;

    return 0;
}

/*
Summary Table

| Concept        | Example/Functionality                  | Description                          |
|----------------|---------------------------------------|--------------------------------------|
| Class          | class Animal {...}                    | Blueprint for objects                |
| Object         | Animal a("Dog");                      | Instance of a class                  |
| Constructor    | Animal(string n) {...}                | Initializes object                   |
| Method         | void speak() {...}                    | Function inside class                |
| Inheritance    | class Dog : public Animal {...}       | Child class inherits parent          |
| Encapsulation  | private, public, getters/setters      | Data hiding                          |
| Polymorphism   | Function overloading/overriding       | Many forms (compile/run time)        |
| Abstraction    | virtual void draw() = 0;              | Hides details, shows essentials      |
*/