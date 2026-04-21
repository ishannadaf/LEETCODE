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


💡 Intuition (VERY IMPORTANT 🔥)

👉 Maintain a window where:

Number of zeros ≤ k

👉 If zeros > k:

Shrink window from left
🔥 Key Idea:
Count zeros in window
Expand right
Shrink left when invalid

"""


def longestOnes(nums, k):
    left = 0
    zeros = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # Output: 6

# Time Complexity: O(n) where n is the length of the input array nums (due to single pass)
# Space Complexity: O(1) since we are using only a constant amount of extra space


"""

⚡ Key Insight (VERY IMPORTANT)

When condition is:

“At most k changes / errors”
👉 Use variable sliding window + constraint tracking

"""