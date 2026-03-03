#include<iostream>
using namespace std;
class Node{
    public:
    int data;
    Node* next;
    Node* prev;
    Node(int data){
        this->data=data;
        this->next=NULL;
        this->prev=NULL;
    }    
};
class Deque{
    public:
    Node* head;
    Node* tail;
    int size;
    Deque(){
        head=NULL;
        tail=NULL;
        size=0;
    }
    void pushBack(int data){
        Node* temp =new Node(data);
        if (size==0){
            head=temp;
            tail=temp;
        }
        else{
            tail->next=temp;
            temp->prev=tail;
            tail=temp;
        }
        size++;
    }
    void pushFront(int data){
        Node* temp =new Node(data);
        if (size==0){
            head=temp;
            tail=temp;
        }
        else{
            head->prev=temp;
            temp->next=head;
            head=temp;
        }
        size++;
    }
    void popFront(){
        if (size==0){
            cout<<"empty"<<endl;
            return;
        }
        head=head->next;
        if (head) head->prev=NULL;
        if(head == NULL) tail=NULL;
        size--;
    }
    void popBack(){
        if (size==0){
            cout<<"empty"<<endl;
            return;
        }
        else if (size==1){
            head=NULL;
            tail=NULL;
        }
        Node* temp=tail;
        tail=tail->prev;
        tail->next=NULL;
        delete temp;
        size--;
    
    }
    int front(){
        if (size == 0) return -1 ;
        return head->data ;
    }
    int back(){
        if (size == 0) return -1 ;
        return tail->data ;
    }
    int getSize(){
        return size ;
    }
    bool empty(){
        return size == 0 ;
    }
    void display(){
        Node* temp=head;
        while(temp){
            cout<<temp->data<<" ";
            temp=temp->next;
        }
        cout<<endl;
    }
        
        
};
int main(){
    Deque d;
    d.pushBack(1);
    d.pushBack(2);
    d.pushBack(3);
    d.pushBack(4);
    d.pushFront(5);
    d.display();
    cout<<d.front()<<endl;
    cout<<d.back()<<endl;
    d.popFront();
    d.popBack();
    d.display();
    cout<<d.front()<<endl;
    cout<<d.back()<<endl;
    cout<<d.getSize()<<endl;
    cout<<d.empty()<<endl;
    return 0;

}