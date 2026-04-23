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


🚀 Approach 2 — Optimal (Binary Search Twice)
💡 Key Insight 🔥

👉 We need:

First occurrence → lower bound
Last occurrence → upper bound

"""

def findFirst(nums, target):
    l, r = 0, len(nums) - 1
    ans = -1
    
    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == target:
            ans = mid
            r = mid - 1   # move left
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    return ans


def findLast(nums, target):
    l, r = 0, len(nums) - 1
    ans = -1
    
    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == target:
            ans = mid
            l = mid + 1   # move right
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    return ans


def searchRange(nums, target):
    return [findFirst(nums, target), findLast(nums, target)]


# Time Complexity: O(n) since we may have to check each element in the worst case
# Space Complexity: O(1) since we are not using any extra space


"""

🧩 Key Understanding
First → push left  
Last → push right
🎯 Pattern

👉 Binary Search (Lower Bound + Upper Bound)

⚠️ Common Mistakes
Stopping at first match ❌
Not continuing search ❌
Mixing conditions ❌
🔥 Interview Tip

Say:
👉 “I’ll run binary search twice to find boundaries”

"""