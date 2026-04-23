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


🚀 Approach 2 — Optimal (Prefix Sum + HashMap)
💡 Key Insight 🔥

👉 If:

prefix_sum[j] - prefix_sum[i] = k

👉 Then:

prefix_sum[i] = prefix_sum[j] - k
🧠 Core Formula

count+=freq[prefix_sum−k]

"""

def subarraySum(nums, k):
    prefix_sum = 0
    count = 0
    freq = {0: 1}
    
    for num in nums:
        prefix_sum += num
        
        if (prefix_sum - k) in freq:
            count += freq[prefix_sum - k]
        
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    
    return count

print(subarraySum([1,2,3], 3))  # Output: 2
# Time Complexity: O(n) where n is the length of the input array nums (due to single loop)
# Space Complexity: O(n) since we are using a HashMap to store prefix sums


"""

🎯 Pattern

👉 Prefix Sum + HashMap (VERY IMPORTANT)

⚠️ Common Mistakes
Forgetting freq = {0:1} ❌
Using sliding window ❌
Not understanding prefix logic ❌
🔥 Interview Tip

Say this:
👉 “I’ll use prefix sum and check how many times (sum - k) appeared”

That’s the entire trick.

"""