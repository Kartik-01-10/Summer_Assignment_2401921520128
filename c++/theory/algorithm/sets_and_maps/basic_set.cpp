// sets is the data structure in which insert element , search element, delete element in 
// O(1)..
// it is not a linear structure 
// imp stl methods : insert(), size(), find(), begin(), end(), erase(), 

// in this values are stored in randam manner/ordered and only unqiue ele stored in it.
// if we insert duplicate ele then it stores one time only..
#include<iostream>
#include<unordered_set>

using namespace std;

int main(){
    unordered_set<int> s;
    s.insert(1);
    s.insert(2);
    s.insert(3);
    s.insert(4);
    s.insert(5);
    s.insert(5);
    s.insert(1);
    // for printing ele we can use for each loop
    for (int ele : s){
        cout<<ele<<" "; // output : 5 4 3 2 1 
    }
    cout<<endl;
    cout << s.size() << endl; // output : 5
    s.erase(5);
    cout << s.size() << endl; // output : 4
    for (auto ele : s){  // when we are using auto then we have to use auto with it
        cout<<ele<<" "; // output : 4 3 2 1 
    }
    cout<<endl;


    // now i have to check is ele present in set or not ..note syntax is tuff
    int target = 4;
    // s.find() -> it searches in the set and if it is not found it returns the last ele
    // s.end() -> getting last ele
    if (s.find(target) != s.end()){// inner condition means target exist
        cout << "exist" << endl;
    }
    else{ // s.find(target) == s.end()
        cout << "not exist" << endl;
    
    } // output of this if else condition is : exist
    // of target = 40 then output will be : not exist 


}