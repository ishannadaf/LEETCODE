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


🐢 Brute Force Approach (Count Length)
💡 Idea:
Count total nodes
Go to n//2 position

"""

class SolutionBrute:
    def middleNode(self, head):
        # Step 1: count length
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        # Step 2: go to middle
        mid = n // 2
        curr = head
        
        for _ in range(mid):
            curr = curr.next
        
        return curr
    
    
    
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

res1 = SolutionBrute().middleNode(head)
# res2 = SolutionOptimal().middleNode(head)

print("Brute Force Result:")
print_list(res1)

# print("Optimal Result:")
# print_list(res2)

# Time Complexity : O(n) 
# Space Complexity : O(1)