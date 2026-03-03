// this is human readable but prefix and postfix not....
#include<iostream>
#include<stack>
using namespace std ;
int prio(char ch){
    if (ch == '+' || ch == '-'){
        return 1;
    }
    else if (ch == '*' || ch == '/'){
        return 2;
    }
    else{
        return 0;
    }
}
int solve(int v1, int v2, char ch){
    if (ch == '+'){
        return v1+v2;
    }
    else if (ch == '-'){
        return v1-v2;
    }
    else if (ch == '*'){
        return v1*v2;
    }
    else{
        return v1/v2;
    }
}
int main(){
    string s = "(2+6)*4/8-3";
    stack<char> op;
    stack<int> val;
    for (int i = 0; i < s.length(); i++){
        // check if s[i] is a digit (0-9)
        if (s[i]>=48 && s[i]<=57){  //digit
            val.push(s[i]-48);
        }
        else{ // s[i] it is -> */+- ()
            if (op.size()==0 ){
                op.push(s[i]);
            }
            else if (s[i] == '('){
                op.push(s[i]);
            }
            else if (op.top() == '(' ){
                op.push(s[i]);
            }
            else if (s[i] == ')'){
                while(op.top()!='('){
                    char ch = op.top();
                    op.pop();
                    int v2 = val.top();
                    val.pop();
                    int v1 = val.top();
                    val.pop();
                    int ans = solve(v1, v2, ch);
                    val.push(ans);
                }
                op.pop();
            }
            else if( prio(s[i])>prio(op.top())){
                op.push(s[i]);
            }
            
            else{ 
                while(op.size()>0 && prio(s[i])<=prio(op.top())){
                    char ch = op.top();
                    op.pop();
                    int v2 = val.top();
                    val.pop();
                    int v1 = val.top();
                    val.pop();
                    int ans = solve(v1, v2, ch);
                    val.push(ans);
                    
                }
                op.push(s[i]);
            }
        
        }
    }
    // the operator stack can have values
    // so make it empty
    while(op.size()>0){
        char ch = op.top();
        op.pop();
        int v2 = val.top();
        val.pop();
        int v1 = val.top();
        val.pop();
        int ans = solve(v1, v2, ch);
        val.push(ans);
    }
    cout << val.top()<<endl;
    cout <<(2+6)*4/8-3;
    
}