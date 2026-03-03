// in case of map also ele stored in random order in key value pair

#include<iostream>
#include<unordered_map>
using namespace std;
// class pair{     :::-> this thing is already built in 
//     public:
//     int first;
//     int second;
// };
int main(){
    // explaination of paired class
    pair<int, int> p ;
    p.first = 1;
    p.second = 2;
    cout<<p.first<<" "<<p.second<<endl; // output: 1 2
    pair<string,char> p1;
    p1.first = "hello";
    p1.second = 'a';
    cout<<p1.first<<" "<<p1.second<<endl; // output: hello a

    // similarly unordered map receives pair 
    unordered_map<string,int> m ;  // here string one is key and int is value..
    // m.insert("kartik",76) --> in c++ this is not the way to input the data in map
    pair<string,int> p2;
    p2.first = "kartik";
    p2.second = 76;
    m.insert(p2);
    pair<string,int> p3;
    p3.first = "kk";
    p3.second = 100;
    m.insert(p3);
    
    // how to print map 
    for (pair<string,int> p : m){
        cout<<p.first<<" "<<p.second<<endl; // output: kartik 76 kk 100
    }
    // second method to print : ie use auto bcz it automatically identify type of data
    for (auto p : m){
        cout<<p.first<<" "<<p.second<<endl; // output: kartik 76 kk 100
    }

    // another method to insert ele

    m["abc"] = 1;
    cout<<m["abc"]<<endl; // output: 1
    m["abc"]++;
    cout<<m["abc"]<<endl; // output: 2

    m["ky"] = 3;

    for (auto p : m){
        cout<<p.first<<" "<<p.second<<endl; // output: kartik 76 kk 100 abc 2 ky 3
    }

    // m.erase(key)
    m.erase("abc");
    m.erase("kk");
    m.erase("jhfdhf"); // there will be no error even if that key is not present

    for (auto p : m){
        cout<<p.first<<" "<<p.second<<endl; // output: kartik 76 ky 3
    }

    cout << m.size(); // output : 2
    
    // m.find(key)
    // and synatx is same as sets
    if (m.find("ky") != m.end()) cout << "exist" ;

}


