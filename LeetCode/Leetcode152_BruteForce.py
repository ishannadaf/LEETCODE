"""

152. Maximum Product Subarray (Brute Force)
Given an integer array `nums`, find a contiguous non-empty subarray within the array that has
the largest product, and return the product.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6

Example 2:
Input: nums = [-2,0,-1]
Output: 0

"""

def maxProduct(nums):
    n = len(nums)
    max_prod = float('-inf')
    
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]
            max_prod = max(max_prod, prod)
    
    return max_prod


# Time Complexity: O(n^2) where n is the length of the input array nums (due to nested loops)
# Space Complexity: O(1) since we are using only a constant amount of extra space