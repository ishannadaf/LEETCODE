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



🐢 Brute Force Approach (Using Extra Space)
💡 Idea:
Store all values in an array
Reverse the array
Rebuild the linked list

"""

class Solution:
    def reverseList(self, head):
        vals = []
        curr = head
        
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            curr.val = vals.pop()
            curr = curr.next
        
        return head
    

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

# Time Complexity: O(n) - We traverse the linked list twice (once to store values and once to rebuild the list).
# Space Complexity: O(n) - We use an extra array to store the values of the linked list.