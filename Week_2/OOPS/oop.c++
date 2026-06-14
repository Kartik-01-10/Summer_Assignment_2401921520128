#include <iostream>
using namespace std;

class Playable {
public:
    virtual void play() = 0; 
    virtual ~Playable() {}   
};

// Veena class
class Veena : public Playable {
public:
    void play() override {
        cout << "Playing Veena" << endl;
    }
};

// Saxophone class
class Saxophone : public Playable {
public:
    void play() override {
        cout << "Playing Saxophone" << endl;
    }
};

// Test class with main
int main() {
    // a. Veena instance
    Veena v;
    v.play();

    // b. Saxophone instance
    Saxophone s;
    s.play();

    // c. Using Playable pointer
    Playable* p;

    p = &v;
    p->play();

    p = &s;
    p->play();

    return 0;
}

