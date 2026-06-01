#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        sort(nums.begin(),nums.end());
        int a = 0 ;
        int b = n-1;
        while(a<b){
            if (nums[a]+nums[b]==target) return {a,b};
            else if (nums[a]+nums[b]>target) b--;
            else if (nums[a]+nums[b]<target) a++;
        }
        return {};
    }
};
