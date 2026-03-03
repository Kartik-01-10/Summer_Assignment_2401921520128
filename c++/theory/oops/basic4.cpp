#include <iostream>
using namespace std ;
class Student {
public:
    string name;
    int rollno;
    float cgpa;
    char gender;
    Student() {  // here why we are giving value 
        name = "";
        rollno = 0;
        cgpa = 0.0;
        gender = ' ';
    }
    Student(string n, int r, float c, char g) {
        name = n;
        rollno = r;
        cgpa = c;
        gender = g;
    }
    
};
int main() {
    Student x1;
    cout << x1.name << " " << x1.rollno << " " << x1.cgpa << " " << x1.gender << endl;  // o/p :   0 0.0
    Student x2("John", 101, 9.1, 'M');
    cout << x2.name << " " << x2.rollno << " " << x2.cgpa << " " << x2.gender << endl;
    
    Student x3 = x2; // copy constructor is called here
    cout << x3.name << " " << x3.rollno << " " << x3.cgpa << " " << x3.gender << endl;// output: John 101 9.1 M
    // here there is problem that if we change the value of x2 then x3 will also change because both are pointing to same memory location
    // it is  shallow copy  
    
}

// how to create shallow copy and deep copy
// shallow copy is when both objects are pointing to same memory location
// deep copy is when both objects are pointing to different memory location


class Student2 {
public:
    string name;
    int rollno;
    float cgpa;
    char gender;
    Student2(string n, int r, float c, char g) {
        name = n;
        rollno = r;
        cgpa = c;
        gender = g;
    }
    // copy constructor
    Student2(Student2 &s) { // here we are passing object by reference to avoid infinite loop
        name = s.name;
        rollno = s.rollno;
        cgpa = s.cgpa;
        gender = s.gender;
    }   
};
int main() {
    Student2 x1("John", 101, 9.1, 'M');
    cout << x1.name << " " << x1.rollno << " " << x1.cgpa << " " << x1.gender << endl;// output: John 101 9.1 M
    Student2 x2 = x1; // copy constructor is called here
    cout << x2.name << " " << x2.rollno << " " << x2.cgpa << " " << x2.gender << endl;// output: John 101 9.1 M
    Student2 x3(x1); // copy constructor is called here
    x3.cgpa = 8.5; // changing value of x3.cgpa
    cout << x3.name << " " << x3.rollno << " " << x3.cgpa << " " << x3.gender << endl;// output: John 101 8.5 M
    // here x1.cgpa is not changed because both objects are pointing to different memory location so this is deep copy
    // if we do not create copy constructor then default copy constructor is called which creates shallow copy
    // and in shallow copy both objects are pointing to same memory location so if we change value of one object then other object value also changes
}