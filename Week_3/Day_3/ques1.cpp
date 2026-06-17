class Solution {
public:
    bool isValid(string s) {
        stack<char> v; // Use char stack

        for (char c : s) {
            // Push opening brackets
            if (c == '(' || c == '[' || c == '{') {
                v.push(c);
            } 
            // Handle closing brackets
            else {
                if (v.empty()) return false; // No matching opening bracket

                char top = v.top();
                v.pop();

                if ((c == ')' && top != '(') ||
                    (c == ']' && top != '[') ||
                    (c == '}' && top != '{')) {
                    return false;
                }
            }
        }
        if (v.size()==0) return true;
        return false;
    }
};