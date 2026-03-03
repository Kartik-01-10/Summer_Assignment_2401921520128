// # Shell Sort — Complete Notes (copy-paste ready)

// ## 1. What is Shell Sort?
// - Shell sort is an in-place comparison-based sorting algorithm.
// - It generalizes insertion sort by allowing exchanges of items that are far apart.
// - Uses a sequence of "gaps" to perform gapped insertion sorts; final pass has gap = 1 (regular insertion sort).

// ## 2. Intuition / Analogy
// - Think of sorting people by height in a stadium: first, sort people in groups separated by many seats (big gap) so tall/short people move closer to their final region; gradually reduce the gap and do finer sorting. By the time gap = 1, the list is nearly sorted, so insertion sort is fast.

// ## 3. High-level Algorithm
// 1. Choose a gap sequence (common: start = n/2, then gap /= 2 until gap = 0).
// 2. For each gap `g`, do a gapped insertion sort:
//    - For i = g .. n-1:
//      - temp = a[i]
//      - j = i
//      - while j >= g and a[j-g] > temp:
//          - a[j] = a[j-g]; j -= g
//      - a[j] = temp
// 3. Repeat with smaller gap until gap = 1 (final insertion sort).

// ## 4. Step-by-step Example
// Array: [23, 12, 1, 8, 34, 54, 2, 3], n = 8  
// - gap = 4 (n/2): groups: indices (0,4), (1,5), (2,6), (3,7)
//   - sort each group using insertion logic → partially ordered array
// - gap = 2: groups: (0,2,4,6), (1,3,5,7)
//   - perform gapped insertion sort on these groups → more ordered
// - gap = 1: normal insertion sort; since array is nearly sorted, few moves needed → fully sorted

// (You can simulate values for each pass to see how elements move toward correct positions.)

// ## 5. Complexity
// - Best case: O(n log n) for some gap sequences, O(n) for already sorted (practically depends)
// - Average: depends on gap sequence; typical empirical ~ O(n^(4/3)) or O(n^(5/4))
// - Worst case: varies with gap sequence; with simple gap = n/2^k often ~ O(n^2)
// - Space: O(1) (in-place)
// - Stable? No (standard implementations are not stable)

// ## 6. Common Gap Sequences (affects performance)
// - Shell original: gap = n/2, n/4, ... , 1 (simple, easy)
// - Hibbard: 1, 3, 7, 15, ... (2^k − 1)
// - Knuth: (3^k − 1) / 2  → sequence: 1, 4, 13, 40, ...
// - Sedgewick, Pratt, Tokuda, Ciura: better empirical performance (Ciura's small sequence is popular: 1,4,10,23,57,132,301,701,1750,...)

// ## 7. Advantages vs Other Sorts
// - Faster than insertion sort and bubble sort for medium-sized arrays because far-away exchanges accelerate progress.
// - In-place and simple to implement.
// - Good when memory is limited (no extra arrays needed).
// - For moderate n (thousands), can be competitive and simpler than quicksort.

// ## 8. Disadvantages vs Other Sorts
// - Not stable by default.
// - Worst-case complexity can be O(n^2) (depends on gap sequence).
// - For large n, highly optimized quicksort or mergesort outperforms Shell sort.
// - Performance is sensitive to gap sequence choice.

// ## 9. When to Use Shell Sort
// - Small to medium arrays where simplicity and low memory overhead matter.
// - Embedded systems or environments where recursion/extra memory is costly.
// - Educational purposes and when predictable in-place behavior is desired.

// ## 10. C++ Implementation Example (copy-paste)
// ```cpp
#include <vector>
#include <iostream>
using namespace std;

// Simple Shell sort using gap = n/2, then gap /= 2
void shellSort(vector<int>& a) {
    int n = a.size();
    for (int gap = n / 2; gap > 0; gap /= 2) {
        // gapped insertion sort for this gap
        for (int i = gap; i < n; ++i) {
            int temp = a[i];
            int j = i;
            // shift elements of the subarray that are greater than temp
            while (j >= gap && a[j - gap] > temp) {
                a[j] = a[j - gap];
                j -= gap;
            }
            a[j] = temp;
        }
    }
}

int main() {
    vector<int> arr = {23, 12, 1, 8, 34, 54, 2, 3};
    shellSort(arr);
    for (int x : arr) cout << x << " ";
    cout << endl;
    return 0;
}
// ```

// ## 11. Practical Tips / Notes
// - Try better gap sequences (Knuth, Ciura) for improved performance.
// - Shell sort is easy to implement and tune; often used where memory is tight.
// - Not stable: if stability is required, use mergesort/stable algorithms.
// - For large datasets, prefer quicksort (std::sort) or mergesort/heapsort depending on stability/memory needs.
// - Measuring on your data is best: empirical performance can vary with input distribution.

// ## 12. Quick Summary
// - Shell sort = repeated gapped insertion sorts with decreasing gaps.
// - In-place, simple, faster than naive sorts for moderate sizes.
// - Complexity and performance depend heavily on gap sequence.
// - Use for medium-size arrays and memory-constrained contexts; use std::sort for large/general-purpose sorting.
