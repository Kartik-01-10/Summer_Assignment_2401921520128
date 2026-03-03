#include<iostream>
#include<unordered_set>
#include<unordered_map>
#include<vector>
#include<algorithm>
#include<string>
#include<cmath>
#include<climits>
using namespace std;

//LC 1 : two sum
class Solution{
    
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m; // Map to store number and its index
        for (int i = 0; i < nums.size(); i++) {
            int ele = nums[i];
            if (m.find(target - ele) != m.end()) {
                return {m[target - ele], i};
            }
            m[ele] = i;
        }
        return {}; // Should not reach here if a solution always exists
    }
};

int main(){
}