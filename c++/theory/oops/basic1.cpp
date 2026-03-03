#include <iostream>
using namespace std;
class Student{
public:
    string name;  //these are attributes
    int rollno;  //these are attributes
    float cgpa;  //these are attributes
    char gender;  //these are attributes
};
int main(){
    Student  x;           // here x, x1, x2 are objects of class Student
    x.name = "kartik";
    x.rollno = 55;
    x.cgpa = 8.7;
    x.gender = 'm';

    Student  x1;
    x1.name = "kartik";
    x1.rollno = 55;
    x1.cgpa = 8.7;
    x1.gender = 'm';
    
    //print
    cout<<x.name<<" "<<x.rollno<<" "<<x.cgpa; // output: kartik 55 8.7
    // how to take input from user
    Student  x2;
    cout<<"Enter name: ";
    cin>>x2.name;
    cout<<"Enter rollno: ";
    cin>>x2.rollno;
    cout<<"Enter cgpa: ";
    cin>>x2.cgpa;
    cout<<"Enter gender: ";
    cin>>x2.gender;

    cout<<x2.name<<" "<<x2.rollno<<" "<<x2.cgpa<<" "<<x2.gender;
    
    printStudentInfo(x);  //output: kartik 55 8.7 m
    printStudent(x);     //output: kartik 55 8.7 m
}

// how to print all attributes of an object using function 
void printStudentInfo(const Student& s) {  //here it is pass by reference
    cout << s.name << " " << s.rollno << " " << s.cgpa << " " << s.gender << endl;
}
// why we use const here because we don't want to change the original object
// if we don't use const then we can change the original object inside the function bcz this is pass by reference
// so to prevent that we use const keyword

void printStudent(Student s) {  //here it is pass by value
    cout << s.name << " " << s.rollno << " " << s.cgpa << " " << s.gender << endl;
}
// here what is difference between pass by reference and pass by value
//  -->in pass by value a copy of the object is created and passed to the function
// -->in pass by reference no copy is created, the original object is used in the function
// so if we make any changes to the object inside the function, it will affect the original object


// in case of pass by value if we change the object inside the function, it will not affect the original object

// how i can initilize the attributes in one line 
// we can use constructor for that
// but we will learn that in next file
