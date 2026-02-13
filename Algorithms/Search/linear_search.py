"""
Docstring for Algorithms.Search.linear_search
This module implements the Linear Search algorithm to find a specific element in an array.
Linear Search : A simple search algorithm that checks each element in the array sequentially until the desired element is found or the end of the array is reached.
To implement the Linear Search algorithm in a programming language, we need:
1. An array with values to search.
2. A target value to search for in the array.
3. A loop to iterate through each element in the array and compare it with the target value

"""

def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

arr = [3, 7, 2, 9, 5]
targetVal = 9

result = linearSearch(arr, targetVal)

if result != -1:
    print("Value",targetVal,"found at index",result)
else:
    print("Value",targetVal,"not found")
    
# Time Complexity: O(n) in the worst and average cases, where n is the number of elements in the array.
# Space Complexity: O(1) as it uses a constant amount of space.