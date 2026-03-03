#include <iostream>
#include <string>
using namespace std;
// syntax   string.substr(start_index, length);
int main() {
    string text = "Hello, World!";
    string slice = text.substr(7, 5);  // "World"
    cout << slice << endl;
    return 0;
}



#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "dog:cat";
    int pos = s.find(":");

    string before = s.substr(0, pos);       // "dog"
    string after = s.substr(pos + 1);       // "cat"

    cout << "Before: " << before << endl;
    cout << "After: " << after << endl;
    return 0;
}



#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "abc";
    int n = s.length();

    for (int i = 0; i < n; i++) {
        for (int len = 1; len <= n - i; len++) {
            cout << s.substr(i, len) << endl;
        }
    }
    return 0;
}
// output:
// a
// ab
// abc
// b
// bc
// c


// how we can find multiple occurance using find func
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "geeksforgeeks";
    string sub = "geeks";
    size_t pos = s.find(sub);
    
    while (pos != string::npos) {
        cout << "Found at index: " << pos << endl;
        pos = s.find(sub, pos + 1);  // Search from next position
    }
    return 0;
}

// 🧠 Summary Table
// | s.find("apple") | Finds first "apple"

// | s.find("apple", pos+1) | Finds next "apple" after position

// | string::npos | Special value meaning “not found” | 





// how to split the given sentence 
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int main() {
    string str = "apple,banana,mango";
    stringstream ss(str);
    string token;
    char delimiter = ',';
    vector<string> result;

    while (getline(ss, token, delimiter)) {
        result.push_back(token);
    }

    for (const string& word : result)
        cout << word << endl;

    return 0;
}


#include <iostream>
#include <vector>
using namespace std;

vector<string> split(const string& str, const string& delimiter) {
    vector<string> tokens;
    size_t start = 0, end;

    while ((end = str.find(delimiter, start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));
        start = end + delimiter.length();
    }
    tokens.push_back(str.substr(start));
    return tokens;
}

int main() {
    string s = "scott>=tiger>=mushroom";
    vector<string> parts = split(s, ">=");

    for (const string& part : parts)
        cout << part << endl;

    return 0;
}
//string s = "Hello     world";
//{"Hello", "", "", "", "", "world"}




vector<string> parts = {"Hello", "world"};
// - parts.back() → gives you the last element of the vector, which is "world" in this case.
// - .size() → gives you the length of that string.
int lengthOfLastWord(string s) {
    vector<string> parts = split(s, " ");
    if (parts.empty()) return 0;
    return parts.back().size();  // Length of last word
}




// how to remove extra spaces from string 
//if (!token.empty()) tokens.push_back(token);


// Absolutely! Let's enhance your split() function so it:
// - ✅ Removes leading/trailing whitespace from each token
// - ✅ Skips empty tokens caused by consecutive delimiters
// - ✅ Works cleanly with any string delimiter
// Here’s the updated version:
#include <vector>
#include <string>
#include <cctype>
using namespace std;

// Helper to trim whitespace from both ends of a string
string trim(const string& s) {
    size_t start = 0;
    while (start < s.size() && isspace(s[start])) start++;

    size_t end = s.size();
    while (end > start && isspace(s[end - 1])) end--;

    return s.substr(start, end - start);
}

vector<string> split(const string& str, const string& delimiter) {
    vector<string> tokens;
    size_t start = 0, end;

    while ((end = str.find(delimiter, start)) != string::npos) {
        string token = trim(str.substr(start, end - start));
        if (!token.empty()) tokens.push_back(token);
        start = end + delimiter.length();
    }

    string lastToken = trim(str.substr(start));
    if (!lastToken.empty()) tokens.push_back(lastToken);

    return tokens;
}
// string s = "  apple  ,  , banana , mango  ";
//vector<string> result = split(s, ",");
//{"apple", "banana", "mango"}