// Complete Guide to 2D Arrays and 2D Vectors in C++

// 1. What is a 2D Array?
// - A 2D array is a matrix-like structure with rows and columns.
// - In C++, you can use built-in arrays or STL vectors for 2D arrays.

// 2. Creating a 2D Array (built-in)
#include <iostream>
using namespace std;

int main() {
    int arr[3][4]; // 3 rows, 4 columns
    // Initializing
    int arr2[2][3] = {{1,2,3},{4,5,6}};
    // Accessing
    cout << arr2[1][2] << endl; // prints 6
}

// 3. Creating a 2D Vector (dynamic size)
#include <vector>
#include <iostream>
using namespace std;

int main() {
    // Create a 3x4 matrix filled with zeros
    vector<vector<int>> matrix(3, vector<int>(4, 0));
    // Assign values
    matrix[0][1] = 5;
    matrix[2][3] = 7;
    // Print matrix
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

// 4. Jagged Array (rows of different sizes)
#include <vector>
#include <iostream>
using namespace std;

int main() {
    vector<vector<int>> jagged(3);
    jagged[0] = {1, 2};
    jagged[1] = {3, 4, 5};
    jagged[2] = {6};
    // Print jagged array
    for (int i = 0; i < jagged.size(); i++) {
        for (int val : jagged[i]) cout << val << " ";
        cout << endl;
    }
}

// 5. Passing 2D Vector to Function
void printMatrix(const vector<vector<int>>& mat) {
    for (const auto& row : mat) {
        for (int val : row) cout << val << " ";
        cout << endl;
    }
}

// 6. Returning a 2D Vector from Function
vector<vector<int>> createMatrix(int n, int m) {
    vector<vector<int>> mat(n, vector<int>(m, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            mat[i][j] = i + j;
    return mat;
}

int main() {
    vector<vector<int>> mat = createMatrix(3, 4);
    printMatrix(mat);
}

// 7. Useful Functions and Operations
// - matrix.size()         : Number of rows
// - matrix[i].size()      : Number of columns in row i
// - matrix.push_back(row) : Add a new row
// - matrix.clear()        : Remove all rows
// - matrix.resize(n)      : Change number of rows
// - matrix[i].resize(m)   : Change number of columns in row i

// 8. Iterating Over 2D Vector
// for (const auto& row : matrix) {
//     for (int val : row) {
//         // use val
//     }
// }

// 9. Summary Table

/*
| Concept         | Syntax/Function                        | Description                        |
|-----------------|----------------------------------------|------------------------------------|
| Create 2D array | int arr[3][4];                         | Built-in, fixed size               |
| Create 2D vector| vector<vector<int>> mat(n,vector<int>(m,0)); | Dynamic size, STL                 |
| Access element  | arr[i][j], mat[i][j]                   | Get/set value                      |
| Pass to func    | void func(const vector<vector<int>>&);  | Use const reference for safety     |
| Return from func| vector<vector<int>> func(...)           | Return by value                    |
| Resize          | mat.resize(n); mat[i].resize(m);        | Change size                        |
| Add row         | mat.push_back(row);                     | Add new row                        |
| Clear           | mat.clear();                            | Remove all rows                    |
*/

//
// Key Points:
// - Use vectors for dynamic size and flexibility.
// - Use const reference for passing to functions (no copy, read-only).
// - Returning vectors is safe and efficient in modern C++.
// - Jagged arrays allow rows of different lengths.
// - STL functions (resize, push_back, clear)


// 🧠 What does   -->  vector<pair<int, int>> zeroPos; mean?
// This line declares a vector named zeroPos that stores pairs of integers. Here's what each part means:
// - vector<...>: A dynamic array from the C++ Standard Library.
// - pair<int, int>: A container that holds two values—both integers in this case.
// - zeroPos: The name of the vector.
// 💡 What is it used for?
// In your code, it's used to store the positions (row, column) of all elements in the matrix that are equal to 0.
// example 
// 1 2 3
// 4 0 6
// 7 8 9    then zeropos will contain { {1, 1} }  but by using this code 
    // Store positions of zero elements
    // vector<pair<int, int>> zeroPos;
    // for (int i = 0; i < row; i++) {
    //     for (int j = 0; j < cols; j++) {
    //         if (matrix[i][j] == 0) {
    //             zeroPos.push_back({i, j});
    //         }
    //     }
    // }

