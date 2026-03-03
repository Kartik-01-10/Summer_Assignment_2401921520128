#include <iostream>
#include <vector>
#include <algorithm>
using namespace std ;
int main(){
    vector <int> v= {1,2,3,3,2,1,4};
    for (int i=0; i<v.size(); i++){
        for (int j=i+1; j<v.size();j++){
            if (v[i]==v[j]){
                v[j]=true;
                continue;

            }
            else if (v[i]==true || v[j]==true){
                continue;
            }
            else {
                if (){}
            }
        }
    }
}