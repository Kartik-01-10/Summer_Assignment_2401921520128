#include <iostream>
using namespace std;
class Node{
    public:
    int val ;
    Node* next ;
    Node(int val){
        this->val = val ;
        this->next = NULL ;
    }
};
class Queue{
    public:
    Node* head ;
    Node* tail ;
    int size ;
    Queue(){
        this->head = NULL ;
        this->tail = NULL ;
        size = 0 ;

    }
    void push(int val){
        Node* temp = new Node(val) ;
        if (size == 0) head = tail = temp ;
        else{
            tail->next = temp ;
            tail = temp ;
        }
        size++ ;
    }
    void pop(){
        if (size == 0) return ;
        Node* temp = head ;
        head = head->next ;
        delete temp ;
        size-- ;
        
    }
    int front(){
        if (size == 0) return -1 ;
        return head->val ;
    }
    int back(){
        if (size == 0) return -1 ;
        return tail->val ;
    }
    int getSize(){
        return size ;
    }
    bool empty(){
        return size == 0 ;
    }
    void display(){
        Node* temp = head ;
        while (temp != NULL) {
            cout<<temp->val<<" " ;
            temp = temp->next ;
        }
        cout<<endl ;    
    }
};
int main(){
    Queue q1 ;
    q1.push(10) ;
    q1.push(20) ;
    q1.push(30) ;
    q1.push(40) ;
    q1.display() ;
    q1.pop() ;
    q1.display() ;
}