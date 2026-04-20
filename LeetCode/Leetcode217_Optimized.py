
"""

217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false


"""

def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


# Time Complexity: O(n) - We are iterating through the list of numbers once.
# Space Complexity: O(n) - In the worst case, we might store all elements in the set.


# Alternate Method Sorting

def containsDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False


# Time Complexity: O(n log n) - Sorting the list takes O(n log n) time, 
# and then we iterate through it once.
# Space Complexity: O(1) - We are sorting the list in place and using only a 
# constant amount of extra space for the loop.



"""

⚠️ Interview Discussion Points

If interviewer asks:

👉 “Which approach is better?”

Answer:

HashSet → faster (O(n))
Sorting → less space (sometimes preferred)
🧪 Variations They Can Ask
Return the duplicate number
Count duplicates
Find first duplicate
Remove duplicates


"""