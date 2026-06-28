#include <iostream>
using namespace std;

class Box {
protected:
    int length;
    int breadth;

public:
    Box(int length, int breadth) {
        this->length = length;
        this->breadth = breadth;
    }

    int area() {
        return length * breadth;
    }
};

class Box3D : public Box {
    int height;

public:
    Box3D(int length, int breadth, int height) : Box(length, breadth) {
        this->height = height;
    }

    int volume() {
        return length * breadth * height;
    }
};

int main() {
    Box b(10, 5);
    cout << "Area = " << b.area() << endl;

    Box3D b3(10, 5, 4);
    cout << "Area = " << b3.area() << endl;
    cout << "Volume = " << b3.volume() << endl;

    return 0;
}
