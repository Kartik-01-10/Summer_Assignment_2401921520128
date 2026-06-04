class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if (m == 0) return {};
        int n = matrix[0].size();
        vector<int> v;
        int a = 0, b = 0;
        int c = m - 1, d = n - 1;

        while (a <= c && b <= d) {
            // Move right
            for (int j = b; j <= d; j++) {
                v.push_back(matrix[a][j]);
            }
            a++;

            // Move down
            for (int i = a; i <= c; i++) {
                v.push_back(matrix[i][d]);
            }
            d--;

            // Move left
            if (a <= c) {
                for (int j = d; j >= b; j--) {
                    v.push_back(matrix[c][j]);
                }
                c--;
            }

            // Move up
            if (b <= d) {
                for (int i = c; i >= a; i--) {
                    v.push_back(matrix[i][b]);
                }
                b++;
            }
        }

        return v;
    }
};