#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();
        double avg = 0;
        for (int i = 0; i < k; i++) {
            avg += nums[i];
        }

        double maxavg = avg;
        for (int i = k; i < n; i++) {
            avg += nums[i] - nums[i - k];  
            maxavg = max(maxavg, avg);
        }

        return maxavg / k;
    }
};
