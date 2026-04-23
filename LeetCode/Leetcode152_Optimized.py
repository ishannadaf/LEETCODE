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
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        curr = nums[i]
        
        temp_max = max(curr, curr * max_prod, curr * min_prod)
        min_prod = min(curr, curr * max_prod, curr * min_prod)
        max_prod = temp_max
        
        result = max(result, max_prod)
    
    return result

print(maxProduct([2,3,-2,4]))  # Output: 6

# Time Complexity: O(n) where n is the length of the input array nums (due to single loop)
# Space Complexity: O(1) since we are using only a constant amount of extra space



"""

🎯 Pattern

👉 Kadane Variant (Track min + max)

⚠️ Common Mistakes
Only tracking max ❌
Forgetting min product ❌
Not handling negative flip ❌
🔥 Interview Tip

If you say this line, you're solid:
👉 “Because of negatives, I track both min and max — since min can become max”

"""