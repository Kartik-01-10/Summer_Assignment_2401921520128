class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int> mp ;
        for (char x : magazine){
            mp[x]++;
        }
        for (char x : ransomNote){
            if (mp.find(x)!=mp.end()){
                mp[x]--;
                if (mp[x]==0) mp.erase(x);
            }
            else return false;
        }
        return true;
    }
};