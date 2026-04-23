"""

88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The number of elements initialized in nums1 and nums2 are m and n respectively. 
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

🚀 Approach 2 — Optimal (Two Pointers from End)
💡 Key Insight 🔥

👉 Fill from back side
Because front shifting is expensive

🧠 Logic
i → end of nums1 valid part
j → end of nums2
k → end of nums1

Compare and place largest at k
Move pointers accordingly

"""

def merge(nums1, m, nums2, n):
    i = m - 1 # Pointer for nums1
    j = n - 1 # Pointer for nums2
    k = m + n - 1 # Pointer for merged array in nums1
    
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        
        k -= 1
        
print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))  # Output: [1,2,2,3,5,6]
    
# Time Complexity: O(m + n) since we are traversing both arrays once
# Space Complexity: O(1) since we are modifying nums1 in place


"""

🎯 Pattern

👉 Two Pointers (Reverse Fill)

⚠️ Common Mistakes
Starting from front ❌
Not using extra space in nums1 properly ❌
Forgetting while j >= 0 condition ❌
🔥 Interview Tip

Say:
👉 “I’ll merge from the end to avoid shifting elements”

"""
