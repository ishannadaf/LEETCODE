"""

876. Middle of the Linked List
🧾 Problem Statement

Given the head of a linked list, return the middle node.

👉 If there are two middle nodes, return the second one


Example 1:
Input:
1 → 2 → 3 → 4 → 5
Output:
3 → 4 → 5

Example 2:
Input:
1 → 2 → 3 → 4 → 5 → 6
Output:
4 → 5 → 6   (second middle)


⚡ Optimal Approach (Fast & Slow Pointer)
💡 Idea:
slow → 1 step
fast → 2 steps

👉 When fast reaches end → slow is at middle
"""

class SolutionOptimal:
    def middleNode(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = ListNode(x)
        curr = curr.next
    return head


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# 🧪 Test
head = build_list([1,2,3,4,5,6])

# res1 = SolutionBrute().middleNode(head)
res2 = SolutionOptimal().middleNode(head)

# print("Brute Force Result:")
# print_list(res1)

print("Optimal Result:")
print_list(res2)

# Time Complexity : O(n) 
# Space Complexity : O(1)


"""

🎯 Key Concepts
Fast moves 2x → reaches end faster
Slow ends exactly at middle
Works for both odd & even length
🧠 One-Line Understanding

👉 Fast pointer reaches end, slow pointer reaches middle

🔥 Pattern Reinforced

👉 Fast & Slow Pointer (again — VERY IMPORTANT)



#=======================================================================================================

You're right:
👉 In LeetCode 876, both brute force and optimal have O(n) time and O(1) space

So… what’s the real difference? 🤔

🎯 Core Answer (Important)

👉 Difference is NOT always about Big-O
👉 It’s about:

Number of passes
Efficiency in practice
Pattern recognition
🔍 Let’s Compare Properly
🐢 Brute Force (Count + Traverse)
Steps:
Traverse list → count nodes
Traverse again → reach middle

👉 Total = 2 passes

⚡ Optimal (Fast & Slow Pointer)
Steps:
Traverse list once using 2 pointers

👉 Total = 1 pass

📊 Real Difference
Aspect	Brute Force	Optimal
Passes	2	1
Time Complexity	O(n)	O(n)
Space	O(1)	O(1)
Efficiency	Slightly slower	Better
Interview Value	Basic	Strong pattern
🧠 Why Optimal is Preferred

Even though Big-O is same:

👉 Brute Force does more work

Traverses list twice
More operations internally

👉 Optimal is smarter

Uses pointer logic
Solves in one traversal
🔥 Interview Insight (VERY IMPORTANT)

If you say:

"Both are O(n), so same"

❌ That’s incomplete

Better answer:

"Both are O(n), but optimal is better because it reduces traversal to a single pass using fast and slow pointers"

👉 This shows depth of understanding

🧪 Simple Analogy

Think of finding middle of a road:

Brute force → walk full road, count steps, go back to middle 🚶‍♂️🚶‍♂️
Optimal → one person walks normal, one runs fast 🏃‍♂️ → middle found instantly
💡 When Big-O is Same, Still Choose Optimal If:
Fewer passes
Cleaner logic
Uses known pattern (like fast/slow)
🔥 Final Takeaway

👉 Optimal ≠ always better Big-O
👉 Sometimes it means:

fewer operations
better technique
interview-level thinking



"""