class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int n = s.length();

        for (int len = 1; len <= n / 2; len++) {
            if (n % len != 0) continue;

            string x = s.substr(0, len);
            int b = len;
            bool match = true;

            while (b < n) {
                for (int i = 0; i < len; i++) {
                    if (s[b] != x[i]) {
                        match = false;
                        break;
                    }
                    b++;
                }
                if (!match) break;
            }

            if (match && b == n) return true;
        }

        return false;
    }
};