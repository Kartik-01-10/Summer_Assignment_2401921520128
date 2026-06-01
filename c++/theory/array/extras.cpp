// // Check if sum or higher exists in the array
//         unordered_set<int> seen(nums.begin(), nums.end());
//         while (seen.count(sum)) {
//             sum++;
//         }


// vector<int> quad = {nums[i], nums[j], nums[k], nums[l]};



// if we want to del specific element form array we can use erase func, we can't use  pop
// func bcz it can only del ele from last only.
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std ;
int main(){
    vector <int> v = {1,2,3,4};
    int pos = 2 ; //index of ele to del (here 3)
    v.erase(v.begin() + pos);
    for (int x : v){
        cout <<x<<" ";
    }
}




// this is how i can create func in leetcode 
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> result = {-1, -1};
        int left = binarySearch(nums, target, true);
        int right = binarySearch(nums, target, false);
        result[0] = left;
        result[1] = right;
        return result;        
    }

    int binarySearch(vector<int>& nums, int target, bool isSearchingLeft) {
        int left = 0;
        int right = nums.size() - 1;
        int idx = -1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                idx = mid;
                if (isSearchingLeft) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }
        
        return idx;
    }    
};




// in such type of ques we return ans in this way 
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if (m == 0 && n != 0) {
            for (int i = 0; i < n; i++) {
                nums1[i] = nums2[i];
            }
            return;
        }

        if (m != 0 && n == 0) return;

        nums1.resize(m + n); // Ensure nums1 has enough space

        int a = 0;
        int b = 0;

        while (a < m + b && b < n) {
            if (nums1[a] > nums2[b]) {
                // Shift elements to the right to make space
                for (int i = m + b; i > a; i--) {
                    nums1[i] = nums1[i - 1];
                }
                nums1[a] = nums2[b];
                b++;
            }
            a++;
        }

        // If nums2 still has remaining elements, append them
        while (b < n) {
            nums1[m + b] = nums2[b];
            b++;
        }
    }
};
// bcz func is void and here if we use return variable_name or cout then we get error 



// we can't we climints func in this way
// class Solution {
// public:
//     int thirdMax(vector<int>& nums) {
//         sort(nums.begin(), nums.end());
//         reverse(nums.begin(), nums.end());
//         // int a=INT_MIN; 
//         // int b=INT_MIN;
//         // int c=INT_MIN; 
//         int n; 
//         a = nums[0];
//         n= nums.size();
        
//         for (int i = 1 ; i<n; i++){
//             if (nums[i]!= a){
//                 b = nums[i];
//             }
//             else if (b!=INT_MIN && nums[i]!=b){
//                 c= nums[i];
//                 break;
//             }
//         }
//         if (b = INT_MIN) return a;
//         else if (c= INT_MIN) return b;
//         else return c;
//     }
// };



// if i want to sort ele in array by its absolute then we can use 
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> arr = { -5, 3, -2, 0, 4 };

    // Sort using a custom comparator based on absolute value
    sort(arr.begin(), arr.end(), [](int a, int b) {
        return abs(a) < abs(b);
    });

    // Print the sorted array
    for (int num : arr) {
        cout << num << " ";
    }

    return 0;
}
// here what is custom comparator : a function or lambda expression that defines a specific order for
// sorting elements
// how to use this : we pass this comparator as the third argument to the sort function
// give different way to use lambda func in c++ : https://www.geeksforgeeks.org/lambda-expressions-in-cpp/




class Solution {
public:
    string intToRoman(int num) {
        vector<pair<int, string>> roman = {
            {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
            {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"},
            {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
        };
        string s = "";
        while (num > 0) {
            for (auto x : roman) {
                if (x.first <= num) {   
                    int rem = num / x.first;
                    for (int i = 0; i < rem; i++) {
                        s += x.second;
                    }
                    num %= x.first;
                    break;   
                }
            }
        }
        return s;
    }
};