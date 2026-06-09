class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int m = s1.length();
        int n = s2.length();
        if (m > n) return false;
        for (int i = 0; i <= n - m; i++) {
            unordered_map<char,int> mp;
            for (int j = i; j < i + m; j++) {
                mp[s2[j]]++;
            }
            for (char x : s1) {
                if (mp.find(x) != mp.end()) {
                    mp[x]--;
                    if (mp[x] == 0) mp.erase(x);
                }
            }
            if (mp.empty()) return true;
        }
        return false;
    }
};