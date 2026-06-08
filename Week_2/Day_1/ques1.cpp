class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        int count1 = 0 ;
        int count2 = 0 ;
        for (int i = 0 ; i < s.length() ; i++){
            count1+=s[i]-'a';
            count2+=t[i]-'a';
        }
        if (count1==count2) return true ;
        return false ;
    }
};