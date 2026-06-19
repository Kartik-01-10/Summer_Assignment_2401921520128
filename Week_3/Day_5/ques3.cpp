class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ans;
        vector<int> ngi(n);   
        stack<int> st;
        ngi[n-1] = n;
        st.push(n-1);

        for (int i = n-2; i >= 0; i--) {
            while (!st.empty() && nums[st.top()] <= nums[i]) {
                st.pop();
            }
            if (st.empty()) ngi[i] = n;
            else ngi[i] = st.top();
            st.push(i);
        }
        int j = 0;
        for (int i = 0; i <= n - k; i++) {
            if (j < i) j = i;  
            while (ngi[j] < i + k) {
                j = ngi[j];   
            }
            ans.push_back(nums[j]);
        }

        return ans;
    }
};