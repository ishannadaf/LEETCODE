"""

33. Search in Rotated Sorted Array (Brute Force)
Given an integer array `nums` sorted in ascending order (with distinct values), and an integer 
target, suppose that `nums` is rotated at some pivot unknown to you beforehand 
(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`). If target is found in the array return its index, 
otherwise return -1. 

You must write an algorithm with O(log n) runtime complexity. 

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

🧠 Key Observation 🔥

Even after rotation:
👉 At least one half is always sorted

Example:

[4,5,6,7 | 0,1,2]
 Left sorted   Right sorted

"""

# Linear Search (Brute Force)

def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

# Time Complexity: O(n) where n is the length of the input array nums (due to single loop)
# Space Complexity: O(1) since we are using only a constant amount of extra space