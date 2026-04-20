"""

167. Two Sum - Brute Force Solution
Given an array of integers nums and an integer target, return indices of the two numbers such that
they add up to target.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

"""

#Only Solution

def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        current_sum = numbers[l] + numbers[r]

        if current_sum == target:
            return [l + 1, r + 1]  # 1-based index
        elif current_sum < target:
            l += 1
        else:
            r -= 1
            
            
# Time Complexity: O(n) - We traverse the input array once with two pointers.
# Space Complexity: O(1) - We are using only a constant amount of space for the two pointers 
# and the current sum variable.


"""

🔥 Why This Is Powerful

👉 Compared to Two Sum:

Approach	    Time	Space
HashMap	        O(n)	O(n)
Two Pointer	    O(n)	O(1) ✅
⚠️ Common Mistakes
Forgetting 1-based indexing ❌
Moving wrong pointer
Using hashmap unnecessarily
🧠 Pattern Insight
👈👉 Sorted Array = Two Pointer

Whenever you see:

Sorted array
Pair / sum condition

👉 Think Two Pointers first

"""