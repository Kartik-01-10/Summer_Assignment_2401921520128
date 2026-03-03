// use of count function in string 
#include <iostream>
#include <string>
using namespace std;
int main() {
    string str = "hello world";
    char ch = 'o';
    int count = 0;

    for (char c : str) {
        if (c == ch) {
            count++;
        }
    }

    cout << "The character '" << ch << "' occurs " << count << " times in the string '" << str << "'." << endl;

    return 0;
}
// 2 method 
#include <algorithm>
int main(){
    string str = "hello world";
    char ch = 'o';
    int c1 = count(str.begin(), str.end(), ch);
    int c2 = count(str.begin(), str.end(), '1');
    cout << c2 << endl;  
    cout << c1 << endl;
    return 0;
}





// how to count occurrences of a substring in a string in C++17
#include <iostream>
#include <string>
using namespace std;

int main() {
    string str = "ababcabc";
    string subStr = "abc";
    int count = 0;
    size_t pos = 0;

    while ((pos = str.find(subStr, pos)) != string::npos) {
        count++;
        pos += subStr.length(); // Move past the last found substring
    }

    cout << "The substring '" << subStr << "' occurs " << count << " times in the string '" << str << "'." << endl;

    return 0;
}


int a = 2;
string s = "banana";
char ch = s[a]; // s[2] = 'n'
string x(1, ch); // x = "n"
// this is the correct way to initialise new string x with any ele of different string 
// syntax : string(size_t count, char ch)



//if i have binary no "0110203"
// and i want to increase length to 32 bit then we use pading :

// string ans = "0110203";
// int len = ans.length();        // current length of binary string
// int pad = 32 - len;            // how many zeros we need
// ans = string(pad, '0') + ans;  // prepend that many '0's
//or 
//ans = string(32 - ans.length(), '0') + ans;

//    string(28, '0') → "0000000000000000000000000000"