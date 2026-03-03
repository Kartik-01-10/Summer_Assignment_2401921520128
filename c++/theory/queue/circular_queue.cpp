#include<iostream>
#include<vector>
using namespace std ;
class Queue{
public:
    int f ;
    int b ;
    int s ;
    vector<int> arr ;
    Queue(int val){
        f = 0 ;
        b = 0 ;
        s = 0 ;
        vector<int> v(val);
        arr = v ;
    }
    void push(int val){
        if (b==arr.size()) {
            cout<<"Queue is full"<<endl ;
            return ;
        }
        
        arr[b] = val ;
        b++ ;
        s++;
    }
    void pop(){
        if (s == 0) {
            cout<<"Queue is empty"<<endl ;
            return ;
        }
        f++ ;
        s--;
    }
    int front(){
        if (s == 0) {
            cout<<"Queue is empty"<<endl ;
            return -1 ;
        }
        return arr[f] ;
    }
    int back(){
        if (s == 0) {
            cout<<"Queue is empty"<<endl ;
            return -1 ;
        }
        return arr[b-1] ;
    }
    int size(){
        return s ;
    }
    bool empty(){
        return s == 0 ;
    }
    void display(){
        if (s == 0) {
            cout<<"Queue is empty"<<endl ;
            return ;
        }
        for (int i = f; i < b; i++) {
            cout<<arr[i]<<" " ;
        }
        cout<<endl ;
    }


};
int main(){
    Queue q1(10) ;
    q1.push(10) ;
    q1.push(20) ;
    q1.push(30) ;
    q1.push(40) ;
    q1.display() ;
    q1.pop() ;
    q1.display() ;
    
}
