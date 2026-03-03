#include<iostream>
#include<vector>
#include<string>
#include<fstream> // Required for File Handling

using namespace std;

class Book {
private:
    string title;
    string author_name;
    int uniqueCode;
    bool isIssued;
    int issuedToAdmno;

public:
    Book(string t, string a, int id, bool issued = false, int adno = -1) {
        title = t;
        author_name = a;
        uniqueCode = id;
        isIssued = issued;
        issuedToAdmno = adno;
    }

    void displayBook() {
        cout << "Code: " << uniqueCode << " | Name: " << title << " | Author: " << author_name << " | ";
        if (isIssued) {
            cout << "STATUS: Issued to Admin No: " << issuedToAdmno << endl;
        } else {
            cout << "STATUS: Available" << endl;
        }
    }

    int getCode() { return uniqueCode; }
    string getTitle() { return title; }
    string getAuthor() { return author_name; }
    bool getIsIssued() { return isIssued; }
    int getIssuedToAdmno() { return issuedToAdmno; }

    void issueTo(int adno) {
        isIssued = true;
        issuedToAdmno = adno;
    }

    void returnBook() {
        isIssued = false;
        issuedToAdmno = -1;
    }
};

class Student {
private:
    string name;
    int admNo;

public:
    Student(string n, int a) : name(n), admNo(a) {}
    int getAdmNo() { return admNo; }
    string getName() { return name; }
    void displayStudent() {
        cout << "Adm_no: " << admNo << " | Name: " << name << endl;
    }
};

class Library {
private:
    vector<Book> books;
    vector<Student> students;

public:
    // --- FILE HANDLING LOGIC ---
    void saveData() {
        ofstream bOut("books.txt");
        for (auto &b : books) {
            bOut << b.getCode() << "," << b.getIsIssued() << "," << b.getIssuedToAdmno() << "," 
                 << b.getTitle() << "," << b.getAuthor() << endl;
        }
        bOut.close();

        ofstream sOut("students.txt");
        for (auto &s : students) {
            sOut << s.getAdmNo() << "," << s.getName() << endl;
        }
        sOut.close();
        cout << "\n[System] Data saved to disk." << endl;
    }

    void loadData() {
        ifstream bIn("books.txt");
        if (bIn) {
            int id, adno; bool iss; string t, a, comma;
            while (bIn >> id) {
                bIn.ignore(); // skip comma
                bIn >> iss; bIn.ignore();
                bIn >> adno; bIn.ignore();
                getline(bIn, t, ',');
                getline(bIn, a);
                books.push_back(Book(t, a, id, iss, adno));
            }
        }
        bIn.close();

        ifstream sIn("students.txt");
        if (sIn) {
            int adno; string name;
            while (sIn >> adno) {
                sIn.ignore(); // skip comma
                getline(sIn, name);
                students.push_back(Student(name, adno));
            }
        }
        sIn.close();
    }

    // --- EXISTING LOGIC ---
    void addbook() {
        string t, a; int id;
        cout << "Enter Book ID: "; cin >> id; cin.ignore();
        cout << "Enter Title: "; getline(cin, t);
        cout << "Enter Author: "; getline(cin, a);
        books.push_back(Book(t, a, id));
        saveData(); // Save after adding
    }

    void addStudent() {
        string n; int adno;
        cout << "Enter Name: "; cin.ignore(); getline(cin, n);
        cout << "Enter Adm No: "; cin >> adno;
        students.push_back(Student(n, adno));
        saveData(); // Save after adding
    }

    void showAllBook() {
        if (books.empty()) { cout << "No books found." << endl; return; }
        for (auto &b : books) {
            b.displayBook();
            if (b.getIsIssued()) {
                for (auto &s : students) {
                    if (s.getAdmNo() == b.getIssuedToAdmno())
                        cout << "   -> Held by: " << s.getName() << endl;
                }
            }
        }
    }

    void issueBook() {
        int id, adno; bool sFound = false;
        cout << "Enter Student Adm No: "; cin >> adno;
        for (auto &s : students) { if (s.getAdmNo() == adno) sFound = true; }
        if (!sFound) { cout << "Student not registered!" << endl; return; }

        cout << "Enter Book ID: "; cin >> id;
        for (auto &b : books) {
            if (b.getCode() == id) {
                if (b.getIsIssued()) cout << "Already issued!" << endl;
                else { b.issueTo(adno); saveData(); cout << "Issued!" << endl; }
                return;
            }
        }
        cout << "Book not found!" << endl;
    }

    void showAllStudent() {
        if (students.empty()) { cout << "No students found." << endl; return; }
        for (auto &s : students) s.displayStudent();
    }
};

int main() {
    Library myLibrary;
    myLibrary.loadData(); // Load data on startup
    int choice = 0;

    while (choice != 6) {
        cout << "\n1. Add Book\n2. Show Books\n3. Issue Book\n4. Add Student\n5. Show Students\n6. Exit\nChoice: ";
        if (!(cin >> choice)) {
            cin.clear(); cin.ignore(1000, '\n'); continue;
        }
        switch (choice) {
            case 1: myLibrary.addbook(); break;
            case 2: myLibrary.showAllBook(); break;
            case 3: myLibrary.issueBook(); break;
            case 4: myLibrary.addStudent(); break;
            case 5: myLibrary.showAllStudent(); break;
            case 6: myLibrary.saveData(); cout << "Goodbye!" << endl; break;
            default: cout << "Invalid choice!" << endl;
        }
    }
    return 0;
}