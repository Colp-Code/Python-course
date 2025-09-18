import numpy as np

arr = np.array(range(101))

average = np.mean(arr)
print(average)

summation = np.sum(arr)
print(summation)

maximum = np.max(arr)
print(maximum)

minimum = np.min(arr)
print(minimum)

std_dev = np.std(arr)
print(std_dev)

even_numbers = arr[arr % 2 == 0]
print(even_numbers)