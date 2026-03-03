# include <iostream>
# include <vector>
# include <algorithm>
using namespace std ;
int main(){
    vector <int> v = {1,2,3,4,5} ;
    v.push_back(6);
    v.push_back(7);
    cout << v.capacity() ;
    cout << endl;
    cout << v.size();
    v.pop_back();
    
    v.pop_back();
    for (int i= 0; i<v.size(); i++){
        cout << v[i]<< endl ;
    }
    // for (int x : v){          //   error   ///
    //     cout << v.at(x);    // - You're treating x as an index, but it's actually an element value.
    // }                        //- If v = {1, 2, 3, 4, 5}, then v.at(5) is invalid (index out of bounds).

    // for (int x: v){                 // error  / //
    //     v.insert (v.begin() + x , 4 );  /// same here also bcz x is value and here we want index.  
    // } 
     
    // // so to remove error use for loop normally : for (int i = 0; i<v.size();i++)
    v.clear() ;
    if (v.empty() ){
        cout << " it is empty " ;
    }
}


// storing and accessing second term from vector 
class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        int m = mat.size();
        int n = mat[0].size();
        vector<pair<int,int>> v;   // store {count, row_index}
        vector<int> v1;
        int count;

        for (int i = 0; i < m; i++) {
            count = 0;
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) count++;
            }
            v.push_back({count, i});
        }

        sort(v.begin(), v.end());  // sorts by count, then index

        for (int i = 0; i < k; i++) {
            v1.push_back(v[i].second);  // push row index
        }
        return v1;
    }
};



// Boyer–Moore Majority Vote Algorithm 
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        int power = 1 ;
        int ele = nums[0];
        for (int i = 1 ; i < n ; i++){

            if (nums[i]==ele) power++;
            else power--;
            if (power==0){
                ele = nums[i];
                power = 1 ;
            }
        }
        return ele;
    }
};
