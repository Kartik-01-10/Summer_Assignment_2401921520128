#include<iostream>
#include<stack>
using namespace std;

string solve(string v1, string v2, char ch) {
    string s = "";
    s.push_back(ch);
    s += v1;
    s += v2;
    return s;
}

int prio(char ch) {
    if (ch == '+' || ch == '-') {
        return 1;
    } else if (ch == '*' || ch == '/') {
        return 2;
    } else {
        return 0;
    }
}

int main() {
    string s = "(2+6)*4/8-3";
    stack<char> op;
    stack<string> val;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] >= '0' && s[i] <= '9') {
            val.push(string(1, s[i]));
        } 
        else {
            if (op.empty()) {
                op.push(s[i]);
            } 
            else if (s[i] == '(') {
                op.push(s[i]);
            } 
            else if (op.top() == '(') {
                op.push(s[i]);
            } 
            else if (s[i] == ')') {
                while (op.top() != '(') {
                    char ch = op.top();
                    op.pop();
                    string v2 = val.top(); val.pop();
                    string v1 = val.top(); val.pop();
                    string ans = solve(v1, v2, ch);
                    val.push(ans);
                }
                op.pop(); // remove '('
            } 
            else if (prio(s[i]) > prio(op.top())) {
                op.push(s[i]);
            } 
            else {
                while (!op.empty() && prio(s[i]) <= prio(op.top())) {
                    char ch = op.top();
                    op.pop();
                    string v2 = val.top(); val.pop();
                    string v1 = val.top(); val.pop();
                    string ans = solve(v1, v2, ch);
                    val.push(ans);
                }
                op.push(s[i]);
            }
        }
    }

    while (!op.empty()) {
        char ch = op.top();
        op.pop();
        string v2 = val.top(); val.pop();
        string v1 = val.top(); val.pop();
        string ans = solve(v1, v2, ch);
        val.push(ans);
    }

    cout << val.top() << endl;
}