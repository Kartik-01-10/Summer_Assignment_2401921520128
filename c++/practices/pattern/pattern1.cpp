// 1 2 3 4 5 6 7 
// 1 2 3   5 6 7 
// 1 2       6 7
// 1           7
# include <iostream>
using namespace std;
int main(){
    int n ; cin >>n;
    for (int i = 1 ;i<= n ;i++){
        int a = 1;
        if (i!=1){
            for (int j=0; j<n-i+1 ; j++){
                cout << a <<" ";
                a++;
            }
        }
        else {
            while(a<=2*n-1){
                cout<<a<<" ";
                a++;
            }
        }
        
        if (i>1){
            for (int j = 0; j<2*(i-1)-1;j++){
                cout <<" ";
            }
            int b = n+i-1;
            for (int j = 0 ; j < n-i+1 ; j++){
                cout <<b<<" ";
                b++;
            }
        }
        cout <<endl;

    }
}
