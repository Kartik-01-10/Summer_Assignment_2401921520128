#include<iostream>
using namespace std;
class Student {
public:
    string name;  
    int rollno;  
    float cgpa;  
    char gender;  
    Student() {
        
    }
    Student(string n, int r, float c, char g) {  
        name = n;             
        rollno = r;
        cgpa = c;
        gender = g;
    }
};
int main(){ 
    Student  x4("kartik", 55, 8.7, 'm'); 
    cout<<x4.name<<" "<<x4.rollno<<" "<<x4.cgpa<<" "<<x4.gender;
    Student x5;
    cout<<x5.name<<" "<<x5.rollno<<" "<<x5.cgpa<<" "<<x5.gender;
    x5.name = "kartik";
    x5.rollno = 55;
    x5.cgpa = 8.7;
    x5.gender = 'm';
    cout<<x5.name<<" "<<x5.rollno<<" "<<x5.cgpa<<" "<<x5.gender;
}
//there is no error now because we have created default constructor ourselves

// use of parameterized constructor is to initialize attributes at the time of object creation 
// use of default constructor is to create object without giving any value at the time of object creation
// if we want to initialize some attributes and not all then we can do that by creating multiple constructors with different parameters
// this is called constructor overloading
// but if we create multiple constructors with same parameters then we get error

#include<iostream>
using namespace std;
class Car{
public:
    string name;
    string color;
    int price;
    Car(string n) {  //constructor with one parameter
        name = n;             
    }
    Car(string n, string c) {  //constructor with two parameter
        name = n;             
        color = c;         
    }
    Car(string n, string c, int p) {  //constructor with three parameter
        name = n;             
        color = c;         
        price = p;
    }
    Car(int p, string c, string n) {  // we can also change the order of parameters
        name = n;             
        color = c;         
        price = p;
    }
};
int main(){
    Car x1("BMW"); //object creation with constructor with one parameter
    x1.color = "White";
    x1.price = 500000;
    cout<<x1.name<<" "<<x1.color<<" "<<x1.price<<endl; // output: BMW White 500000
    Car x2("Audi", "Red"); //object creation with constructor with two parameter
    cout<<x2.name<<" "<<x2.color<<" "<<x2.price<<endl; // price will be garbage value
    Car x3("Mercedes", "Black", 5000000); //object creation with constructor with three parameter
    cout<<x3.name<<" "<<x3.color<<" "<<x3.price<<endl;
// we get garbage value if we do not initialize attributes
// we can also create default constructor to avoid garbage value
}
