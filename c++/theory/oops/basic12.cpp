// multilevel inheritance
// e.g. a sports car is like a car but with more features
#include <iostream>
using namespace std;
class Vehicle{  // parent class
    public:
        int speed;
        float mileage;
    private:
        int bootSpace;

};
class Car : public Vehicle{   // child class
    public:
        int gears;

};
class SportsCar : public Car{   // child class of Car
    public:
        int turboBoost;

};
int main(){
    SportsCar sc1;
    sc1.speed = 200;  // we can access speed because it is public in parent class
    sc1.mileage = 30.5; // we can access mileage because it is public in parent class
    sc1.gears = 6; // we can access gears because it is public in child class
    sc1.turboBoost = 50; // we can access turboBoost because it is public in child class
    cout<<"Sports Car Speed: "<<sc1.speed<<endl;
    cout<<"Sports Car Mileage: "<<sc1.mileage<<endl;
    cout<<"Sports Car Gears: "<<sc1.gears<<endl;
    cout<<"Sports Car Turbo Boost: "<<sc1.turboBoost<<endl;

    // we cannot access bootSpace because it is private in parent class
    // sc1.bootSpace = 20; // Error
    // cout<<"Sports Car Boot Space: "<<sc1.bootSpace<<endl; // Error
    // we can only access if we use getter and setter constructor
    return 0;
}

