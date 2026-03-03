#include<iostream>
using namespace std;
class Student{
public:
    string name;  
    int rollno;  
    float cgpa;  
    char gender;  
    Student(string n, int r, float c, char g) {  //constructor
        name = n;             // here what is happening, first n , r , c , g are created and values are assigned to them then 
        rollno = r;         // these values are assigned to the attributes of the class
        cgpa = c;
        gender = g;
    }
};
int main(){ 
    Student  x4("kartik", 55, 8.7, 'm'); //object creation with constructor  but we give value in order of constructor else we get error
    cout<<x4.name<<" "<<x4.rollno<<" "<<x4.cgpa<<" "<<x4.gender;

    // now if we want to initialize attributes as previously we doing
    // Student x5;
    // x5.name = "kartik";
    // x5.rollno = 55;
    // x5.cgpa = 8.7;
    // x5.gender = 'm';
    // we will get error
    // concept is that if i have not created constructor then there is default constructor which allows to initialize attributes in that way
    // but if we have created constructor then there is no default constructor
    //means if we have created constructor then we have to give value in that way only
    // we can do initialization in both way, to do that we have to create another constructor with no parameter
}
// means default is not visible but it is there 
// student() {
 
// }  --> this is default constructor. this is created by compiler if we have not created any constructor
// if we have created any constructor then this is not created by compiler

// if we want to create default constructor also then we have to create it by ourselves

