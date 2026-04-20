
"""

1. Two Sum - Optimized Approach
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


def twoSum(nums, target):
    hashmap = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in hashmap:
            return [hashmap[complement], i]
        
        hashmap[num] = i

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)

print(result)  # Output: [0, 1]

# Time Complexity: O(n) - We traverse the list of numbers once.
# Space Complexity: O(n) - In the worst case, we may store all numbers in the hashmap.


"""

🔥 Important Interview Concepts
1. HashMap Lookup Trick

👉 “Check before insert” pattern

2. Complement Thinking

Instead of:

a + b = target

Think:

b = target - a
3. Order Matters ⚠️
if complement in hashmap:
    return ...

hashmap[num] = i

👉 If you reverse this → you may use same element twice ❌

⚠️ Common Mistakes
Using same element twice
Returning values instead of indices
Adding to hashmap before checking
🧪 Variations (Very Important)

Interviewer may twist this:

Sorted array → use Two Pointers
Return values instead of indices
Multiple pairs → modify logic
3Sum → extension of this

"""

