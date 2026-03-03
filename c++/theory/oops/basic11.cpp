// multiple inheritance
// e.g. a car is like a vehicle but with more features
#include <iostream>
using namespace std;
class Vehicle{  // parent class
    public:
        int speed;
        float mileage;
    private:
        int bootSpace;

};
class Car : public Vehicle{   // child class  // if we want to access all the detail of vehicle class then we have to use public inheritance
    public:                                // to access all the public members of parent class
        int gears;

};
class Truck : public Vehicle{   // child class  // if we want to access all the detail of vehicle class then we have to use public inheritance
    public:                                // to access all the public members of parent class
        int loadCapacity;

};
int main(){
    Car c1;
    c1.speed = 100;  // we can access speed because it is public in parent class
    c1.mileage = 60.5; // we can access mileage because it is public in parent class
    c1.gears = 5; // we can access gears because it is public in child class
    cout<<"Car Speed: "<<c1.speed<<endl;
    cout<<"Car Mileage: "<<c1.mileage<<endl;
    cout<<"Car Gears: "<<c1.gears<<endl;

    Truck t1;
    t1.speed = 80;  // we can access speed because it is public in parent class
    t1.mileage = 40.5; // we can access mileage because it is public in parent class
    t1.loadCapacity = 1000; // we can access loadCapacity because it is public in child class
    cout<<"Truck Speed: "<<t1.speed<<endl;
    cout<<"Truck Mileage: "<<t1.mileage<<endl;
    cout<<"Truck Load Capacity: "<<t1.loadCapacity<<endl;

    // we cannot access bootSpace because it is private in parent class
    // c1.bootSpace = 20; // Error
    // cout<<"Car Boot Space: "<<c1.bootSpace<<endl; // Error
    // we can only access if we use getter and setter constructor
    return 0;
}



class Cricketer{
    public:
        int runs;
        float average;
        int wickets;
};
class Enginer{
    public:
        int experience;
        string domain;
};
class Phodo : public Cricketer, public Enginer{  // multiple inheritance
    public:
        string name;
        int age;
};