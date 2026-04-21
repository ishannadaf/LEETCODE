"""

643. Maximum Average Subarray I
Given an array consisting of `n` integers, find the contiguous subarray of given length `k` 
that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

💡 Intuition

👉 Instead of recomputing sum:

Maintain running window sum
🔥 Key Idea:
Add next element
Remove previous element

"""


def findMaxAverage(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k


# Time Complexity: O(n) where n is the length of the input array nums (due to single loop)
# and k is the length of the subarray (due to constant time operations for sum updates)
# Space Complexity: O(1) since we are using only a constant amount of extra space 