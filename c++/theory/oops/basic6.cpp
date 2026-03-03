// object pointer 
#include<iostream>
using namespace std;

class Cricketer {
    public:
    string name;
    int runs;
    Cricketer(string name, int runs) {
        this->name = name;
        this->runs = runs;
    }

    void print() {
        cout << name << " " << runs << endl;
    }
};

int main() {
    Cricketer c1("Sachin", 10000);
    c1.print(); // output: Sachin 10000

    Cricketer* ptr = &c1; // object pointer
    ptr->print(); // output: Sachin 10000
    cout << ptr->name << " " << ptr->runs << endl; // output: Sachin 10000
    cout << (*ptr).name << " " << (*ptr).runs << endl; // output: Sachin 10000
    // here (*ptr) is used to dereference the pointer and access the object
    (*ptr).runs = 15000; // changing the value of runs using pointer
    ptr->name = "Rahul"; // changing the value of name using pointer
    ptr->print(); // output: Rahul 15000
    // a->b is same as (*a).b
    return 0;
}
// here ptr is pointer to object c1 and we can access the attributes and methods of the object using pointer
// we use -> operator to access the attributes and methods of the object using pointer 