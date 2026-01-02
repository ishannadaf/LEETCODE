"""
Docstring for Algorithms.Sorting.merge_sort
This module implements the Merge Sort algorithm to sort an array of numbers in ascending order.
Merge Sort : A divide-and-conquer sorting algorithm that divides the input array into two halves,
sorts each half recursively, and then merges the sorted halves to produce the final sorted array.
To implement the Merge Sort algorithm in a programming language, we need:
1. An array with values to sort.
2. A base case to end the recursion when the array has one or zero elements.
3. A function to merge two sorted arrays into a single sorted array.

"""

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)

# Time Complexity: O(n log n) for all cases (best, average, worst).
# Space Complexity: O(n) due to the temporary arrays used for merging.