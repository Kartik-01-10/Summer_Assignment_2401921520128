#include <iostream>
#include <climits>
using namespace std;
int main(){
    int a=INT_MIN;
    int b=INT_MIN;
    int arr[]={13,18,19,21};
    for (int i=0;i<sizeof(arr)/sizeof(arr[0]);i++){
        if (arr[i]>a){
            a=arr[i];
        }
    }
    for (int i=0;i<sizeof(arr)/sizeof(arr[0]);i++){
        if (arr[i]!=a && b<arr[i]){
            b=arr[i];
        }
    }
    cout <<"second highest no. is :"<<b;
}