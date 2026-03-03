#include <iostream>
#include <string>
using namespace std;
class Node {
    public:
    int val;
    Node* next;
    Node(int v = 0) : val(v), next(NULL) {}
};
void display(Node* head){
    Node* temp = head;
    while (temp!=NULL){
        cout << temp->val << endl;
        temp = temp->next;
    }
}
int size(Node* head){
    Node* temp = head ;
    int n = 0 ;
    while (temp!=NULL){
        n++;
        temp = temp->next;
    }
    return n;
}

void displayrev(Node* head){
    if (head == NULL) return ;
    displayrev(head->next);
    cout << head->val << endl;
}
void insertatstr(Node* head , int size , int val){
    // append a new node with value val to the end of the list
    if (head == NULL) return;
    Node* newNode = new Node(val);
    Node* temp = head;
    while (temp->next != NULL){
        temp = temp->next;
    }
    temp->next = newNode;
}

int main(){
    Node a;
    a.val = 1;
    a.next = NULL;
    Node b;
    b.val = 2;
    b.next = NULL;
    a.next = &b;
    Node c;
    c.val = 3;
    c.next = NULL;
    b.next = &c;

    display(&a);
    size(&a);
    displayrev(&a);
    int val = 10;
    insertatstr(&a,size(&a), val);

   
    
}