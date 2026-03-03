# include <iostream>
# include <vector>
using namespace std ;
int sum(vector <int> v1){
    int add = 0;
    for (int x : v1){
        add += x ;
    }
    return  add ; 
}
int main (){
    vector<int> v = {1,2,3,4,5,6};
    sum (v);
}
// here no output will be shown because the result of sum(v) is returned but not used or printed.

int sum(vector<int> v) {
    int total = 0;
    for (int x : v) total += x;
    return total; // Return the result
}

int main() {
    vector<int> v = {1, 2, 3};
    int result = sum(v); // Store the returned value
    cout << "Sum is: " << result << endl; // Print it
}   // now we get output --> 6




// if we want to sort the array in descending order then use this 
//sort(arr.begin(), arr.end(), greater<int>());
/// or if you dont want to use sort func
//reverse(s.begin(), s.end());