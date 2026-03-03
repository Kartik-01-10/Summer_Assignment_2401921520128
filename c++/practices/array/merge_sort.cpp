#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& a, vector<int>& b, vector<int>& v) {
    int m = a.size();
    int n = b.size();
    v.clear(); // make sure v is empty before merging

    int i = 0, j = 0;
    while (i < m && j < n) {
        if (a[i] < b[j]) {
            v.push_back(a[i]);
            i++;
        } else {
            v.push_back(b[j]);
            j++;
        }
    }
    while (i < m) {
        v.push_back(a[i]);
        i++;
    }
    while (j < n) {
        v.push_back(b[j]);
        j++;
    }
}

void mergeSort(vector<int>& ar) {
    int n = ar.size();
    if (n == 1) return;

    int n1 = n / 2;
    int n2 = n - n1;

    vector<int> a(ar.begin(), ar.begin() + n1);
    vector<int> b(ar.begin() + n1, ar.end());

    mergeSort(a);
    mergeSort(b);
    merge(a, b, ar);
    a.clear();
    b.clear();
}

int main() {
    vector<int> a = {7, 3, 75, 2, 34, 6665, 657, 57, 34, 345, 46, 4664, 4, 3};
    mergeSort(a);
    for (int i = 0; i < a.size(); i++) {
        cout << a[i] << " ";
    }
    cout << endl;
}