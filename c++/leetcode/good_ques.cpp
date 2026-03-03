#include<iostream>
#include<unordered_set>
#include<unordered_map>
#include<vector>
#include<algorithm>
#include<string>
#include<cmath>
#include<climits>

using namespace std;

//   1.. Plus One

// You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

// Increment the large integer by one and return the resulting array of digits.

 

// Example 1:

// Input: digits = [1,2,3]
// Output: [1,2,4]
// Explanation: The array represents the integer 123.
// Incrementing by one gives 123 + 1 = 124.
// Thus, the result should be [1,2,4].

vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();

        for (int i = n - 1 ; i >= 0 ; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                break;
            } 
            else {
                digits[i] = 0;
                if (i == 0) {
                    digits.insert(digits.begin(), 1);
                }
            }
        }

        return digits;
    };



// LC 1721 :   here we are swapping value only...
// class Solution {
// public:
//     ListNode* swapNodes(ListNode* head, int k) {
//         ListNode* temp = head;
//         ListNode* a = nullptr;
//         ListNode* b = nullptr;

//         int n = 0;

//         // count length and find kth from start
//         while (temp) {
//             n++;
//             if (n == k) a = temp;
//             temp = temp->next;
//         }

//         // find kth from end (n-k+1 from start)
//         temp = head;
//         for (int i = 1; i <= n - k + 1; i++) {
//             temp = temp->next;
//         }
//         b = temp;

//         // swap values this is how we can swap val only 
//         int val = a->val;
//         a->val = b->val;
//         b->val = val;

//         return head;
//     }
// };

// LC 26 remove duplicate from sorted list
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;

        int i = 0; // pointer for the last unique element
        for (int j = 1; j < nums.size(); j++) {
            if (nums[j] != nums[i]) { 
                i++; 
                nums[i] = nums[j]; 
            }
        }
        return i + 1; // length of unique elements
    }
};


// LC 1290   Convert Binary Number in a Linked List to Integer
// class Solution {
// public:
//     int getDecimalValue(ListNode* head) {
//         int ans = 0;
//         while (head) {
//             ans = ans * 2 + head->val;  // shift left and add bit
//             head = head->next;
//         }
//         return ans;
//     }
// };
 
// LC 70 climbing stair ... in this we can use recursive method which requires more space 
//so will doing stair ques we observe that the ans is like fabionic series 
class Solution {
public:
    int climbStairs(int n) {
    if (n <= 2) return n;
    int a = 1, b = 2;
    for (int i = 3; i <= n; i++) {
        int c = a + b;
        a = b;
        b = c;
    }
    return b;
}
};




// LC 153. Find Minimum in Rotated Sorted Array
// using binary search 
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] <= nums[right]) {
                right = mid; // **** imp *****
            } else {
                left = mid + 1;
            }
        }

        return nums[left];        
    }
};
// in next lc 154 : same ques but now, we have duplicate values also 
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] < nums[right]) {
                right = mid; // **** imp *****
            } else if(nums[mid] > nums[right]) {
                left = mid + 1;
            } else // nums[mid] = nums[right]
            right--;
        }

        return nums[left];        
    }
};



// LC 75 sort color   
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int low = 0 ;
        int mid = 0 ;
        int high = n-1;
        while (mid<=high){
            if (nums[mid] == 0) swap(nums[mid++], nums[low++]);
            else if (nums[mid] == 1) mid++;
            else swap(nums[mid], nums[high--]);
        }
    }
};