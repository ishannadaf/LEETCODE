"""

209. Minimum Size Subarray Sum
Given an array of positive integers `nums` and a positive integer `target`, 
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which 
the sum is greater than or equal to `target`. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2

Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

💡 Intuition (VERY IMPORTANT 🔥)

👉 Unlike previous problems:

Window size is NOT fixed

👉 Strategy:

Expand window → increase sum
When sum ≥ target → shrink window
🔥 Key Idea:
Use two pointers left, right
Expand right
Shrink left when condition met

"""

def minSubArrayLen(target, nums):
    left = 0
    total = 0
    min_len = float('inf')

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len

print(minSubArrayLen(7, [2,3,1,2,4,3]))  # Output: 2

# Time Complexity: O(n) where n is the length of the input array nums 
# (each element is visited at most twice by the left and right pointers)
# Space Complexity: O(1) since we are using only a constant amount of extra space


"""

⚡ Key Insight (CRITICAL)

When you see:

“Minimum / Maximum length subarray”
👉 Think variable sliding window

"""