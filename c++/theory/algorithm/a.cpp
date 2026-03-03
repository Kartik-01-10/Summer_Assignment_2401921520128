// 1. algorithm...
// Sieve of Eratosthenes algorithm : it is used to find all prime numbers up to a given limit n
// Time complexity : O(n log log n)
// Space complexity : O(n)
// Steps : how to implement
// 1. Create a boolean array isPrime[0..n] and initialize all entries   as true. A value in isPrime[i] will be false if i is Not a prime, else true.
// 2. Set isPrime[0] and isPrime[1] to false as 0 and 1 are not prime numbers.
// 3. Start with the first prime number, p = 2. Mark all multiples of p as false (not prime).
// 4. Find the next number greater than p in the list that is still true. This number is the next prime.
// 5. Repeat steps 3 and 4 until p^2 is greater than n
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <climits>
using namespace std;

void sieveOfEratosthenes(int n) {
    vector<bool> isPrime(n + 1, true);
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
                }
            }
        }
    // Print all prime numbers
    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) {
            cout << i << " ";
        }
    }
}

// 2 method
class Solution {
public:
    int countPrimes(int n) {
        if (n == 0 || n == 1) return 0;
        vector<int> s(n);
        for (int i = 2; i < sqrt(n); i++) {
            if (s[i] != 0)
                continue;
            for (int j = i * i; j < n; j += i) {
                s[j] = 1;
            }
        }
        return count(s.begin() + 2, s.end(), 0);
    }
};


 



//brute force to check total subarray
int subarray(vector<int>& nums) { // O(n^3) 
    for (int st = 0 ; st < nums.size() ; st++) {
        for (int end = st ; end < nums.size() ; end++) {
            for (int i = st ; i <= end ; i++) {
                    cout<<nums[i]<<" ";
            }
            cout<<endl;
        }
    }
    return 0;
}  // by this methode if we want find max sum subarray then we get o(n^3)
// if input is 1 2 3 4 5 
//output :
// 1 12 123 1234 12345
// 2 23 234 2345
// 3 34 345
// 4 45
// 5

// more optimise O(n^2) in which we can find currsum 
int subarray2(vector<int>& nums) {
    int maxSum = INT_MIN;
    for (int st = 0 ; st < nums.size() ; st++) {
        int currsum = 0;
        for (int end = st ; end < nums.size() ; end++) {
            currsum += nums[end];
            maxSum = max(maxSum, currsum);
        
        }
        cout<<maxSum<<endl;
    }
    return 0;

}
// kadane's algorithm for maximum subarray sum
 // what algorithm specifically does is it iterates through the array, maintaining a running sum of the current subarray.
 // If the running sum becomes negative, it resets it to zero, as starting a new sub
int maxSubArray(vector<int>& nums) { //O(n)
    int maxSum = nums[0];
    int currentSum = 0;

    for (int num : nums) {
        currentSum += num;
        
        maxSum = max(maxSum, currentSum);
        if (currentSum < 0) {
            currentSum = 0;
        }
    }
    return maxSum;
}