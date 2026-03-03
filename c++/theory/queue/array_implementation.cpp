// #include<iostream>
// using namespace std ;
// class Queue{
// public:
//     int f ;
//     int b ;
//     int arr[100] ;
//     Queue(){
//         f = 0 ;
//         b = 0 ;
//     }
//     void push(int val){
//         if (b==100) {
//             cout<<"Queue is full"<<endl ;
//             return ;
//         }
//         arr[b] = val ;
//         b++ ;
//     }
//     void pop(){
//         if (b-f == 0) {
//             cout<<"Queue is empty"<<endl ;
//             return ;
//         }
//         f++ ;
//     }
//     int front(){
//         if (b-f == 0) {
//             cout<<"Queue is empty"<<endl ;
//             return -1 ;
//         }
//         return arr[f] ;
//     }
//     int back(){
//         if (b-f == 0) {
//             cout<<"Queue is empty"<<endl ;
//             return -1 ;
//         }
//         return arr[b-1] ;
//     }
//     int size(){
//         return b-f ;
//     }
//     bool empty(){
//         return b-f == 0 ;
//     }
//     void display(){
//         if (b-f == 0) {
//             cout<<"Queue is empty"<<endl ;
//             return ;
//         }
//         for (int i = f; i < b; i++) {
//             cout<<arr[i]<<" " ;
//         }
//         cout<<endl ;
//     }


// };
// int main(){
//     Queue q ;
//     q.push(10) ;
//     q.push(20) ;
//     q.push(30) ;
//     q.push(40) ;
//     q.display() ;
//     q.pop() ;
//     q.display() ;
//     cout<<q.front()<<endl ;
//     cout<<q.back()<<endl ;
//     cout<<q.size()<<endl ;
//     cout<<q.empty()<<endl ;
//     return 0 ;

// }

/// in this, size is fixed so to make variable use vector


#include<iostream>
#include<vector>
using namespace std ;
class Queue{
public:
    int f ;
    int b ;
    vector<int> arr ;
    Queue(int val){
        f = 0 ;
        b = 0 ;
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
    }
    void pop(){
        if (f-b == 0) {
            cout<<"Queue is empty"<<endl ;
            return ;
        }
        f++ ;
    }
    int front(){
        if (f-b == 0) {
            cout<<"Queue is empty"<<endl ;
            return -1 ;
        }
        return arr[f] ;
    }
    int back(){
        if (f-b == 0) {
            cout<<"Queue is empty"<<endl ;
            return -1 ;
        }
        return arr[b-1] ;
    }
    int size(){
        return b-f ;
    }
    bool empty(){
        return b-f == 0 ;
    }
    void display(){
        if (b-f == 0) {
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
