class Solution {
public:
    string decodeString(string s) {
        stack<char> st;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == ']') {
                string temp;
                while (!st.empty() && st.top() != '[') {
                    temp.push_back(st.top());
                    st.pop();
                }
                st.pop();
                string num;
                while (!st.empty() && isdigit(st.top())) {
                    num.push_back(st.top());
                    st.pop();
                }
                reverse(temp.begin(), temp.end());
                reverse(num.begin(), num.end());
                int n = stoi(num);
                int size = temp.size();
                while (n--) {
                    for (int i = 0; i < size; i++) {
                        st.push(temp[i]);
                    }
                }
            } else {
                st.push(s[i]);
            }
        }
        string ans;
        while (!st.empty()) {
            ans.push_back(st.top());
            st.pop();
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};