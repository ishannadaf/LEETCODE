"""

238. Product of Array Except Self - Optimized Solution
Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""

def productExceptSelf(nums):
    n = len(nums)
    prefix = [1]*n
    suffix = [1]*n

    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]

    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    result = []
    for i in range(n):
        result.append(prefix[i] * suffix[i])

    return result

productExceptSelf([1,2,3,4])  # Output: [24, 12, 8, 6]

# Time Complexity: O(n) - We traverse the input array three times: once to build the prefix array, 
# once to build the suffix array, and once to build the result array.
# Space Complexity: O(n) - We are using two additional arrays (prefix and suffix) of size n,
# and the result array also takes O(n) space.

#Space Optimized (IMPORTANT)
#No need for suffix array

def productExceptSelf(nums):
    n = len(nums)
    result = [1]*n

    # prefix pass
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # suffix pass
    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


# Time Complexity: O(n) - We traverse the input array twice: once for the prefix pass 
# and once for the suffix pass.
# Space Complexity: O(1) - We are only using a constant amount of extra space (excluding the output array).



"""

🔥 Key Concept
📊 Prefix + Suffix Pattern

This is VERY IMPORTANT

Used in:

Range product/sum problems
Trapping rain water
Subarray problems
⚠️ Common Mistakes
Using division ❌ (not allowed)
Wrong order of prefix/suffix
Overwriting values incorrectly
🧪 Edge Cases
Zeros in array
Negative numbers

👉 This approach handles all automatically ✅

🧠 Pattern Summary

You’ve now mastered:

Hashing
Frequency maps
Grouping
Heap / Bucket
Prefix/Suffix ⭐

"""
