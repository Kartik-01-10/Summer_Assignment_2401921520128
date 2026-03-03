// Examples for vector element access and modification

#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {10, 20, 30, 40};

    
    cout << "v[2]: " << v[2] << endl;         // direct access, no bounds check (prints 30)
    cout << "v.at(1): " << v.at(1) << endl;   // access with bounds check (prints 20)
    cout << "Front: " << v.front() << endl;   // first element (prints 10)
    cout << "Back: " << v.back() << endl;     // last element (prints 40)

    
    v.push_back(50);                          // add at end
    v.pop_back();                             // remove last (removes 50)
    v.insert(v.begin() + 2, 25);              // insert 25 at index 2
    v.erase(v.begin() + 1);                   // remove element at index 1 (removes 20)
    // Print vector after modifications
    cout << "After modifications: ";
    for (int x : v) cout << x << " ";
    cout << endl;

    v.clear();                                // remove all elements
    cout << "Size after clear: " << v.size() << endl;

    
    v.resize(5);                              // changes size to 5, adds 0s if increasing
    cout << "After resize to 5: ";
    for (int x : v) cout << x << " ";
    cout << endl;

    v.reserve(20);                            // allocates memory for 20 elements
    cout << "Capacity after reserve(20): " << v.capacity() << endl;

    v.shrink_to_fit();                        // reduces capacity to size
    cout << "Capacity after shrink_to_fit: " << v.capacity() << endl;

    return 0;
}