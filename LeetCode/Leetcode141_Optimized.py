"""

141. Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by 
continuously following the next pointer. Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the first node.


⚡ Optimal Approach (Floyd’s Cycle Detection)
💡 Idea:

Use two pointers:

slow → moves 1 step
fast → moves 2 steps

👉 If cycle exists → they will meet

"""


class SolutionOptimal:
    def hasCycle(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    
    
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# 🔧 Create linked list with cycle
def create_cycle_list(arr, pos):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    nodes = [head]
    
    for x in arr[1:]:
        new_node = ListNode(x)
        curr.next = new_node
        curr = new_node
        nodes.append(new_node)
    
    # create cycle
    if pos != -1:
        curr.next = nodes[pos]
    
    return head


# 🧪 Test
head = create_cycle_list([1,2,3,4], 1)  # cycle at index 1

# print("Brute Force:", SolutionBrute().hasCycle(head))
print("Optimal:", SolutionOptimal().hasCycle(head))



"""

🎯 Key Concepts (VERY IMPORTANT)
Compare nodes, not values
Fast pointer catches slow pointer
Works like race in circle
🧠 One-Line Understanding

👉 If there is a loop, fast pointer will eventually meet slow pointer

🚨 Common Mistakes
Comparing val instead of node
Forgetting fast.next check → crash
Not understanding why pointers meet


🔥 Pattern Learned
👉 Fast & Slow Pointer (Floyd’s Algorithm)

Used in:
Cycle detection
Find middle node
Detect loop start (LeetCode 142)

"""
