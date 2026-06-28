#include <iostream>
using namespace std;

// Abstract class as interface
class Test {
public:
    virtual int square(int n) = 0; // pure virtual function
};

class Arithmetic : public Test {
public:
    int square(int n) override {
        return n * n;
    }
};

int main() {
    Arithmetic obj;
    cout << "Square of 5 = " << obj.square(5) << endl;
    cout << "Square of 10 = " << obj.square(10) << endl;
    return 0;
}
