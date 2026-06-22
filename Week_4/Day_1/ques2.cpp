
class Solution {
public:
    void help(TreeNode* root){
        if (root==nullptr) return ;
        TreeNode* temp = root->left;
        root->left=root->right;
        root->right = temp;
        help(root->left);
        help(root->right);
    }
    TreeNode* invertTree(TreeNode* root) {
        help(root);
        return root;
    }
};