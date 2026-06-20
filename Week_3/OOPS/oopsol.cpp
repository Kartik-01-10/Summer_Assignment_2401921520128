#include <iostream>
#include <cstdlib>   
#include <ctime>     

using namespace std;

// Abstract base class
class Compartment {
public:
    virtual string notice() = 0; 
    virtual ~Compartment() {}    
};

// Derived classes
class FirstClass : public Compartment {
public:
    string notice() {
        return "This is a First Class compartment";
    }
};

class Ladies : public Compartment {
public:
    string notice() {
        return "This is a Ladies compartment";
    }
};

class General : public Compartment {
public:
    string notice() {
        return "This is a General compartment";
    }
};

class Luggage : public Compartment {
public:
    string notice() {
        return "This is a Luggage compartment";
    }
};


int main() {
    srand(time(0)); 

    Compartment* compartments[10]; 

    for (int i = 0; i < 10; i++) {
        int randNum = 1 + rand() % 4; 
        switch (randNum) {
            case 1: compartments[i] = new FirstClass(); break;
            case 2: compartments[i] = new Ladies(); break;
            case 3: compartments[i] = new General(); break;
            case 4: compartments[i] = new Luggage(); break;
        }
    }

    
    for (int i = 0; i < 10; i++) {
        cout << compartments[i]->notice() << endl;
        delete compartments[i]; 
    }

    return 0;
}
