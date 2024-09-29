import sys

# Increase recursion limit to handle large inputs
sys.setrecursionlimit(3000)

# Helper function for partitioning
def partition(arr, low, high):
    pivot = arr[high]  # Pivot is the last element
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# QuickSort using median of three as pivot selection for improved performance
def median_of_three(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    arr[mid], arr[high] = arr[high], arr[mid]  # Use the median as pivot

def quicksort(arr, low, high):
    if low < high:
        # Median-of-three strategy to reduce the chance of worst-case partitioning
        median_of_three(arr, low, high)

        pi = partition(arr, low, high)

        quicksort(arr, low, pi - 1)  # Recursively sort elements before pivot
        quicksort(arr, pi + 1, high)  # Recursively sort elements after pivot
