
// Given an array of integers nums and an integer target, return indices of the two numbers such that
// they add up to target
#include <iostream>
#include <vector>
using namespace std;

vector <int> sum(int nums[], int target, int l) {
    vector <int> v;
    for (int i = 0; i < l; i++) {
        for (int j = i + 1; j < l; j++) {
            if (target == (nums[i] + nums[j])) {
                v.push_back(i);
                v.push_back(j);
                return v;  // ✅ return immediately after finding the pair
            }
        }
    }
    return v;  // ✅ return empty vector if no pair found
}

int main() {
    int nums[] = {1, 2, 3, 4, 5};
    int target;
    cout << "enter target : ";
    cin >> target;
    int l = sizeof(nums) / sizeof(nums[0]);

    vector<int> result = sum(nums, target, l);  // ✅ capture the result

    if (!result.empty()) {
    cout << "Indices: " << result[0] << " and " << result[1] << endl;
} else {
    cout << "No two numbers add up to the target." << endl;
}
    return 0;
}