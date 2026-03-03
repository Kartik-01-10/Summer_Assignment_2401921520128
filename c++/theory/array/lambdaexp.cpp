
// different way to use 
#include <iostream>
using namespace std;

int main() {
    
    // Defining a lambda
    auto res = [](int x) {
        return x + x;
    };
    cout << res(5);
    
    return 0;
} // op 10
//    auto res = [](int x) {
//        return x + x;
//    };  here res is a variable which stores the lambda function
//    [] this is called capture list and it is used to capture variables from the surrounding scope
//    (int x) this is the parameter list of the lambda function
//    { return x + x; } this is the body of the lambda function
//    ; this is used to terminate the lambda expression
//    auto is used to automatically deduce the type of the variable res 
//    we can also use explicit type instead of auto like this : int (*res)(int) = [](int x) { return x + x; };
//    here int (*res)(int) is a function pointer that points to a function that takes an int as parameter and returns an int
//    but using auto is more convenient and less error-prone
//    we can also define and call the lambda function in one line like this : cout << [](int x) { return x + x; }(5);


// [&]: capture all external variables by reference.
// [=]: capture all external variables by value.
// [a, &b]: capture 'a' by value and 'b' by reference


#include <iostream>
#include <vector>
using namespace std;

void print(vector<int> v) {
    for (auto x : v) cout << x << " "; // here auto is used to automatically deduce the type of x
    cout << endl;
}

int main() {
    vector<int> v1, v2;

    // Capture v1 and v2 by reference
    auto byRef = [&] (int m) {
        v1.push_back(m);
        v2.push_back(m);
    };
    
    // Capture v1 and v2 by reference instead of value to modify outer vectors
    auto byVal = [&] (int m) {
        v1.push_back(m);
        v2.push_back(m);
    };
    
    // Capture v1 by reference and v2 by reference
    auto mixed = [&v1, &v2] (int m) {
        v1.push_back(m);
        v2.push_back(m);
    };

    // Push 20 in both v1 and v2
    byRef(20);
    
    // Push 234 in both v1 and v2
    byVal(234);
    
    // Push 10 in both v1 and v2
    mixed(10);
    
    print(v1);
    print(v2);
    
    return 0;
}
// op : 20 234 10
//      20 234 10
// explain this auto func  :
//Instead of manually writing the type, like int, float, vector<int>::iterator, etc., you let the compiler deduce it.
auto x = 5;        // Compiler sees 5 is int → x becomes int
auto y = 3.14;     // y becomes double
auto z = "hello";  // z becomes const char*

// where we can use auto 
//1. Storing a Lambda Function
auto res = [](int x) { return x + x; };
// - res is a variable that holds a lambda function.
// - The compiler deduces the type of res as a callable object.
// - You could write it explicitly as:

int (*res)(int) = [](int x) { return x + x; };
// but auto is cleaner and safer 

// 2. range 
//for (auto x : v) cout << x << " ";


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	vector<int> v = {5, 1, 8, 3, 9, 2};

	// Sort in descending order
	sort(v.begin(), v.end(), [] (const int& a, const int&b) {
		return a > b;
	});

	for (int x : v)
		cout << x << " ";
	return 0;
}
// op : 9 8 5 3 2 1
// here we use lambda func to sort array in descending order



#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	vector<int> v = {5, 1, 8, 3, 9, 2};

	// Sort in descending order
	auto it = find_if(v.begin(), v.end(), [] (const int& a) {
		return a % 3 == 0;
	});

    if (it != v.end()) cout << *it;
	else cout << "No such element";
	return 0;
}
// op : 3
// here we use lambda func to find first ele which is divisible by 3