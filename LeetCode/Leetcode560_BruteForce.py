"""

560. Subarray Sum Equals K
Given an array of integers `nums` and an integer `k`, 
return the total number of continuous subarrays whose sum equals to `k`.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2


🧠 Why Sliding Window FAILS ❌

👉 Because array can have negative numbers
→ sum is not monotonic
→ window expand/shrink logic breaks

🧠 Approach 1 — Brute Force (O(n²))
💡 Idea
Try all subarrays
Count those with sum = k

"""

def subarraySum(nums, k):
    n = len(nums)
    count = 0
    
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum == k:
                count += 1
    
    return count

print(subarraySum([1,2,3], 3))  # Output: 2
# Time Complexity: O(n^2) where n is the length of the input array nums (due to nested loops)
# Space Complexity: O(1) since we are using only a constant amount of extra space
