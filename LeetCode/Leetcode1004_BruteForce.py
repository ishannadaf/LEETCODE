"""

1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,0]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined

Example 2:
Input: nums = [0,0,1,1,1,0,0], k = 0
Output: 3
Explanation: The bolded numbers were flipped from 0 to 1. The longest subarray is underlined

"""


def longestOnes(nums, k):
    n = len(nums)
    max_len = 0

    for i in range(n):
        zeros = 0
        for j in range(i, n):
            if nums[j] == 0:
                zeros += 1
            if zeros <= k:
                max_len = max(max_len, j - i + 1)
            else:
                break

    return max_len

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # Output: 6

# Time Complexity: O(n^2) where n is the length of the input array nums (due to nested loops)
# Space Complexity: O(1) since we are using only a constant amount of extra space
