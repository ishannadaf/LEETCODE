"""

🔹 LeetCode 143 – Reorder List
🧾 Problem Statement

Reorder a linked list:
👉 From:
L0 → L1 → L2 → L3 → L4

👉 To:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 ...


Example 1:
Input:
1 → 2 → 3 → 4 → 5

Output:
1 → 5 → 2 → 4 → 3


🐢 Brute Force Approach (Using Array)
💡 Idea:
Store nodes in array
Use two pointers (start & end)
Rebuild links

"""

class SolutionBrute:
    def reorderList(self, head):
        if not head:
            return
        
        nodes = []
        curr = head
        
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        i, j = 0, len(nodes) - 1
        
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            
            if i == j:
                break
            
            nodes[j].next = nodes[i]
            j -= 1
        
        nodes[i].next = None

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
arr = [1,2,3,4,5]

head1 = build_list(arr)
head2 = build_list(arr)

SolutionBrute().reorderList(head1)
# SolutionOptimal().reorderList(head2)

print("Brute:")
print_list(head1)

# print("Optimal:")
# print_list(head2)


"""

⏱ Complexity:
Time: O(n)
Space: O(n)

"""