#include<iostream>
#include<unordered_set>
#include<vector>
#include<algorithm>
#include<string>
#include<cmath>
#include<climits>
using namespace std;

// LC 2744 ..  find max. no of string pairs

class Solution1 { // basic approach using array O(n^2)
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        int n = words.size();
        int count = 0;
        for (int i = 0; i < n; i++){
            string rev = words[i];
            reverse(rev.begin(), rev.end());
            for (int j = i+1; j < n; j++){
                if (rev == words[j]){
                    count++;
                }
            }
        }
        return count;
        
    }
};


class Solution2 { // O(n)
    
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        unordered_set<string> s;
        int count = 0;
        for (int i = 0 ; i < words.size(); i++){
            s.insert(words[i]);
        }
        for (int i = 0 ; i < words.size(); i++){ // o(n)
            string rev = words[i];
            reverse(rev.begin(), rev.end());
            if (words[i] == rev) continue;
            if (s.find(rev) != s.end()){ //o(1)
                count++;
                s.erase(rev);
            }
            
        }
        return count;
    }

};

class Solution3 { // in this we take ele one by one reverse it then check isit present in set 
// if not then push it.
//and if ele present then increse count
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        int n = words.size();
        int count = 0 ;
        unordered_set<string> s;
        for (int i = 0; i < n; i++){
            string rev = words[i];
            reverse(rev.begin(), rev.end());
            if (s.find(rev) == s.end()){
                count++;
            }
            else s.insert(rev);
        }
        return count;
    }

};


int main(){

}