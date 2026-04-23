"""

153. Find Minimum in Rotated Sorted Array
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. 
For example, 
the array `nums = [0,1,2,4,5,6,7]` might become: 
- `[4,5,6,7,0,1,2]` if it was rotated 4 times.
- `[0,1,2,4,5,6,7]` if it was rotated 7 times.

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

"""

def findMin(nums):
    l, r = 0, len(nums) - 1
    
    while l < r:
        mid = (l + r) // 2
        
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    
    return nums[l]


# Time Complexity: O(log n) where n is the length of the input array nums (due to binary search)
# Space Complexity: O(1) since we are using only a constant amount of extra space


"""

🎯 Pattern

👉 Binary Search on Answer Space

⚠️ Common Mistakes
Using l <= r loop ❌ (can break logic)
Not including mid in left half ❌
Confusing with search problem ❌
🔥 Interview Tip

Say this clearly:
👉 “I compare mid with right to detect unsorted half”

That’s the whole trick. If mid > right → min is in right half
Else → min is in left half (including mid)


"""