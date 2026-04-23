"""

704. Binary Search (Brute Force)
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

"""


def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


# Time Complexity: O(n) since we may have to check each element in the worst case
# Space Complexity: O(1) since we are not using any extra space