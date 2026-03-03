// to make uppercase to lowercase 
#include <iostream>
#include <cctype>  // for tolower
using namespace std;

int main() {
    char c = 'G';
    cout << "Lowercase of " << c << " is " << (char)tolower(c) << endl;
    return 0;
}


// Explanation of All Functions in <cctype> and <string> Modules in C++

// <cctype> provides functions to classify and convert characters.
// Each function takes a character (usually as int or char) and returns true/false or the converted character.

// Character Classification Functions
/*
isalnum(c)   // Returns true if c is alphanumeric (letter or digit)
isalpha(c)   // Returns true if c is an alphabet letter (A-Z or a-z)
isdigit(c)   // Returns true if c is a digit (0-9)
islower(c)   // Returns true if c is a lowercase letter (a-z)
isupper(c)   // Returns true if c is an uppercase letter (A-Z)
isspace(c)   // Returns true if c is a whitespace character (space, tab, newline, etc.)
ispunct(c)   // Returns true if c is a punctuation character (e.g., !, ?, ., ,)
isblank(c)   // Returns true if c is a blank character (space or tab)
iscntrl(c)   // Returns true if c is a control character (non-printable, e.g., '\n', '\t')
isprint(c)   // Returns true if c is a printable character (including space)
isgraph(c)   // Returns true if c is a printable character except space
isxdigit(c)  // Returns true if c is a hexadecimal digit (0-9, a-f, A-F)
*/

// Character Conversion Functions
/*
tolower(c)   // Converts c to lowercase if it's uppercase; else returns c unchanged
toupper(c)   // Converts c to uppercase if it's lowercase; else returns c unchanged
*/

// Example Usage:
#include <iostream>
#include <cctype>
#include <string>
using namespace std;

int main() {
    char c = 'A';
    cout << "isalnum: " << isalnum(c) << endl;   // 1 (true)
    cout << "isalpha: " << isalpha(c) << endl;   // 1 (true)
    cout << "isdigit: " << isdigit(c) << endl;   // 0 (false)
    cout << "islower: " << islower(c) << endl;   // 0 (false)
    cout << "isupper: " << isupper(c) << endl;   // 1 (true)
    cout << "isspace: " << isspace(' ') << endl; // 1 (true)
    cout << "ispunct: " << ispunct('!') << endl; // 1 (true)
    cout << "isblank: " << isblank('\t') << endl;// 1 (true)
    cout << "iscntrl: " << iscntrl('\n') << endl;// 1 (true)
    cout << "isprint: " << isprint('A') << endl; // 1 (true)
    cout << "isgraph: " << isgraph('A') << endl; // 1 (true)
    cout << "isxdigit: " << isxdigit('F') << endl;// 1 (true)

    cout << "tolower: " << (char)tolower('G') << endl; // g
    cout << "toupper: " << (char)toupper('g') << endl; // G

    // <string> module provides string class and functions for string manipulation
    string s = "Hello World!";
    cout << "Length: " << s.length() << endl;        // Number of characters
    cout << "Substring: " << s.substr(0, 5) << endl; // "Hello"
    cout << "Find: " << s.find("World") << endl;     // Position of "World"
    cout << "Replace: " << s.replace(6, 5, "C++") << endl; // "Hello C++!"
    cout << "Append: " << s.append("!!!") << endl;   // "Hello C++!!!!"
    cout << "Compare: " << s.compare("Hello") << endl; // Lexicographical comparison
    cout << "Empty: " << s.empty() << endl;          // 0 (false)
    cout << "Front: " << s.front() << endl;          // First character
    cout << "Back: " << s.back() << endl;            // Last character

    return 0;
}

/*
Summary Table  func which is present in cctype lib

| Function      | Purpose/Return Value                        |
|---------------|--------------------------------------------|
| isalnum(c)    | Alphanumeric? (letter or digit)             |
| isalpha(c)    | Alphabet letter?                            |
| isdigit(c)    | Digit?                                      |
| islower(c)    | Lowercase letter?                           |
| isupper(c)    | Uppercase letter?                           |
| isspace(c)    | Whitespace?                                 |
| ispunct(c)    | Punctuation?                                |
| isblank(c)    | Blank (space/tab)?                          |
| iscntrl(c)    | Control character?                          |
| isprint(c)    | Printable character?                        |
| isgraph(c)    | Printable except space?                     |
| isxdigit(c)   | Hexadecimal digit?                          |
| tolower(c)    | Convert to lowercase                        |
| toupper(c)    | Convert to uppercase                        |

| string member functions | Purpose                            |
|------------------------|------------------------------------|
| length()/size()        | Get string length                  |
| substr(pos, len)       | Get substring                      |
| find(str)              | Find substring position            |
| replace(pos, len, str) | Replace part of string             |
| append(str)            | Add to end of string               |
| compare(str)           | Compare strings                    |
| empty()                | Check if string is empty           |
| front()                | First character                    |
| back()                 | Last character                     |
*/


// Iterators:
// begin	Return iterator to beginning (public member function)
// end	Return iterator to end (public member function)
// rbegin	Return reverse iterator to reverse beginning (public member function)
// rend	Return reverse iterator to reverse end (public member function)
// cbegin	Return const_iterator to beginning (public member function)
// cend	Return const_iterator to end (public member function)
// crbegin	Return const_reverse_iterator to reverse beginning (public member function)
// crend	Return const_reverse_iterator to reverse end (public member function)

// Capacity:
// size	Return length of string (public member function)
// length	Return length of string (public member function)
// max_size	Return maximum size of string (public member function)
// resize	Resize string (public member function)
// capacity	Return size of allocated storage (public member function)
// reserve	Request a change in capacity (public member function)
// clear	Clear string (public member function)
// empty	Test if string is empty (public member function)
// shrink_to_fit	Shrink to fit (public member function)

// Element access:
// operator[]	Get character of string (public member function)
// at	Get character in string (public member function)
// back	Access last character (public member function)
// front	Access first character (public member function)

// Modifiers:
// operator+=	Append to string (public member function)
// append	Append to string (public member function)
// push_back	Append character to string (public member function)
// assign	Assign content to string (public member function)
// insert	Insert into string (public member function)
// erase	Erase characters from string (public member function)
// replace	Replace portion of string (public member function)
// swap	Swap string values (public member function)
// pop_back	Delete last character (public member function)

// String operations:
// c_str	Get C string equivalent (public member function)
// data	Get string data (public member function)
// get_allocator	Get allocator (public member function)
// copy	Copy sequence of characters from string (public member function)
// find	Find content in string (public member function)
// rfind	Find last occurrence of content in string (public member function)
// find_first_of	Find character in string (public member function)
// find_last_of	Find character in string from the end (public member function)
// find_first_not_of	Find absence of character in string (public member function)
// find_last_not_of	Find non-matching character in string from the end (public member function)
// substr	Generate substring (public member function)
// compare	Compare strings (public member function)

// Member constants
// npos	Maximum value for size_t (public static member constant)

// Non-member function overloads
// operator+	Concatenate strings (function)
// relational operators	Relational operators for string (function)
// swap	Exchanges the values of two strings (function)
// operator>>	Extract string from stream (function)
// operator<<	Insert string into stream (function)
// getline	Get line from stream into string (function)
