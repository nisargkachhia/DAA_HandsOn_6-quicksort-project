import random

def partition_random(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[rand_pivot], arr[high] = arr[high], arr[rand_pivot]  # swap random pivot with last element
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]  # fixed pivot (last element)
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quicksort_random(arr, low, high):
    if low < high:
        pi = partition_random(arr, low, high)
        quicksort_random(arr, low, pi - 1)
        quicksort_random(arr, pi + 1, high)
