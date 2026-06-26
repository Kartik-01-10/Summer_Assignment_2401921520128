class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) return "N,";
        string s = "";
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            if (node) {
                s += to_string(node->val) + ",";
                q.push(node->left);
                q.push(node->right);
            } else {
                s += "N,";
            }
        }
        return s;
    }
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data.empty()) return nullptr;
        stringstream ss(data);
        string val;
        getline(ss, val, ',');
        if (val == "N") return nullptr;
        TreeNode* root = new TreeNode(stoi(val));
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            if (getline(ss, val, ',')) {
                if (val != "N") {
                    node->left = new TreeNode(stoi(val));
                    q.push(node->left);
                }
            }
            if (getline(ss, val, ',')) {
                if (val != "N") {
                    node->right = new TreeNode(stoi(val));
                    q.push(node->right);
                }
            }
        }
        return root;
    }
};
