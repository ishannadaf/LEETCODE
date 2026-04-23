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
 
 
💡 Core Idea

At each step:

Find mid
Check which half is sorted
Decide where to go
🧠 Logic
Case 1: Left half is sorted
nums[l] <= nums[mid]

👉 Check if target lies here
→ if yes → go left
→ else → go right

Case 2: Right half is sorted

👉 Do the same logic

"""

# Binary Search (Optimized)

def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half sorted
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        # Right half sorted
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    
    return -1

print(search([4,5,6,7,0,1,2], 0))  # Output: 4

# Time Complexity: O(log n) where n is the length of the input array nums (due to binary search)
# Space Complexity: O(1) since we are using only a constant amount of extra space


"""

🎯 Pattern

👉 Modified Binary Search

⚠️ Common Mistakes
Not identifying sorted half ❌
Wrong boundary checks ❌
Infinite loop due to bad conditions ❌
🔥 Interview Tip

If you clearly say:
👉 “One half is always sorted, I’ll exploit that”

→ you’re already ahead of most candidates

"""