#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

// Function to split list into two halves
Node* getMiddle(Node* head) {
    if (!head) return head;
    Node* slow = head;
    Node* fast = head->next;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

// Merge two sorted lists
Node* merge(Node* left, Node* right) {
    if (!left) return right;
    if (!right) return left;

    Node* result;
    if (left->data <= right->data) {
        result = left;
        result->next = merge(left->next, right);
    } else {
        result = right;
        result->next = merge(left, right->next);
    }
    return result;
}

// Merge sort for linked list
Node* mergeSort(Node* head) {
    if (!head || !head->next) return head;

    Node* middle = getMiddle(head);
    Node* nextToMiddle = middle->next;
    middle->next = nullptr;

    Node* left = mergeSort(head);
    Node* right = mergeSort(nextToMiddle);

    return merge(left, right);
}

// Utility functions
void printList(Node* head) {
    while (head) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    Node* head = new Node(4);
    head->next = new Node(2);
    head->next->next = new Node(1);
    head->next->next->next = new Node(3);

    cout << "Original list: ";
    printList(head);

    head = mergeSort(head);

    cout << "Sorted list: ";
    printList(head);

    return 0;
}

// 2 method 
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

void printList(Node* head) {
    while (head) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

void sortList(Node* head) {
    vector<int> arr;
    Node* temp = head;

    // Step 1: Copy values into vector
    while (temp) {
        arr.push_back(temp->data);
        temp = temp->next;
    }

    // Step 2: Sort the vector
    sort(arr.begin(), arr.end());

    // Step 3: Put sorted values back into linked list
    temp = head;
    int i = 0;
    while (temp) {
        temp->data = arr[i++];
        temp = temp->next;
    }
}

int main() {
    // Create linked list: 4 -> 2 -> 1 -> 3
    Node* head = new Node(4);
    head->next = new Node(2);
    head->next->next = new Node(1);
    head->next->next->next = new Node(3);

    cout << "Original list: ";
    printList(head);

    sortList(head);

    cout << "Sorted list: ";
    printList(head);

    return 0;
}
