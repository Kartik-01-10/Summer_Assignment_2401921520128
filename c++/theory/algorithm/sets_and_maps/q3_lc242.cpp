#include<iostream>
#include<unordered_set>
#include<unordered_map>
#include<vector>
#include<algorithm>
#include<string>
#include<cmath>
#include<climits>
using namespace std;

// LC 242 valid anagram

class Solution1{ // in this we have used 2 unordered map
    public:
    bool isAnagram(string s, string t){
        if (s.length() != t.length()) return false;
        unordered_map<char,int> m;  // for s
        unordered_map<char,int> n;  // for t
        for (int i = 0; i < s.length(); i++){
            m[s[i]]++;
            n[t[i]]++;
        }
        for (auto x : m){
            char ch1 = x.first;
            int freq1 = x.second;
            if (m[ch1] != n[ch1]) {
                int freq2 = n[ch1];
                if (freq1 != freq2) return false;
            }
            else return false;
        }
        return true;
    }
        
};
class Solution2{
    public:
    bool isAnagram(string s, string t){
        if (s.length() != t.length()) return false;
        unordered_map<char,int> m;  
        for (int i = 0; i < s.length(); i++){
            m[s[i]]++;
        }
        for (int i = 0; i < t.length(); i++){
            char ch = t[i];
            if (m.find(ch) == m.end()) return false; // if not exist
            else{
                m[ch]--;
                if (m[ch] == 0) m.erase(ch);
            }
        }
        return m.size() == 0;
    }

};

int main(){

}