// if elements is zero then make all hoizontal and vertical ele also zero
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    int row, cols;
    cin >> row >>cols ;
    vector<vector <int>> matrix(row,vector<int>(cols));
    for (int i = 0 ; i<row ; i++){
        for (int j=0 ; j< cols ;j++){
            cin>>matrix[i][j];
        }
    }
    cout << " before oper\n ";
    for (int i = 0 ; i<row ; i++){
        for (int j=0 ; j< cols ;j++){
            cout<<matrix[i][j]<<" ";
        }
        cout << endl;
    }
    
    int a = 0,b= 0 ;
    for (int i =0 ; i < row ; i++){
        for (int j= 0 ; j< cols ;j++){
            if (matrix [i][j]==0){a= i ;
                b =j; 
                break ;
            }
        }
    }


    if (row == cols){
    for (int i = 0 ; i< row ; i++){
        
        matrix[i][b] = 0;
        matrix[a][i] = 0; 
    }}
    else {
        for (int i =0; i<row  ; i++){
            matrix[i][b] = 0 ;
        }
        for (int j= 0 ; j<cols; j++){
            matrix[a][j]= 0 ;
        }
    }
    cout << " after  oper \n ";
    for (int i = 0 ; i<row ; i++){
        for (int j=0 ; j< cols ;j++){
            
            cout<<matrix[i][j]<<" ";

        }
        cout << endl; 
    }


}