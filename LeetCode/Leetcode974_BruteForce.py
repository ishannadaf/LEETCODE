"""

974. Subarray Sums Divisible by K
Given an integer array `nums` and an integer `k`, return the number of non-empty subarrays 
that have a sum divisible by `k`.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7

Example 2:
Input: nums = [5], k = 9
Output: 0



🧠 Key Insight 🔥

👉 Instead of sum = k
We need:

sum % k == 0
🧠 Core Trick

If:

(prefix_sum[j] % k) == (prefix_sum[i] % k)

👉 Then subarray between them is divisible by k

🧠 Why?
(prefix[j] - prefix[i]) % k = 0
🧠 Approach 1 — Brute Force (O(n²))
💡 Idea
Try all subarrays
Check if sum % k == 0

"""


def subarraysDivByK(nums, k):
    n = len(nums)
    count = 0
    
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum % k == 0:
                count += 1
    
    return count

# Time Complexity: O(n^2) where n is the length of the input array nums (due to nested loops)
# Space Complexity: O(1) since we are using only a constant amount of extra space