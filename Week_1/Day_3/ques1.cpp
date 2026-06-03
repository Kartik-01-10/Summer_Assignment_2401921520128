class Solution {
public:
    void swap(int *a, int *b) {
        int temp = *a;
        *a = *b;
        *b = temp;
    }

    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int lastNonZero = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                swap(&nums[i], &nums[lastNonZero]);
                lastNonZero++;
            }
        }
    }
};