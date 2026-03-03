// access modifier are used to set the access level for class members (attributes and methods).
// There are three access modifiers in C++:
// 1. Public: Members declared as public are accessible from anywhere in the program.
// 2. Private: Members declared as private are accessible only within the class itself.
// 3. Protected: Members declared as protected are accessible within the class and by derived classes.

// public : access in outside class , within class , derived class
// private : access within class only
// protected : access within class and derived class only
#include <iostream>
using namespace std;
class Student{
public:
    int rno;
private:
    string name;
protected:
    float marks;
};
int main(){
    Student s1;
    // we can access rno because it is public
    s1.rno = 101;
    cout<<"Roll number: "<<s1.rno<<endl;
    // we cannot access name because it is private
    // s1.name = "John"; // Error
    // cout<<"Name: "<<s1.name<<endl; // Error  
    // we cannot access marks because it is protected
    // s1.marks = 95.5; // Error

    // we do not want the user to change a particularclass member but we want that user can atleast print it 
    // for that we can use getter and setter functions
}


class Student2{
    public:
        int rno;
        string name;
        Student2(int r, string n, float m){
            rno = r;
            name = n;
            
        }
        Student2(){
            
        }
    private:
        float marks;
    
};
int main(){
    Student2 s1(101, "John", 95.5);  // here we are able to give marks
    cout<<"Roll number: "<<s1.rno<<endl;
    cout<<"Name: "<<s1.name<<endl;
    Student2 s2; // here we are not able to give marks
    //s2.marks = 90.5; // Error
    //count <<"Marks: "<<s2.marks<<endl; // Error

    // so the reason is that marks is private and we are not able to access it directly from outside the class in this case 
    // but in case of above example we are able to give marks because we are giving it through constructor which is public 
    // and we access marks internally 
}



// we can use getter and setter functions to access private members of a class
class Student3{
    public:
        int rno;
        string name;
        Student3(int r, string n, float m){
            rno = r;
            name = n;
            setMarks(m); // we can set marks using setter function
        }
        Student3(){
            
        }
        // setter function to set marks
        void setMarks(float m){
            if(m >= 0 && m <= 100){ // we can add validation here
                marks = m;
            }
            else{
                marks = 0;
            }
        }
        // getter function to get marks
        float getMarks(){
            return marks;
        }
        // we have to use getter and setter functions to access marks from outside the class only when we create 
        // constructor in public section
    private:
        float marks;
    
};
int main(){
    Student3 s1(101, "John", 95.5);  // here we are able to give marks
    cout<<"Roll number: "<<s1.rno<<endl;
    cout<<"Name: "<<s1.name<<endl;
    cout<<"Marks: "<<s1.getMarks()<<endl; // we can get marks using getter function
    Student3 s2; // here we are not able to give marks
    s2.setMarks(90.5); // we can set marks using setter function
    cout<<"Marks: "<<s2.getMarks()<<endl; // we can get marks using getter function
    s2.setMarks(150); // we are trying to set invalid marks
    cout<<"Marks: "<<s2.getMarks()<<endl; // marks will be set to 0 due to validation in setter function
}
