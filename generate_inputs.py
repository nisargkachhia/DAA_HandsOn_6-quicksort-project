import numpy as np

def generate_best_case(n):
    # Best case is when the input is already sorted
    return list(range(n))

def generate_worst_case(n):
    # Worst case is when the input is reverse sorted
    return list(range(n, 0, -1))

def generate_average_case(n):
    # Average case is when the input is randomly shuffled
    return np.random.randint(0, 1000, size=n).tolist()
