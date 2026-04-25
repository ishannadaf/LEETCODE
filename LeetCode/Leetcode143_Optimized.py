"""

🔹 LeetCode 143 – Reorder List
🧾 Problem Statement

Reorder a linked list:
👉 From:
L0 → L1 → L2 → L3 → L4

👉 To:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 ...


Example 1:
Input:
1 → 2 → 3 → 4 → 5

Output:
1 → 5 → 2 → 4 → 3


⚡ Optimal Approach (3 Steps – VERY IMPORTANT)
💡 Idea:
Find middle
Reverse second half
Merge both halves

"""

class SolutionOptimal:
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # Step 1: find middle
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: reverse second half
        prev = None
        curr = slow.next
        slow.next = None
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: merge two halves
        first = head
        second = prev
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2

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
arr = [1,2,3,4,5]

head1 = build_list(arr)
head2 = build_list(arr)

# SolutionBrute().reorderList(head1)
SolutionOptimal().reorderList(head2)

print("Brute:")
print_list(head1)

# print("Optimal:")
# print_list(head2)


"""

⏱ Complexity:
Time: O(n)
Space: O(1)




🎯 Key Concepts (VERY IMPORTANT)
Split list (fast/slow)
Reverse second half
Merge alternating
🧠 One-Line Understanding

👉 Split → Reverse → Merge

🚨 Common Mistakes
Forgetting slow.next = None → creates cycle ❌
Merging incorrectly
Losing pointers
🔥 Patterns Combined (VERY POWERFUL)

👉 Fast & Slow Pointer
👉 Reverse Linked List
👉 Merge Two Lists
"""