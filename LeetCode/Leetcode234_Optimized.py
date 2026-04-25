"""

🔹 LeetCode 234 – Palindrome Linked List
🧾 Problem Statement

Given a linked list, check if it is a palindrome.

👉 Same forward and backward

Example 1:
Input:
1 → 2 → 2 → 1

Output:
True

Example 2:
Input:
1 → 2 → 3

Output:
False



⚡ Optimal Approach (Reverse Second Half)
💡 Idea:
Find middle (fast/slow)
Reverse second half
Compare both halves
"""


class SolutionOptimal:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # Step 1: find middle
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: reverse second half
        prev = None
        curr = slow
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: compare
        first = head
        second = prev
        
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True


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


# 🧪 Test
arr = [1,2,2,1]

head1 = build_list(arr)
head2 = build_list(arr)

# print("Brute:", SolutionBrute().isPalindrome(head1))
print("Optimal:", SolutionOptimal().isPalindrome(head2))


"""

⏱ Complexity:
Time: O(n)
Space: O(1)

"""