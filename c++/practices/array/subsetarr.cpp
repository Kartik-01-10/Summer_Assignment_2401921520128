#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v1 = {1, 2, 3, 4, 5};
    vector<int> v2 = {1, 7};
    int a = v1.size();
    int b = v2.size();
    bool c = true;

    for (int j = 0; j < b; j++) {
        bool found = false;
        for (int i = 0; i < a; i++) {
            if (v1[i] == v2[j]) {
                found = true;
                break;
            }
        }
        if (!found) {
            c = false;
            break;
        }
    }

    if (c == true) {
        cout << "one is subset of another one";
    } else {
        cout << "not a subset";
    }

    return 0;
}