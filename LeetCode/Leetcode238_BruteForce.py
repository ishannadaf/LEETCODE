"""
238. Product of Array Except Self

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
    result = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i != j:
                prod *= nums[j]
        result.append(prod)
    return result


# Time Complexity: O(n^2) - We have a nested loop where the outer loop runs n times and 
# the inner loop also runs n times in the worst case.
# Space Complexity: O(n) - We are storing the result in a new list that takes O(n) space.
