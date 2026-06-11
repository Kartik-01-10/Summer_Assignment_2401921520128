class Solution {
public:
    string reverseWords(string s) {
        int l = s.length();
        string x = "";
        int a = 0; 

        for (int i = 0; i < l; i++) {
            if (s[i] == ' ') {
                for (int j = i - 1; j >= a; j--) {
                    x += s[j];
                }
                x += ' ';
                a = i + 1; 
            }
        }
        for (int j = l - 1; j >= a; j--) {
            x += s[j];
        }

        return x;
    }
};
