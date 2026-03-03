//dynamic allocation of objects
#include <iostream>
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
int main() {    // in dynamic allocation memory is allocated at runtime 
    // what is diff btw compile time and runtime? --> compile time is when the code is being compiled and runtime is when the code
    // is being executed and memory is allocated at runtime using new keyword
    Cricketer* ptr = new Cricketer("Sachin", 10000); // dynamic allocation of object
    ptr->print(); // output: Sachin 10000  // means (*ptr).print()
    delete ptr; // deallocating memory
    
    int* p = new int; // dynamic allocation of integer
    *p = 10;
    cout << *p << endl; // output: 10
    delete p; // deallocating memory

    int* arr = new int[5]; // dynamic allocation of array
    for(int i=0; i<5; i++) {
        arr[i] = i+1;
    }
    for(int i=0; i<5; i++) {
        cout << arr[i] << " ";
    }
    delete[] arr; // deallocating memory


    Cricketer* c1 = new Cricketer("Dhoni", 8000);
    c1->print(); // output: Dhoni 8000
    delete c1; // deallocating memory   

    
    Cricketer* team = new Cricketer[3] {Cricketer("Virat", 12000), Cricketer("Rohit", 9000), Cricketer("Jadeja", 5000)}; // dynamic allocation of array of objects
    for(int i=0; i<3; i++) {
        team[i].print();
    }
    delete[] team; // deallocating memory
}