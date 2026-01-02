"""
Docstring for Algorithms.Sorting.counting_sort
This module implements the Counting Sort algorithm to sort an array of non-negative integers in ascending order.
Counting Sort : A non-comparison based sorting algorithm that counts the occurrences of each unique element in the input array and uses this information to place the elements in sorted order.
To implement the Counting Sort algorithm in a programming language, we need:
1. An array with non-negative integer values to sort.
2. Determine the maximum value in the array to define the range of the counting array.
3. Create a counting array to store the count of each unique element.
4. Modify the counting array to store the cumulative count of elements.
5. Build the output sorted array using the counting array.

"""

def countingSort(arr):
    if not arr:
        return arr
        
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1
        
    arr[:] = []

    for num, freq in enumerate(count):
        arr.extend([num] * freq)

    return arr

unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sortedArr = countingSort(unsortedArr)
print("Sorted array:", sortedArr)

# Time Complexity: O(n + k) where n is the number of elements in the input array and k is the range of the input values.
# Space Complexity: O(k) for the counting array.