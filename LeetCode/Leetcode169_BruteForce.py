"""

169. Majority Element
Given an array nums of size n, return the majority element. 
The majority element is the element that appears more than ⌊n / 2⌋ times in the array. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2


🧠 Approach 1 — Brute Force (Counting)
💡 Idea
For each element → count frequency
If > n/2 → return that element

"""

def majorityElement(nums):
    n = len(nums)
    
    for i in nums:
        if nums.count(i) > n // 2:
            return i

# Time Complexity: O(n^2) where n is the length of the input array nums (due to count method inside loop)
# Space Complexity: O(1) since we are using only a constant amount of extra space