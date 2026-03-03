// what is constructor overloading?
// constructor overloading is a way to have multiple constructors in a class with different parameters of same name
// eg :
// class Box{
//     public:
//         Box(int l, int b, int h){          ------> constructor overloading
//             length = l;
//             breadth = b;
//             height = h;
//         }
//         Box(int s){                        ------> constructor overloading      // same name but different parameters
//             length = breadth = height = s;
//         }
//     private:
//         int length, breadth, height;
// };


// here we have one more point that if we are doing func overloading then return type is has to be same 
// if return type is different then it will give error
// eg :
// int add(int a, int b){
//     return a + b;
// }
// float add(float a, float b){
//     return a + b;
// }   // this will give error because return type is different
// why we are learning this bcz in polymorphism naam ek , kaam kai

//operator overloading : e.g + is an operator which perform different operation for different data type
// eg : int a = 10, b = 20; cout<<a + b; // here + is performing addition operation
// eg : string s1 = "Hello", s2 = "World"; cout<<s1 + s2; // here + is performing concatenation operation

// polymorphism : two types : compile time polymorphism and run time polymorphism
// compile time polymorphism : function overloading and operator overloading
// run time polymorphism : virtual function and pure virtual function

// create fraction class which can perform different class operations 
#include <iostream>
using namespace std;
class Fraction{
    private:
        int numerator;
        int denominator;
    public:
        // constructor overloading
        Fraction(int n, int d){
            numerator = n;
            denominator = d;
        }
        Fraction(int n){
            numerator = n;
            denominator = 1;
        }
        void display(){
            cout<<numerator<<" / "<<denominator<<endl;
        }
        // operator overloading
            Fraction operator + (Fraction f){  //here if you want to give func name here then remove operator + by variable name 
            int n = numerator * f.denominator + f.numerator * denominator;
            int d = denominator * f.denominator;
            return Fraction(n, d);
        }
        Fraction operator - (Fraction f){
            int n = numerator * f.denominator - f.numerator * denominator;
            int d = denominator * f.denominator;
            return Fraction(n, d);
        }
        Fraction operator * (Fraction f){
            int n = numerator * f.numerator;
            int d = denominator * f.denominator;
            return Fraction(n, d);
        }
};
int main(){
    Fraction f1(3, 4); // 3/4
    Fraction f2(2); // 2/1
    Fraction f3 = f1 + f2; // operator overloading
    Fraction f4 = f1 - f2; // operator overloading
    Fraction f5 = f1 * f2; // operator overloading
    f3.display(); // 11/4
    f4.display(); // -5/4
    f5.display(); // 6/4
    return 0;
}


//diff btw func overloading and func overriding
// func overloading : same func name but different parameters
// func overriding : same func name and same parameters but different classes (base class and derived class)

//now run time polymorphism
// virtual function : a function in base class which is overridden in derived class
// when we use base class pointer to point to derived class object then base class pointer will call derived class function
// eg : use of virtual function and without virtual function also
class Animal{
    public:
        void speak(){
            cout<<"Animal is speaking"<<endl;
        }
        virtual void sound(){   // virtual function
            cout<<"Animal is making sound"<<endl;
        }
};
class Dog : public Animal{
    public:
        void speak(){
            cout<<"Dog is speaking"<<endl;
        }
        void sound(){   // overriding virtual function
            cout<<"Dog is barking"<<endl;
        }
};
int main2(){
    Animal a;
    Dog d;
    Animal *ptr; // base class pointer
    ptr = &a;
    ptr->speak(); // Animal is speaking
    ptr->sound(); // Animal is making sound
    ptr = &d;
    ptr->speak(); // Animal is speaking (because speak() is not virtual function)
    ptr->sound(); // Dog is barking (because sound() is virtual function)
    Animal* ptr2 = new Dog(); // base class pointer pointing to derived class object
    ptr2->speak(); // Animal is speaking
    ptr2->sound(); // Dog is barking   // bcz sound() is virtual function
    delete ptr2; // free memory
    return 0;
}
// so what is the adv of virtual function over non virtual function
// when we use base class pointer to point to derived class object then base class pointer will call derived class function
// but when we use base class pointer to point to derived class object then base class pointer will call base class function
// so this is the adv of virtual function over non virtual function


// use of static and const keyword in class
class Counter{
    private:
        static int count; // static variable
    public:
        Counter(){
            count++;
        }
        static int getCount(){ // static function
            return count;
        }
};
int Counter::count = 0; // static variable
int main3(){
    Counter c1;
    Counter c2;
    Counter c3;
    cout<<"Count: "<<Counter::getCount()<<endl; // Count: 3
    return 0;
}
// const keyword in class
class Circle{   
    private:
        const float pi; // const variable
        float radius;
    public:
        Circle(float r) : pi(3.14), radius(r){} // const variable must be initialized in constructor
        float area() const{ // const function
            return pi * radius * radius;
        }
};
int main4(){
    Circle c(5);
    cout<<"Area: "<<c.area()<<endl; // Area: 78.5
    return 0;
} 
// diff btw static and const 
// static : memory is allocated only once and shared by all objects of the class and can be accessed without creating object of class
// const : value cannot be changed once initialized and must be initialized in constructor and can only be accessed through object of class
