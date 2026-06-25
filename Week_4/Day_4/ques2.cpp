class Solution {
public:
    int level(TreeNode* root){
        if(root==nullptr) return 0;
        return 1+max(level(root->left),level(root->right));
    }
    void helpher(TreeNode* root,int &maxdia){
        if(root==nullptr) return ;
        int dia = level(root->left)+level(root->right);
        maxdia = max(maxdia,dia);
        helpher(root->left,maxdia);
        helpher(root->right,maxdia);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int maxdia = 0 ;
        helpher(root,maxdia);
        return maxdia;
    }
};