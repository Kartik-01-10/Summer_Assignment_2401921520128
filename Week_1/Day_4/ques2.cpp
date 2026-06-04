class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int total = mat.size() * mat[0].size();
        if (total != r * c) return mat;  

        vector<vector<int>> matrix(r, vector<int>(c, 0));
        vector<int> v;

        for (int i = 0 ; i < mat.size(); i++) {
            for (int j = 0 ; j < mat[0].size(); j++) {
                v.push_back(mat[i][j]);
            }
        }

        int x;
        for (int i = r - 1 ; i >= 0; i--) {
            for (int j = c - 1 ; j >= 0; j--) {
                x = v.back(); v.pop_back();
                matrix[i][j] = x;
            }
        }

        return matrix;
    }
};