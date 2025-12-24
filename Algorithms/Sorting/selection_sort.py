"""

Selection Sort : A simple sorting algorithm that repeatedly finds the minimum element
from the unsorted part and puts it at the beginning.

"""

my_array = [64, 25, 12, 22, 11]
n = len(my_array)
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_idx]:
            min_idx = j
    my_array[i], my_array[min_idx] = my_array[min_idx], my_array[i]
    
print("Sorted array:", my_array)

# Time Complexity: O(n^2)
# Space Complexity: O(1)