#include <iostream>
using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node* prev;
    Node(int val) {
        this->val = val;
        this->next = NULL;
        this->prev = NULL;
    }
};

class DLL {
public:
    Node* head;
    Node* tail;
    int size;

    DLL() {
        this->head = NULL;
        this->tail = NULL;
        this->size = 0;
    }

    void insertAtTail(int val) {
        Node* newNode = new Node(val);
        if (size == 0) head = tail = newNode;
        else {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
        size++;
    }

    void insertAtHead(int val) {
        Node* newNode = new Node(val);
        if (size == 0) head = tail = newNode;
        else {
            head->prev = newNode;
            newNode->next = head;
            head = newNode;
        }
        size++;
    }

    void insertAtIdx(int idx, int val) {
        if (idx < 1 || idx > size + 1) {
            cout << "Invalid Index" << endl;
            return;
        }
        if (idx == 1) insertAtHead(val);
        else if (idx == size + 1) insertAtTail(val);
        else {
            Node* newNode = new Node(val);
            Node* temp = head;
            for (int i = 1; i < idx - 1; i++) {
                temp = temp->next;
            }
            newNode->next = temp->next;
            newNode->prev = temp;
            temp->next->prev = newNode;
            temp->next = newNode;
            size++;
        }
    }

    void display() {
        Node* temp = head;
        while (temp != NULL) {
            cout << temp->val << " ";
            temp = temp->next;
        }
        cout << endl;
    }

    void deleteAtHead() {
        if (size == 0) cout << "List is empty" << endl;
        else if (size == 1) head = tail = NULL;
        else {
            head = head->next;
            head->prev = NULL;
        }
        size--;
    }

    void deleteAtTail() {
        if (size == 0) cout << "List is empty" << endl;
        else if (size == 1) head = tail = NULL;
        else {
            tail = tail->prev;
            tail->next = NULL;
        }
        size--;
    }

    void deleteAtIdx(int idx) {
        if (idx < 1 || idx > size) {
            cout << "Invalid Index" << endl;
            return;
        }
        if (idx == 1) deleteAtHead();
        else if (idx == size) deleteAtTail();
        else {
            Node* temp = head;
            for (int i = 1; i < idx - 1; i++) {
                temp = temp->next;
            }
            Node* toDelete = temp->next;
            temp->next = toDelete->next;
            toDelete->next->prev = temp;
            delete toDelete;
            size--;
        }
    }

    int getAtIdx(int idx) {
        if (idx < 1 || idx > size) {
            cout << "Invalid Index" << endl;
            return -1;
        }
        else if (idx == 1) return head->val;
        else if (idx == size) return tail->val;
        else{
            Node* temp = head;
            for (int i = 1; i < idx; i++) {
                temp = temp->next;
            }
            return temp->val;
        }
    }
};

int main() {
    DLL list;
    list.insertAtTail(10);
    list.insertAtTail(20);
    list.insertAtTail(30);
    list.display();

    list.insertAtHead(5);
    list.display();

    list.insertAtIdx(3, 15);
    list.display();

    list.deleteAtHead();
    list.display();

    list.deleteAtTail();
    list.display();

    list.deleteAtIdx(3);
    list.display();

    cout << list.getAtIdx(2) << endl;
}


// i want to optimise getatidx func 
// problem statement :
//      you have a DLL of size 100 & head, tail, size
//      you have to del 80 index element 
// m1 = Node* temp = tail;
//  traverse temp "idx" times
//m2 = Node* temp = tail
//  traverse temp (100-idx)times


// m2 :
// replace full code which  is written in else statement 
// if (idx<size/2){
//     Node* temp = head;
//     for (int i = 1; i < idx; i++) {
//         temp = temp->next;
//     }
//     return temp->val;
// }
// else {
//     Node* temp = tail;
//     for (int i = 1; i < size - idx; i++) {
//         temp = temp->prev;
//     }
//     return temp->val;
// }
// same approach we can use in other function 