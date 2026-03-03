// user defined data structure
// create own vector
#include <iostream>
using namespace std;
class Vector {
    public:
    int *arr;
    int capacity;
    int size;
    Vector(){ //default constructor 
        capacity = 1;
        size = 0;
        arr = new int[capacity];
    }

    Vector(int cap) {
        capacity = cap;
        size = 0;
        arr = new int[capacity];
    }

    void add(int value) {
        if (size == capacity) {
            // Resize the array if needed
            int *newArr = new int[capacity * 2];
            for (int i = 0; i < size; i++) {
                newArr[i] = arr[i]; // copy old elements to new array
            }
            delete[] arr;
            arr = newArr; // point to new array but with name arr 
            capacity *= 2;
        }
        arr[size++] = value;
    }

    int get(int index) const {  // 
        if (index >= 0 && index < size) {
            return arr[index];
        }
        throw out_of_range("Index out of range"); // error handling
    }
    void print(){
        for(int i=0;i<size;i++){
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }

    int getSize() const {
        return size;
    }
    void clear() {
        delete[] arr;
        arr = nullptr;
        size = 0;
        capacity = 0;
    }
    void removeLast() {
        if (size > 0) {
            size--;
        }
    }

    ~Vector() {    // destructor , what is use of destructor --> free the memory when 
        delete[] arr;
    }
};
int main(){
    Vector v; // default constructor
    v.add(10);
    v.add(20);
    v.add(30);
    v.print(); // 10 20 30
    cout<<v.get(1)<<endl; // 20
    cout<<v.getSize()<<endl; // 3

    Vector v2(5); // parameterized constructor
    v2.add(100);
    v2.add(200);
    v2.print(); // 100 200
    cout<<v2.get(0)<<endl; // 100
    cout<<v2.getSize()<<endl; // 2

    return 0;
}