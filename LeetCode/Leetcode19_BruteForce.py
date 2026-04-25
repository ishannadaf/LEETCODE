"""

19. Remove Nth Node From End of List

🧾 Problem Statement

Given a linked list, remove the n-th node from the end and return the head.

Input:
1 → 2 → 3 → 4 → 5,  n = 2

Output:
1 → 2 → 3 → 5


🐢 Brute Force Approach (Two Pass)
💡 Idea:
Count total nodes n_total
Find (n_total - n)th node
Remove it

"""

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


class SolutionBrute:
    def removeNthFromEnd(self, head, n):
        # Step 1: count length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # Step 2: remove (length - n)th node
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        for _ in range(length - n):
            curr = curr.next
        
        # delete node
        curr.next = curr.next.next
        
        return dummy.next
    
    
    
# 🧪 Test
arr = [1,2,3,4,5]
n = 2

head1 = build_list(arr)
head2 = build_list(arr)

res1 = SolutionBrute().removeNthFromEnd(head1, n)
# res2 = SolutionOptimal().removeNthFromEnd(head2, n)

print("Brute Force:")
print_list(res1)

# print("Optimal:")
# print_list(res2)

"""

Time: O(n) (2 passes)
Space: O(1)

"""