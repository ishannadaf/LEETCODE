"""
LeetCode 15: 3Sum - Brute Force Solution
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

"""

# For brute force, we can use three nested loops to check all possible triplets in the array and 
# see if they sum up to zero.
# So, instead of 3 loops we will use directly opimal solution which is 2 pointer approach

def threeSum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        # skip duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            total = nums[i] + nums[l] + nums[r]

            if total == 0:
                result.append([nums[i], nums[l], nums[r]])

                # skip duplicates
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1

                l += 1
                r -= 1

            elif total < 0:
                l += 1
            else:
                r -= 1

    return result


print(threeSum([0,0,0,0]))  # Output: [[0, 0, 0]]


# Time Complexity: O(n^2) - We have an outer loop that runs n times and an inner while loop 
# that can run up to n times in the worst case.
# Space Complexity: O(n) - We are storing the result in a new list that can take up to O(n) 
# space in the worst case when all triplets are unique. The sorting step also takes O(n log n) time, 
# but it does not affect the overall time complexity of O(n^2).


"""

🔥 Key Concepts (VERY IMPORTANT)
1. Sorting + Two Pointer Combo

👉 Most powerful pattern in interviews

2. Duplicate Handling ⭐

This is where most people fail:

if i > 0 and nums[i] == nums[i-1]:
    continue

AND

while nums[l] == nums[l+1]:
3. Reduce Problem

👉 3Sum → 2Sum
👉 4Sum → 3Sum

⚠️ Common Mistakes
Not sorting ❌
Forgetting duplicates ❌
Infinite loop due to pointer issues ❌
🧪 Variations (VERY IMPORTANT)
3Sum closest
4Sum
Count triplets
Triplets with target ≠ 0

"""