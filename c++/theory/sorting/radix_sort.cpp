// # Radix Sort — Complete Notes (copy-paste ready)

// ## 1. What is Radix Sort?
// - Radix sort is a non-comparative integer sorting algorithm.
// - It sorts numbers by processing individual digits (or "radices") from least significant to most (LSD) or most to least (MSD).
// - Uses a stable subroutine (commonly counting sort) to sort by each digit.
// - Best when keys have fixed length or small range of digits.

// ## 2. Intuition / Analogy
// - Imagine sorting mail by ZIP code: first group by the last digit, then by the second-last, and so on. After processing all digit positions (from least significant to most), mail is fully sorted. Each pass refines order while preserving previous order for equal digits (stability).

// ## 3. High-level Algorithm (LSD Radix Sort for base 10)
// 1. Find maximum number to know number of digits `d`.
// 2. For `exp = 1` (1s place); `exp <= max`; `exp *= 10`:
//    - Use counting sort (stable) to sort array by digit `(number / exp) % 10`.
// 3. After `d` passes, array is sorted.

// ## 4. Step-by-step Example
// Array: [170, 45, 75, 90, 802, 24, 2, 66]

// - Pass 1 (units digit):
//   - Bucket by units → order becomes (170, 90, 802, 2, 24, 45, 75, 66) after stable counting
// - Pass 2 (tens digit):
//   - Sort by tens preserving previous order → becomes (802, 2, 24, 45, 66, 170, 75, 90)
// - Pass 3 (hundreds digit):
//   - Sort by hundreds → (2, 24, 45, 66, 75, 90, 170, 802) sorted.

// ## 5. Complexity
// - Time: O(d * (n + k))
//   - n = number of elements
//   - d = number of digits (≈ log_base(maxValue))
//   - k = base (e.g., 10 for decimal)
// - Space: O(n + k) for counting buckets (not in-place)
// - If d is constant (fixed-size keys) complexity ≈ O(n)
// - Not comparison-based, so can beat O(n log n) when d is small

// ## 6. Variants
// - LSD (Least Significant Digit): process digits from least to most significant — common for integers, stable.
// - MSD (Most Significant Digit): process from most significant; useful for variable-length keys (strings) and can partition recursively.
// - Bases: base 2^b (binary digits), base 10, base 256 (bytes) — choosing base affects passes vs bucket size tradeoff.

// ## 7. Key Implementation Details
// - Must use a stable sort for each digit pass (counting sort is typical).
// - For negative numbers: either
//   - separate negatives and positives, sort absolute values then merge (negatives in reverse),
//   - or offset values by adding a constant to make them non-negative.
// - For large keys, choose larger base to reduce passes (but increases k memory/time per pass).

// ## 8. Advantages vs Other Sorts
// - Can be linear time for fixed-length keys: O(n).
// - Not comparison-limited → can outperform O(n log n) sorts on suitable data.
// - Simple to implement for integers and fixed-length strings.
// - Stable (when using stable subroutine), useful for multi-key sorting.

// ## 9. Disadvantages vs Other Sorts
// - Extra memory required (O(n + k)); not in-place.
// - Performance depends on number of digits (d) and base (k).
// - For large keys (many digits) or huge base, overhead can be worse than std::sort.
// - Only works directly on discrete keys (integers, fixed-length strings); needs adaptations for negatives or floating points.
// - Implementation complexity increases for variable-length keys or larger alphabets.

// ## 10. When to Use Radix Sort
// - Sorting integers with limited number of digits (e.g., 32-bit ints).
// - Sorting fixed-length strings (e.g., fixed-width keys).
// - When you need stable, linear-time sorting and memory for buckets is acceptable.
// - In systems/competitions where guaranteed linear-ish time beats worst-case O(n log n).

// ## 11. Practical Tips
// - Use counting sort as the stable subroutine.
// - Use base = 256 (1 byte) for large integers to reduce passes (d = bytes count), but counting array length = 256.
// - For 32-bit ints using base 256 → 4 passes, good performance.
// - For negatives: handle separately or offset.
// - For general use and large/unknown inputs, std::sort (introsort) is robust and often faster in practice.

// ## 12. C++ Example (LSD Radix Sort for non-negative integers)
// ````cpp
// Radix sort (LSD) using counting sort for base 10
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void countingSortByDigit(vector<int>& a, int exp) {
    int n = a.size();
    vector<int> output(n);
    int count[10] = {0};

    // Count occurrences of digits
    for (int i = 0; i < n; ++i) {
        int digit = (a[i] / exp) % 10;
        ++count[digit];
    }
    // Make count[i] contain actual position (stable)
    for (int i = 1; i < 10; ++i) count[i] += count[i - 1];

    // Build output array (traverse from end for stability)
    for (int i = n - 1; i >= 0; --i) {
        int digit = (a[i] / exp) % 10;
        output[count[digit] - 1] = a[i];
        --count[digit];
    }
    // Copy to original
    for (int i = 0; i < n; ++i) a[i] = output[i];
}

void radixSort(vector<int>& a) {
    if (a.empty()) return;
    int mx = *max_element(a.begin(), a.end());
    for (int exp = 1; mx / exp > 0; exp *= 10)
        countingSortByDigit(a, exp);
}

int main() {
    vector<int> arr = {170, 45, 75, 90, 802, 24, 2, 66};
    radixSort(arr);
    for (int x : arr) cout << x << " ";
    cout << endl;
    return 0;
}