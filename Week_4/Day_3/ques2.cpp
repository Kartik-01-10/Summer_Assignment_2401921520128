class Solution {
public:
    void inorder(TreeNode* root,vector<int>& ans){
        if (root==nullptr) return ;
        inorder(root->left,ans);
        ans.push_back(root->val);
        inorder(root->right,ans);
    }
    bool isValidBST(TreeNode* root) {
        vector<int> ans;
        inorder(root,ans);
        for (int i = 1 ; i < ans.size() ; i++){
            if (ans[i]<=ans[i-1]) return false;
        }
        return true;
    }
};