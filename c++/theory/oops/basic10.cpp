// inheritance 
// e.g bike is like scooty but with more features 
#include <iostream>
using namespace std;
class Scooty{  // parent class
    public:
        int speed;
        float mileage;
    private:
        int bootSpace;

};
class Bike : public Scooty{   // child class  // if we want to access all the detail of scooty class then we have to use public inheritance
    public:                                // to access all the public members of parent class
        int gears;
        
};
int main(){
    Bike b1;
    b1.speed = 100;  // we can access speed because it is public in parent class
    b1.mileage = 60.5; // we can access mileage because it is public in parent class
    b1.gears = 5; // we can access gears because it is public in child class
    cout<<"Speed: "<<b1.speed<<endl;
    cout<<"Mileage: "<<b1.mileage<<endl;
    cout<<"Gears: "<<b1.gears<<endl;

    // we cannot access bootSpace because it is private in parent class
    // b1.bootSpace = 20; // Error
    // cout<<"Boot Space: "<<b1.bootSpace<<endl; // Error
    // we can only access if we use getter and setter constructor
    return 0;
}

// there are different type of inheritance which are as follows:
// 1. Single Inheritance : A class can inherit from only one base class.
// 2. Multiple Inheritance : A class can inherit from multiple base classes.
// 3. Multilevel Inheritance : A class can inherit from a derived class, forming a chain.
// 4. Hierarchical Inheritance : Multiple classes can inherit from a single base class.
// 5. Hybrid Inheritance : A combination of two or more types of inheritance.

// Note: Inheritance is a way to reuse the code and it is also a way to achieve polymorphism
// Note: Inheritance is a way to achieve code reusability and it is also a way to achieve polymorphism

// above example is of single inheritance
// if we want to see other types of inheritance then please refer to the following links:
// multiple inheritance : c++/theory/oops/basic11.cpp
// multilevel inheritance : c++/theory/oops/basic12.cpp
