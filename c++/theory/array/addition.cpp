#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <climits>
using namespace std;
int main(){
     string s = "is2 sentence4 This1 a3";
    int m ;
   // if (s[i] == m + '0') {} // compare digit character

//     What It Means
// - s[i] is a character from the string s.
// - m is an integer (like 1, 2, 3, etc.).
// - '0' is the ASCII character for zero, which has a value of 48.

}



class Solution {
public:
    string triangleType(vector<int>& nums) {
        set<int>s(nums.begin(),nums.end());  // this is creating a set which store unqiue value  
        sort(nums.begin(),nums.end());
        if((nums[0] + nums[1])<=nums[2]) return "none";
        if(s.size() == 1) return "equilateral";
        if(s.size() == 2) return "isosceles";
        return "scalene";
    }
};


// Example 
// vector<int> v = {1, 2, 3, 4};
// int x = v.back();     // x = 4
// v.pop_back();         // v becomes {1, 2, 3}


// how to find first and second smllest no
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int first = INT_MAX, second = INT_MAX;
        
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] <= first) first = nums[i]; // update first if nums[i] is smaller than both
            else if(nums[i] <= second) second = nums[i]; // update second if nums[i] is smaller than second
            else return true; // found a number greater than both first and second

        }
         return false;
        }
};


// if we want to sort the matrix in row wise 
void sortMatrixRowWise(vector<vector<int>>& matrix) {
    int m = matrix.size(); // number of rows
    for (int i = 0; i < m; i++) {
        sort(matrix[i].begin(), matrix[i].end());
    }
}

int main() {
    vector<vector<int>> matrix = {
        {3, 1, 2},
        {9, 5, 6},
        {4, 8, 7}
    };
    sortMatrixRowWise(matrix);
    return 0;
}
// output

    // {1, 2, 3}
    // {5, 6, 9}
    // {4, 7, 8}

// and for col wise 
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void columnWiseSort(vector<vector<int>>& mat) {
    int rows = mat.size(), cols = mat[0].size();
    for (int col = 0; col < cols; ++col) {
        vector<int> temp;
        for (int row = 0; row < rows; ++row)
            temp.push_back(mat[row][col]);
        sort(temp.begin(), temp.end());
        for (int row = 0; row < rows; ++row)
            mat[row][col] = temp[row];
    }
}

int main() {
    vector<vector<int>> mat = {
        {3, 2, 1},
        {9, 8, 7},
        {6, 5, 4}
    };
    columnWiseSort(mat);
    for (auto& row : mat) {
        for (int val : row)
            cout << val << " ";
        cout << endl;
    }
    return 0;
}
// Output:
// 3 2 1
// 6 5 4
// 9 8 7