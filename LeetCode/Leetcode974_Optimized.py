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



🚀 Approach 2 — Optimal (Prefix Mod + HashMap)
💡 Key Insight

👉 Track frequency of:

prefix_sum % k
🧠 Core Formula

count+=freq[prefix_mod]

⚠️ Important Edge Case

👉 Negative numbers → negative mod

Fix:

prefix_mod = (prefix_sum % k + k) % k

"""


def subarraysDivByK(nums, k):
    prefix_sum = 0
    count = 0
    freq = {0: 1}
    
    for num in nums:
        prefix_sum += num
        prefix_mod = (prefix_sum % k + k) % k
        
        if prefix_mod in freq:
            count += freq[prefix_mod]
        
        freq[prefix_mod] = freq.get(prefix_mod, 0) + 1
    
    return count

# Time Complexity: O(n) where n is the length of the input array nums (due to single loop)
# Space Complexity: O(min(n, k)) since we are using a hash map to store frequencies of prefix sums modulo k

"""

🎯 Pattern

👉 Prefix Sum + Modulo + HashMap

⚠️ Common Mistakes
Forgetting negative mod fix ❌
Not initializing {0:1} ❌
Confusing with sum=k ❌
🔥 Interview Tip

Say:
👉 “If two prefix sums have same mod k, their difference is divisible by k”

That’s the whole trick.


"""