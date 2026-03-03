#include<iostream>
#include<unordered_set>
#include<unordered_map>
#include<vector>
#include<algorithm>
#include<string>
#include<cmath>
#include<climits>
using namespace std;

// LC: 1207 unique no of occurances

class Solution{
    
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> freqMap;
        for (int num : arr) {
            freqMap[num]++;
        }

        unordered_set<int> occurrences;
        for (auto x : freqMap) {
            int freq = x.second;
            if (occurrences.find(freq) != occurrences.end()) {
                return false;
            }
            occurrences.insert(freq);
        }
        return true;
    }
};

int main(){
};