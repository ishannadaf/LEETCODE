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


🐢 Brute Force Approach (Using Extra Space)
💡 Idea:
Convert both linked lists → array
Merge + sort
Convert back → linked list

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


class Solution:
    def mergeTwoLists(self, l1, l2):
        arr = []
        
        while l1:
            arr.append(l1.val)
            l1 = l1.next
        
        while l2:
            arr.append(l2.val)
            l2 = l2.next
        
        arr.sort()
        
        dummy = ListNode(0)
        curr = dummy
        
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        
        return dummy.next


# 🧪 Testing
l1 = build_list([1, 2, 4])
l2 = build_list([1, 3, 4])

sol = Solution()
result = sol.mergeTwoLists(l1, l2)

print("Merged List:")
print_list(result)


# Time Complexity: O((n+m) log(n+m)) where n and m are lengths of l1 and l2 (due to sorting)
# Space Complexity: O(n+m) for the array and the new linked list 
