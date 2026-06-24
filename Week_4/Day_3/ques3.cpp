class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == NULL) return NULL;
        int cur = root->val;
        if (p->val < cur && q->val < cur) {
            return lowestCommonAncestor(root->left, p , q);
        }
        if (p->val > cur && q->val > cur) {
            return lowestCommonAncestor(root->right, p, q);
        }

        return root;
    }
};