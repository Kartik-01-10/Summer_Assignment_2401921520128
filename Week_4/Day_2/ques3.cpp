class Solution {
public:
    void help(vector<vector<int>>& ans, int no , TreeNode* root){
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int i = q.size();
            vector<int> v;
            for(int j = 0 ; j < i ; j++){
                TreeNode* temp = q.front();
                q.pop();
                v.push_back(temp->val); 

                if (temp->left) q.push(temp->left);
                if (temp->right) q.push(temp->right);
            }
            if (no % 2 == 1) reverse(v.begin(), v.end()); 
            ans.push_back(v); 
            no++;
        }
    }

    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if (!root) return ans;
        help(ans, 0, root);
        return ans;
    }
};
