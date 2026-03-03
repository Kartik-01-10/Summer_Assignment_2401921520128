#include <iostream>
#include <vector>
#include <climits>
using namespace std;
int main(){
    vector<int> nums ;
    int n = nums.size();
        int max = INT_MIN; 
        int a ; int b =0 ;
        for (int i = 0 ; i<n-1 ; i++){
            a=1; 
            for (int j = i+1 ; j< n ; j++){
                if (nums[i]==nums[j]-a){
                    a++;
                }
                else if (nums[i]!=nums[j]-a){
                    continue;
            }
            if (max<a){
                max = a ;
                b = i ;
            }
        }
        int sum = 0 ;
        for (int i = b ; i<= max ; i++){
            sum += nums[i];
        }
        bool flag = false; 
        for (int i = 0 ; i<n ; i++){
            if (sum == nums[i]) flag = true; 
        }
        int c; 
        if (flag == false){
            c =sum;
        }
        return c; 
    }
}