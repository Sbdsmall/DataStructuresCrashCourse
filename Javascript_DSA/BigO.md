# Big O Basic Concepts:
1. ** O(1): Constant Time **
    - Doesn't depend on the size of the data set.
    - Example: Accessing an array element by its index.
1. O(log n): Logarithmic Time
    - Splits the data in each step (divide and conquer).
    - Example: Binary search.
1. O(n): Linear Time
    - Directly proportional to the data set size.
    - Example: Looping through an array.
1. O(n log n): Linearithmic Time
    - Splits and sorts or searches data.
    - Example: Merge sort, quick sort.
1. O(n^k): Polynomial Time
    - Nested loops for each power of n.
    - Example: Bubble sort (O(n^2)).
## Omega (Ω) - Lower Bound
1. What it means: Omega (Ω) describes the best-case scenario for an algorithm.
1. In simple terms: It tells you the fastest an algorithm can run in the best
circumstances.
## Theta (Θ) - Tight Bound
1. In simple terms: It tells you what to generally expect in terms of Fme complexity.
## Big O (O) - Upper Bound (Worst Case)
1. What it means: Big O (O) describes the worst-case scenario for an algorithm. 
1. In simple terms: It tells you the slowest an algorithm can run in the worst
circumstances.
### Useful Tips
1. Best Case, Average Case, Worst Case
2. Consider all scenarios when analyzing. 
3. Drop Non-Dominant Terms
4. In O(n^2 + n), focus on O(n^2) as it will dominate for large n. 
5. Drop Constants
6. O(2n) simplifies to O(n).