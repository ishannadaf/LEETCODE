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



🐢 Brute Force Approach (Using Array)
💡 Idea:
Store values in array
Check if array == reversed array
"""


class SolutionBrute:
    def isPalindrome(self, head):
        arr = []
        curr = head
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        return arr == arr[::-1]



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

print("Brute:", SolutionBrute().isPalindrome(head1))
# print("Optimal:", SolutionOptimal().isPalindrome(head2))


"""

⏱ Complexity:
Time: O(n)
Space: O(n)

"""