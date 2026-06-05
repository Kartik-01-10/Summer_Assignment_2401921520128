class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        sort(strs.begin(),strs.end());
        string s = strs[0];
        string t = strs[n-1];
        int count =0 ;
        for (int i = 0 ;i < min(s.length(), t.length()); i++){
            if (s[i]==t[i]){
                count++;
            }
            else break;
        } s = "";
        for (int i = 0 ;i<count ; i++){
            s += t[i];
        }
        return s ;
    }
};