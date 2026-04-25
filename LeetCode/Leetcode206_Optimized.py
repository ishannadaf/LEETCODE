"""

206. Reverse Linked List - Brute Force
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []



⚡ Optimal Approach (Iterative – In-place)
💡 Idea:

Reverse pointers one by one.

🔁 Steps:
Maintain 3 pointers:
prev → previous node
curr → current node
next → next node
"""

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next   # store next
            curr.next = prev        # reverse link
            prev = curr             # move prev
            curr = next_node        # move curr
        
        return prev
    

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr):
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


head = build_list([1,2,3,4,5])
sol = Solution()
new_head = sol.reverseList(head)
print_list(new_head)

# Time Complexity: O(n) - We traverse the linked list once.
# Space Complexity: O(1) - We only use a constant amount of space for the pointers.



#🔥 Recursive Approach (Important for Interviews)

#💡Idea:
#Reverse rest of the list, then fix current node.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        
        return new_head
    
    
head = build_list([1,2,3,4,5])
sol = Solution()
new_head = sol.reverseList(head)
print_list(new_head)


"""

🎯 Key Points (VERY IMPORTANT)
Iterative is most preferred in interviews
Recursive shows deep understanding
Always remember: reverse link = curr.next = prev

"""