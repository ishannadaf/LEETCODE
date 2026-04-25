"""

83. Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]



💡 Core Idea (VERY SIMPLE)

👉 Since list is sorted, duplicates will always be adjacent

So:

Compare curr.val with curr.next.val
If same → skip node
Else → move forward

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 🔧 Helper: Build Linked List from array
def build_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    
    for x in arr[1:]:
        curr.next = ListNode(x)
        curr = curr.next
    
    return head


# 🔧 Helper: Print Linked List
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

class SolutionBrute:
    def deleteDuplicates(self, head):
        if not head:
            return None
        
        values = []
        curr = head
        
        # collect unique values
        while curr:
            if not values or values[-1] != curr.val:
                values.append(curr.val)
            curr = curr.next
        
        # rebuild list
        dummy = ListNode(0)
        curr = dummy
        
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next
    
    
arr = [1, 1, 2, 3, 3]


# 🐢 Brute Force Test
head1 = build_list(arr)
sol1 = SolutionBrute()
res1 = sol1.deleteDuplicates(head1)

print("Brute Force Result:")
print_list(res1)


# Time Complexity: O(n) to traverse list + O(n) to build new list → O(n)
# Space Complexity: O(n) for values array + O(n) for new list → O(n)