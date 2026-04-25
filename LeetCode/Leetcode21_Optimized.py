"""

21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new sorted list. The new list should be made 
by splicing together the nodes of the first two lists. 

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]


⚡ Optimal Approach (Two Pointers – MOST IMPORTANT)
💡 Idea:

Compare nodes one by one and attach smaller one.

🧠 Steps:
Create a dummy node
Use pointer curr
Compare l1.val and l2.val
Attach smaller node
Move that pointer
At end, attach remaining list

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


# 🚀 Optimal Solution
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        
        # attach remaining
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        
        return dummy.next


# 🧪 Testing
l1 = build_list([1, 2, 4])
l2 = build_list([1, 3, 4])

sol = Solution()
result = sol.mergeTwoLists(l1, l2)

print("Merged List:")
print_list(result)


# Time Complexity: O(n + m) where n and m are lengths of l1 and l2
# Space Complexity: O(1) - We are merging in-place without using extra space for