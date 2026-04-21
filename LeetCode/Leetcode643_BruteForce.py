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

💡 Intuition (VERY IMPORTANT 🔥)
👉 Brute Force:
- Check all subarrays of length k
- Calculate average
- Update maximum average

"""


def findMaxAverage(nums, k):
    max_avg = float('-inf')

    for i in range(len(nums) - k + 1):
        total = sum(nums[i:i+k])
        max_avg = max(max_avg, total / k)

    return max_avg


# Time Complexity: O(n*k) where n is the length of the input array nums (due to nested loops) 
# and k is the length of the subarray (due to sum calculation)
# Space Complexity: O(1) since we are using only a constant amount of extra space 