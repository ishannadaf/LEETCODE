"""
Docstring for Algorithms.Search.binary_search
This module implements the Binary Search algorithm to find a specific element in a sorted array.
Binary Search : An efficient search algorithm that repeatedly divides the search interval in half to locate the target
element. The array must be sorted prior to performing a binary search.
To implement the Binary Search algorithm in a programming language, we need:
1. A sorted array with values to search.
2. A target value to search for in the array.
3. Two pointers to represent the current search interval (low and high).

"""

def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid
        
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15

result = binarySearch(myArray, myTarget)

if result != -1:
    print("Value",myTarget,"found at index", result)
else:
    print("Target not found in array.")