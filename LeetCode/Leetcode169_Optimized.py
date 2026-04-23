"""

169. Majority Element
Given an array nums of size n, return the majority element. 
The majority element is the element that appears more than ⌊n / 2⌋ times in the array. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2


🧠 Approach 2 — HashMap (Better)
💡 Idea
Count frequency using dictionary
Return element with max count

"""

def majorityElement(nums):
    count = {}
    
    for num in nums:
        count[num] = count.get(num, 0) + 1
        
        if count[num] > len(nums) // 2:
            return num

# Time Complexity: O(n) where n is the length of the input array nums 
# (due to single loop and dictionary operations)
# Space Complexity: O(n) in the worst case if all elements are unique 
# (due to dictionary storing counts of each element)


"""

🚀 Approach 3 — Optimal (Boyer-Moore Voting Algorithm)
💡 Key Insight 🔥

👉 Majority element dominates the array
👉 It can cancel out all other elements

🧠 Core Idea
Maintain:
candidate
count
If count = 0 → pick new candidate
If same → increment
Else → decrement


"""


def majorityElement(nums):
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate


# Time Complexity: O(n) where n is the length of the input array nums (due to single loop)
# Space Complexity: O(1) since we are using only a constant amount of extra space

"""

🎯 Pattern

👉 Voting Algorithm / Greedy

⚠️ Common Mistakes
Not resetting candidate when count = 0 ❌
Confusing with max frequency ❌
🔥 Interview Tip (IMPORTANT)

Say this line:

👉 “Majority element cancels out all other elements, so it survives”

That’s the intuition behind Boyer-Moore.

✅ Follow-up (VERY IMPORTANT)

👉 What if majority element is not guaranteed?

Answer:

Run algorithm → get candidate
Do second pass → verify if candidate is actually majority

"""