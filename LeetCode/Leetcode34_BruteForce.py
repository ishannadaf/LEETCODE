"""

34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position
of a given target value. If target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]
Explanation: The first occurrence of 8 is at index 3 and the last occurrence is at index 4.

Example 2:
Input: nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
Explanation: The target is not found in the array.

Example 3:
Input: nums = [], target = 0
Output: [-1, -1]
Explanation: The target is not found in the array.


🧠 Approach 1 — Brute Force
💡 Idea
Traverse array
Track first and last occurrence

"""

def searchRange(nums, target):
    first, last = -1, -1
    
    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    
    return [first, last]

print(searchRange([5, 7, 7, 8, 8, 10], 8))  # Output: [3, 4]

# Time Complexity: O(n) since we may have to check each element in the worst case
# Space Complexity: O(1) since we are not using any extra space