class Solution {
public:
    void rec(string s ,int str, int end , vector<string>& ans ,int n){
        if (s.length()==2*n){
            ans.push_back(s);
            return;
        }
        if (str<n) rec(s+'(',str+1,end,ans,n);
        if (end<str) rec(s+')',str,end+1,ans,n);
    }
    vector<string> generateParenthesis(int n) {
        string s = "";
        int str = 0 , end = 0 ;
        vector<string> ans;
        rec(s,str,end,ans,n);
        return ans ;
    }
};