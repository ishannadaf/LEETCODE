
"""

217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false


"""

def containsDuplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return True
    return False


# Time Complexity: O(n^2) - We have two nested loops, each iterating through the list of numbers.
# Space Complexity: O(1) - We are using a constant amount of extra space to store the indices of the two numbers.

