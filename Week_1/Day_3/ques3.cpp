class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size() - 1;
        int maxArea = 0;
        int area =0;
        while (i < j) {
            area = (j - i) * min(height[i], height[j]);
            maxArea = max(maxArea, area);

            if (height[i] > height[j]) {
                j--;
            } else {
                i++;
            }
        }

        return maxArea;
    }
};