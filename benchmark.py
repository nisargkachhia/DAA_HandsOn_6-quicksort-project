import platform
import psutil
import time
import matplotlib.pyplot as plt
from quicksort_non_random import quicksort
from generate_inputs import generate_best_case, generate_worst_case, generate_average_case

def benchmark(func, input_data):
    start = time.time()
    func(input_data.copy(), 0, len(input_data)-1)
    return time.time() - start

sizes = [100, 500, 1000, 5000, 10000]
best_times = []
worst_times = []
avg_times = []

for size in sizes:
    best_times.append(benchmark(quicksort, generate_best_case(size)))
    worst_times.append(benchmark(quicksort, generate_worst_case(size)))
    avg_times.append(benchmark(quicksort, generate_average_case(size)))

# Plot the results
plt.plot(sizes, best_times, label="Best Case")
plt.plot(sizes, worst_times, label="Worst Case")
plt.plot(sizes, avg_times, label="Average Case")
plt.xlabel("Input size (n)")
plt.ylabel("Time (seconds)")
plt.title("Quicksort Performance (Non-Random Pivot)")
plt.legend()
plt.show()

# Print system information
print("\nSystem Information:")
print(f"Platform: {platform.system()} {platform.release()}")
print(f"Processor: {platform.processor()}")
print(f"RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
print(f"Python Version: {platform.python_version()}")
print(f"ROM: {psutil.disk_usage('/').total / (1024 ** 3):.2f} GB")