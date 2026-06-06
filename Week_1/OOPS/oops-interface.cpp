#include <iostream>
#include <string>

using namespace std;

// 1. Define the Interface (Base Class)
class LibraryUser {
public:
    // Pure virtual functions (the contract)
    virtual void registerAccount() = 0;
    virtual void requestBook() = 0;
};

// 2. Kid User Class
class KidUsers : public LibraryUser {
public:
    int age;
    string bookType;

    void registerAccount() {
        if (age < 12) {
            cout << "You have successfully registered under a Kids Account" << endl;
        } 
        else if (age > 12) {
            cout << "Sorry, Age must be less than 12 to register as a kid" << endl;
        }
    }

    void requestBook() {
        if (bookType == "Kids") {
            cout << "Book Issued successfully, please return the book within 10 days" << endl;
        } 
        else {
            cout << "Oops, you are allowed to take only kids books" << endl;
        }
    }
};

// 3. Adult User Class
class AdultUser : public LibraryUser {
public:
    int age;
    string bookType;

    void registerAccount() {
        if (age > 12) {
            cout << "You have successfully registered under an Adult Account" << endl;
        } 
        else if (age < 12) {
            cout << "Sorry, Age must be greater than 12 to register as an adult" << endl;
        }
    }

    void requestBook() {
        if (bookType == "Fiction") {
            cout << "Book Issued successfully, please return the book within 7 days" << endl;
        } 
        else {
            cout << "Oops, you are allowed to take only adult Fiction books" << endl;
        }
    }
};

// 4. Main Function to run Test Cases
int main() {
    // --- Test Case 1: Kid Setup ---
    cout << "--- Testing KidUser ---" << endl;
    KidUsers kid;
    
    kid.age = 10;
    kid.registerAccount(); // Success
    
    kid.age = 18;
    kid.registerAccount(); // Fails
    
    kid.bookType = "Kids";
    kid.requestBook();     // Success
    
    kid.bookType = "Fiction";
    kid.requestBook();     // Fails
    
    cout << endl;

    // --- Test Case 2: Adult Setup ---
    cout << "--- Testing AdultUser ---" << endl;
    AdultUser adult;
    
    adult.age = 5;
    adult.registerAccount(); // Fails
    
    adult.age = 23;
    adult.registerAccount(); // Success
    
    adult.bookType = "Kids";
    adult.requestBook();     // Fails
    
    adult.bookType = "Fiction";
    adult.requestBook();     // Success

    return 0;
}