#include<iostream>
using namespace std ;
class Cricketer {
    public:
    string name;
    int runs;
    //this keyword is used to refer to the current object of the class
    Cricketer(string name, int runs) {
        this->name = name; // this->name refers to the attribute of the class  // this keyword is used when there is ambiguity between attribute and parameter
        this->runs = runs; // this->runs refers to the attribute of the class
        // without this keyword, name = name; will assign the parameter to itself and attribute will remain uninitialized
        // this keyword use if we want to give same name to parameter as attribute
        // for information if we don''t use this keyword then it not give error after taking same name for parameter as attribute
        // but we get garbage value 

    }

    void print(){
        cout<<name<<" "<<this->runs<<endl;  // here ouput will be same as this keyword is optional here 
    }  // but in such case if we same name to parameter as attribute then we have to use this keyword for example 

};
void display(Cricketer c) {
    cout << c.name << " " << c.runs << endl;
}
int main(){
    Cricketer c1("Sachin", 10000);
    c1.print(); // output: Sachin 10000
    c1.runs = 10000;
    cout << c1.name << " " << c1.runs << endl;
    return 0;
    //how to display func 
    display(c1); // output: Sachin 10000
}


class Cricketer2 {
    public:
    string name;
    int runs;
    Cricketer2(string name, int runs) {
        this->name = name; 
        this->runs = runs; 
    }

    void print(string name, int runs){
        cout<<name<<" "<<this->runs<<endl;  
    }  
    // return current object
    Cricketer2 getCricketer() {
        return *this; // this is a pointer to the current object // *this is used to dereference the pointer and return the object
    }
};
int main(){
    Cricketer2 c1("Sachin", 10000);
    c1.print("kk", 10); // output: kk 10000  // here name is kk and runs is 10000 because this->runs is used, i.e runs is not changing but name is changing
    cout <<c1.name; // output: Sachin
    //so this is the reason why this keyword is used to refer to the current object of the class
    Cricketer2 c2 = c1.getCricketer(); // getCricketer() returns the current object
    c2.print("Sachin", 10000); // output: Sachin 10000  
    return 0;
}
