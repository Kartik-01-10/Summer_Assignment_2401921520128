class Solution {
public:
    int firstUniqChar(string s) {
        
        int n = s.length();
        vector<int> v(n,0);

        for (int i = 0 ; i < n; i++){
            if (v[i]==1) continue;
            bool flag = true;
            for (int j = i + 1 ; j < n ; j++){
                if (s[i]==s[j]) {
                    flag = false;
                    v[j] = 1 ;
                }
            }
            if (flag) return i ;
        }
        return -1 ;
    }
};