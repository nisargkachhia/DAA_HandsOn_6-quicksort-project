# DAA_HandsOn-6

## Quicksort Benchmark Project

This project implements two versions of the quicksort algorithm (non-random and random pivot) and benchmarks the non-random version for the best, worst, and average cases.

## Files
- `quicksort.py`: Non-random pivot quicksort implementation.
- `quicksort_random.py`: Random pivot quicksort implementation.
- `generate_inputs.py`: Functions to generate best, worst, and average case inputs.
- `benchmark.py`: Script to benchmark non-random quicksort and plot the results.

## How to Run
1. Install required libraries: `pip install numpy matplotlib`.
2. Run the benchmarking script: `python benchmark.py`.

## Benchmark Results

The following results were obtained from running the Quicksort benchmarks for different input sizes. The times are measured in milliseconds (ms) for each case:

```plaintext
Best Case (n=100): 0.000000ms
Worst Case (n=100): 0.000000ms
Average Case (n=100): 0.000000ms

Best Case (n=500): 10.731220ms
Worst Case (n=500): 0.504732ms
Average Case (n=500): 0.000000ms

Best Case (n=1000): 3.248692ms
Worst Case (n=1000): 2.505541ms
Average Case (n=1000): 0.978708ms

Best Case (n=5000): 3.257275ms
Worst Case (n=5000): 19.475698ms
Average Case (n=5000): 12.760878ms

Best Case (n=10000): 17.378807ms
Worst Case (n=10000): 73.850632ms
Average Case (n=10000): 65.176487ms
```

![Graph](https://github.com/user-attachments/assets/213a42df-0b21-42c0-9fc0-d2d5a78d24c9)

## System Information

The benchmarks were run on the following system configuration:

```plaintext
Platform: Windows 10
Processor: Intel64 Family 6 Model 142 Stepping 12, GenuineIntel
RAM: 7.86 GB
Python Version: 3.10.5
ROM: 500.00 GB
```

## Deriving the Average Case Time Complexity for Non-Random Quicksort

The average case time complexity of the non-random pivot version of Quicksort can be derived mathematically. In general, Quicksort performs well with random pivots, but when using a fixed pivot strategy (like the first or last element), the average time complexity can be analyzed as follows:

1. **Divide and Conquer**: Each partitioning operation divides the array into two subarrays. The performance depends on how evenly the pivot splits the array.
  
2. **Recursive Formula**: The recursive time complexity can be represented as:
   \[
   T(n) = T(k) + T(n - k - 1) + O(n)
   \]
   where \(k\) is the number of elements in one partition and \(O(n)\) accounts for the time taken to partition the array.

3. **Expected Splits**: On average, the pivot will split the array into two roughly equal halves. This gives us:
   \[
   T(n) = 2T\left(\frac{n}{2}\right) + O(n)
   \]

4. **Master Theorem**: By applying the Master Theorem, we can conclude:
   \[
   T(n) = O(n \log n)
   \]
   Therefore, the average case time complexity of non-random Quicksort is \(O(n \log n)\).
