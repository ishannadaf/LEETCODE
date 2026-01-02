"""

Quick sort implementation in Python.
Quick Sort : An efficient sorting algorithm that uses a divide-and-conquer approach to sort an array of numbers in ascending order.
To implement the Quick Sort algorithm in a programming language, we need:
1. An array with values to sort.
2. A base case to end the recursion when the array has one or zero elements.
3. A pivot element to partition the array into sub-arrays of elements less than, equal to, and greater than the pivot.
4. Recursive calls to sort the sub-arrays and combine them with the pivot to form the sorted array.


"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]#arr[len(arr) // 2]   # Choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


# Example usage
numbers = [10, 7, 8, 9, 1, 5]
sorted_numbers = quick_sort(numbers)

print("Sorted array:", sorted_numbers)


# Time Complexity: O(n log n) on average, O(n^2) in the worst case (n^2 when pivot is always smaller or largest).
# Space Complexity: O(log n) due to recursive stack space.