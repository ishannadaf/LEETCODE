"""

🔹 LeetCode 160 – Intersection of Two Linked Lists
🧾 Problem Statement

Given two linked lists, return the node where they intersect.
If no intersection → return None.

Example:
List A: 1 → 2 → 3 \
                      → 7 → 8 → 9
List B:     4 → 5  /




🐢 Brute Force Approach
💡 Idea:
For each node in list A
Check every node in list B

👉 Compare node reference (not value)
"""

class SolutionBrute:
    def getIntersectionNode(self, headA, headB):
        currA = headA
        
        while currA:
            currB = headB
            while currB:
                if currA == currB:
                    return currA
                currB = currB.next
            currA = currA.next
        
        return None
    
    
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# 🔧 Create intersecting lists
def create_intersection():
    # common part
    common = ListNode(7)
    common.next = ListNode(8)
    common.next.next = ListNode(9)

    # list A
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)
    headA.next.next.next = common

    # list B
    headB = ListNode(4)
    headB.next = ListNode(5)
    headB.next.next = common

    return headA, headB


# 🧪 Test
headA, headB = create_intersection()

res1 = SolutionBrute().getIntersectionNode(headA, headB)
# res2 = SolutionBetter().getIntersectionNode(headA, headB)
# res3 = SolutionOptimal().getIntersectionNode(headA, headB)

print("Brute:", res1.val if res1 else None)
# print("Better:", res2.val if res2 else None)
# print("Optimal:", res3.val if res3 else None)


"""
Time: O(n + m)
Space: O(n)
"""
