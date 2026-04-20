"""

1. Two Sum - Brute Force Approach
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers 
such that they add up to `target`.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

"""


def twoSum_bruteforce(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = twoSum_bruteforce(nums, target)
print(result)  # Output: [0, 1]

# Time Complexity: O(n^2) - We have two nested loops, each iterating through the list of numbers.
# Space Complexity: O(1) - We are using a constant amount of extra space to 
# store the indices of the two numbers.