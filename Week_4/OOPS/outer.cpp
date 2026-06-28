#include <iostream>
using namespace std;

class Outer {
public:
    void display() {
        cout << "Display method of Outer class" << endl;
    }

    class Inner {
    public:
        void display() {
            cout << "Display method of Inner class" << endl;
        }
    };
};

int main() {
    Outer obj;
    obj.display();

    Outer::Inner in;
    in.display();

    return 0;
}
