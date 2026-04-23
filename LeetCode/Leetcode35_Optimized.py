"""

35. Merge Sorted Array (Brute Force)
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

"""

def searchInsert(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l


# Time Complexity: O(log n) since we are performing binary search
# Space Complexity: O(1) since we are not using any extra space

"""

🧩 Key Understanding
Loop ends when l > r  
At that moment → l = correct insert position
🎯 Pattern

👉 Binary Search (Lower Bound concept)

⚠️ Common Mistakes
Returning r instead of l ❌
Not understanding final pointer position ❌
🔥 Interview Tip

Say:
👉 “If target not found, left pointer gives insertion index”

"""