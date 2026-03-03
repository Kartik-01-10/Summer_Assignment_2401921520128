#include <iostream>
#include <vector>
#include <algorithm> // max_element
using namespace std;

// Example 1: simple vector<int>
int main() {
    vector<int> a = {3, 7, 2, 9, 5};
    if (!a.empty()) {
        int mx = *max_element(a.begin(), a.end()); // dereference iterator to get value 
        cout << "max value = " << mx << endl;
    }
    return 0;
}
// explain : we use * to dereference the iterator and get the actual value

// Example 2: get iterator and index safely
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> a = {3, 7, 2, 9, 9, 5};
    if (a.empty()) return 0;
    auto it = max_element(a.begin(), a.end());      // iterator to first max
    int mx = *it;                                   // value
    int idx = distance(a.begin(), it);              // index of that max
    cout << "max = " << mx << " at index " << idx << "\n";
    return 0;
}
// explain : distance gives index from begin to iterator position


// Example 3: custom comparator (max by second element of pair)
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<pair<string,int>> v = {{"a",2}, {"b",5}, {"c",4}};
    // find element with maximum .second
    auto it = max_element(v.begin(), v.end(),
        [](auto &lhs, auto &rhs){ return lhs.second < rhs.second; });
    if (it != v.end()) {
        cout << it->first << " has max second = " << it->second << "\n";
    }
    return 0;
}
// explain  : here we use a lambda function to compare the second elements of the pairs


// Example 4: C-style array
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int arr[] = {10, 3, 8, 12, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    int mx = *max_element(arr, arr + n); // works with pointers too
    cout << "max = " << mx << "\n";
    return 0;
}
// explain : pointers can be used as iterators for C-style arrays

