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

class SolutionOptimal:
    def deleteDuplicates(self, head):
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
    
arr = [1, 1, 2, 3, 3]


# 🐢 Optimal Test
head1 = build_list(arr)
sol1 = SolutionOptimal()
res1 = sol1.deleteDuplicates(head1)

print("Optimal Result:")
print_list(res1)

# Time Complexity: O(n) - We traverse the list once.
# Space Complexity: O(1) - We use constant extra space.


"""

🎯 Interview Insight
Brute = shows thinking
Optimal = shows efficiency
Always mention:
👉 "Since list is sorted, duplicates are adjacent"

"""