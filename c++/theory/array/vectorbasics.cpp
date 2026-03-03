/*
===========================
Complete C++ Vector Mastery Guide (with Comments)
===========================

1. What is a vector?
- vector is a dynamic array in C++.
- Its size can grow or shrink at runtime.
- Part of the C++ STL.
- Header file: <vector>

2. Difference between vector and array
// Array: fixed size, stack memory, no STL support, copies by default
// Vector: dynamic size, heap memory, STL support, can use reference

3. Accessing elements
// v[i];       // direct access, no bounds check
// v.at(i);    // access with bounds check
// v.front();  // first element
// v.back();   // last element

4. Adding & removing elements
// v.push_back(10);          // add at end
// v.pop_back();             // remove last
// v.insert(v.begin()+i, x); // insert x at index i
// v.erase(v.begin()+i);     // remove element at index i
// v.clear();                // remove all

// Complexity:
// push_back → O(1) amortized
// insert/erase → O(n)
// pop_back → O(1)

5. Resize, reserve, shrink_to_fit
// v.resize(10);       // changes size, adds 0s if increasing
// v.reserve(20);      // allocates memory for 20 elements
// v.shrink_to_fit();  // reduces capacity to size

#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v;
    v.reserve(10);           // Capacity: 10, Size: 0
    v.resize(5);             // Capacity: 10, Size: 5
    cout << v.empty();       // Output: 0 (false)
    v.clear();               // Size: 0
    cout << v.empty();       // Output: 1 (true)
    v.shrink_to_fit();       // Capacity may reduce to 0
}


🔹 resize(n)
- If n > current size: Adds default-initialized elements.
- If n < current size: Removes elements from the end.
- May reallocate memory if n > current capacity.
🔹 reserve(n)
- Ensures capacity is at least n.
- Useful to avoid multiple reallocations during push_back.
- Does not change the number of elements.
🔹 shrink_to_fit()
- Attempts to free unused memory.
- After many pop_back() or resize() calls, capacity may remain high.
- This is a non-binding request — the compiler may ignore it.
🔹 empty()
- Equivalent to vec.size() == 0.
- Very fast — just checks internal size counter.


}
// Key Points:
// size() vs capacity()
// Use reserve() to optimize large data inserts

6. Iterating vectors
// Range-based for: for (int x : v)  /* use x */ 
// syntax :
// for (declaration : range) {
//     // loop body
// }    here - declaration: Variable that represents each element.
//- range: Container or iterable object (e.g., array, vector, map).
#include <vector>
#include <iostream>
using namespace std;
int main() {
vector<int> v = {1, 2, 3, 4, 5};
for (int x : v) {
    cout << x << " ";
}
for (int& x : v) {
    x += 10;  // modifies original vector
}
for (const int& x : v) {
    cout << x << " ";  // safe, no modification
}
}


// Index-based for: for (int i=0;i<v.size();i++){ /* use v[i] */ }
// Iterator-based: for (auto it=v.begin(); it!=v.end(); it++){ cout << *it; }
// Reverse iterator: for (auto it=v.rbegin(); it!=v.rend(); it++){ /* use *it */ }

//7. Passing vector to functions
// By value: void func(vector<int> v);
// By reference: void func(vector<int>& v);
// By const reference: void func(const vector<int>& v);


//8. Returning a vector
// vector<int> createVector() { return {1,2,3}; }

//9. 2D vectors
// vector<vector<int>> matrix(n, vector<int>(m,0));
// matrix[1][2] = 5;

// Jagged array:
// vector<vector<int>> jagged(3);
// jagged[0] = {1,2};
// jagged[1] = {3,4,5};
// jagged[2] = {6};

// Jagged Array in C++ using vector<vector<int>>

/*
A jagged array is an array of arrays where each sub-array can have a different size.
In C++, you can easily create jagged arrays using vector<vector<int>>.

Why use jagged arrays?
- Useful when each row needs a different number of columns.
- Common in problems where data is not rectangular (e.g., adjacency lists in graphs).

How to declare and use a jagged array:
*/

#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Declare a jagged array with 3 rows
    vector<vector<int>> jagged(3);

    // Assign different sized vectors to each row
    jagged[0] = {1, 2};         // Row 0 has 2 elements
    jagged[1] = {3, 4, 5};      // Row 1 has 3 elements
    jagged[2] = {6};            // Row 2 has 1 element

    // Print the jagged array
    for (int i = 0; i < jagged.size(); i++) {
        cout << "Row " << i << ": ";
        for (int val : jagged[i]) {
            cout << val << " ";
        }
        cout << endl;
    }
    return 0;
}


// Output:
// Row 0: 1 2 
// Row 1: 3 4 5 
// Row 2: 6 

// Key Points:
// - Each row can have a different number of elements.
// - Access elements using jagged[row][col].
// - Useful for representing non-rectangular data

//10. Common vector operations in LeetCode
// push_back(x) → O(1) amortized
// pop_back() → O(1)
// insert(pos,x) → O(n)
// erase(pos) → O(n)
// resize(n) → O(n)
// access: v[i] / v.at(i) → O(1)
// front(), back() → O(1)
// sort(v.begin(),v.end()) → O(n log n)
// reverse(v.begin(),v.end()) → O(n)
// binary search: lower_bound, upper_bound → O(log n)

//11. Tips for reading LeetCode vector problems
// Look at function signature: inputs & outputs
// Check & or const &
// 2D vector: matrix[i][j], jagged allowed
// Loops: range-for for read-only, index-for for indices
// Returning vector: return {…} is safe

//12. Key points & summary
// vector<int> → dynamic array
// & → pass by reference
// const & → read-only reference
// Returning vector<int> → safe
// Loops: range-for, index-for, iterator
// 2D vectors → vector<vector<int>>
// Key STL functions: push_back, pop_back, insert, erase, sort, reverse, lower_bound, upper_bound
// Use reserve() to reduce reallocations
// Use at() for safe access in user input scenarios

//13. Advanced concepts
// vector of pairs: vector<pair<int,int>> vp;
// vector of vectors for graphs or matrices
// Iterator invalidation: after insert/erase, old iterators may become invalid
// Emplace_back(x): constructs in-place, faster than push_back for objects
// Using STL algorithms: sort, reverse, unique, lower_bound, upper_bound, find, accumulate
// 2D vector traversal: nested loops, range-for recommended


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Example: Sum all elements of a vector (read-only, use const reference)
int sumVector(const vector<int>& nums) {
    int sum = 0;
    for (int x : nums) sum += x;
    return sum;
}

// Example: Reverse a vector (modifies original, returns by value)
vector<int> reverseVector(vector<int>& nums) {
    reverse(nums.begin(), nums.end());
    return nums;
}
// - Parameter Type: vector<int>&
// - The & means you're passing the vector by reference, not by value.
// - This avoids copying the entire vector — faster and memory-efficient.
// - Any changes made to nums inside the function will affect the original vector outside.
// it means if we change or modify it will not update in original if we don't use "&" 


// Example: Find two indices whose values sum to target
vector<int> twoSum(vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] + nums[j] == target) return {i, j};
        }
    }
    return {};
}

// Example: Return a simple vector
vector<int> createVector() {
    return {1, 2, 3, 4, 5};
}

// Example: Return all even numbers up to n
vector<int> getEvenNumbers(int n) {
    vector<int> evens;
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) evens.push_back(i);
    }
    return evens;
}

// Example: Create and return a 2D vector (matrix)
vector<vector<int>> createMatrix(int n, int m) {
    vector<vector<int>> matrix(n, vector<int>(m, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            matrix[i][j] = i + j;
    return matrix;
}

// Example: Create and return a vector of pairs
vector<pair<int, int>> createPairs(int n) {
    vector<pair<int, int>> vp;
    for (int i = 1; i <= n; i++)
        vp.push_back({i, i * 2});
    return vp;
}

int main() {
    // Create and print a vector
    vector<int> result = createVector();
    for (int x : result) cout << x << " ";
    cout << endl;

    // Get and print even numbers up to 10
    vector<int> evenList = getEvenNumbers(10);
    for (int x : evenList) cout << x << " ";
    cout << endl;

    // Create and print a 3x4 matrix
    vector<vector<int>> mat = createMatrix(3, 4);
    for (auto row : mat) {
        for (int val : row) cout << val << " ";
        cout << endl;
    }

    // Create and print vector of pairs
    vector<pair<int, int>> pairs = createPairs(3);
    for (auto p : pairs) cout << "(" << p.first << "," << p.second << ") ";
    cout << endl;

    // Sum elements of a vector
    vector<int> nums = {1, 2, 3, 4, 5};
    cout << "Sum: " << sumVector(nums) << endl;

    // Reverse and print a vector
    vector<int> reversed = reverseVector(nums);
    for (int x : reversed) cout << x << " ";
    cout << endl;

    // Find two indices whose values sum to 7
    vector<int> indices = twoSum(nums, 7);
    if (!indices.empty())
        cout << "Two Sum indices: " << indices[0] << ", " << indices[1] << endl;
    else
        cout << "No two numbers add up to target." << endl;

    return 0;
}


//Returning Vectors in C++ – Complete Guide

//1. Returning a simple vector
vector<int> createVector() {
    vector<int> v = {1, 2, 3, 4, 5};
    return v; // return the vector
}

//2. Returning a dynamically filled vector
vector<int> getEvenNumbers(int n) {
    vector<int> evens;
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) evens.push_back(i);
    }
    return evens;
}

//3. Returning a 2D vector (vector of vectors)
vector<vector<int>> createMatrix(int n, int m) {
    vector<vector<int>> matrix(n, vector<int>(m, 0)); // n x m matrix of zeros
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            matrix[i][j] = i + j; // fill some values
    return matrix;
}

//4. Returning a vector of pairs
vector<pair<int,int>> createPairs(int n) {
    vector<pair<int,int>> vp;
    for(int i = 1; i <= n; i++)
        vp.push_back({i, i*2});
    return vp;
}

// 5. Best Practices
// - Returning by value is fine in modern C++ (move semantics are efficient)
// - For large vectors, avoid unnecessary copies inside the function
// - Use const reference when only reading a vector inside a function
// - Use emplace_back() for objects to construct in place (faster than push_back)
// - For 2D vectors, always initialize rows and columns before

// 🔹 Common STL Functions from <algorithm>:
// |  |  | 
// | reverse() |  | 
// | sort() |  | 
// | max_element() |  | 
// | min_element() |  | 
// | find() |  | 
// | count() |  | 
// | binary_search() |  | 



#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

void demoVectorAlgorithms() {
    vector<int> v = {5, 2, 9, 1, 5, 6};

    // 🔄 Reverse elements
    reverse(v.begin(), v.end());

    // 🔢 Sort ascending
    sort(v.begin(), v.end());

    // 🔢 Sort descending
    sort(v.rbegin(), v.rend()); // or use custom comparator

    // 🔍 Find max and min
    int maxVal = *max_element(v.begin(), v.end());
    int minVal = *min_element(v.begin(), v.end());

    // 🔎 Search for element (must be sorted)
    bool found = binary_search(v.begin(), v.end(), 5);

    // 🔎 Find iterator to element
    auto it = find(v.begin(), v.end(), 5); // returns v.end() if not found

    // 🔢 Count occurrences
    int count5 = count(v.begin(), v.end(), 5);

    // 🔁 Rotate vector left by 2
    rotate(v.begin(), v.begin() + 2, v.end()); // [3rd arg = end of range]

    // 🔁 Next permutation
    next_permutation(v.begin(), v.end());

    // 🔁 Previous permutation
    prev_permutation(v.begin(), v.end());

    // 🧹 Remove consecutive duplicates (after sort)
    v.erase(unique(v.begin(), v.end()), v.end());

    // 🔄 Stable sort (preserves relative order)
    stable_sort(v.begin(), v.end());

    // 🔄 Partial sort (first k elements sorted)
    int k = 3;
    partial_sort(v.begin(), v.begin() + k, v.end());

    // 🔍 Check if sorted
    bool isSorted = is_sorted(v.begin(), v.end());

    // 🔍 Check if all elements satisfy condition
    bool allEven = all_of(v.begin(), v.end(), [](int x){ return x % 2 == 0; });

    // 🔍 Check if any element satisfies condition
    bool anyEven = any_of(v.begin(), v.end(), [](int x){ return x % 2 == 0; });

    // 🔍 Check if no element satisfies condition
    bool noneEven = none_of(v.begin(), v.end(), [](int x){ return x % 2 == 0; });
}

