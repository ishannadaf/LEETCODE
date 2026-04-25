"""

142. Linked List Cycle II
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


⚡ Optimal Approach (Floyd’s Algorithm – MAGIC PART)
💡 Idea:
Detect cycle (like 141)
When slow == fast
Move one pointer to head
Move both 1 step → meeting point = cycle start
🧠 Why this works (IMPORTANT)

👉 Distance math:

Let:
L = distance before cycle
C = cycle length

After meeting:

Moving both pointers → they meet at cycle start

👉 Don’t memorize — just remember:
reset one pointer to head

"""

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


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
    
    if pos != -1:
        curr.next = nodes[pos]
    
    return head



class SolutionOptimal:
    def detectCycle(self, head):
        slow = head
        fast = head
        
        # Step 1: detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            return None  # no cycle
        
        # Step 2: find start
        slow = head
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow



# 🧪 Test
head = create_cycle_list([1,2,3,4,5], 1)  # cycle at node with value 2

# res1 = SolutionBrute().detectCycle(head)
res2 = SolutionOptimal().detectCycle(head)

# print("Brute Force Cycle Start:", res1.val if res1 else None)
print("Optimal Cycle Start:", res2.val if res2 else None)


"""

🎯 Key Takeaways (VERY IMPORTANT)
Phase 1: detect cycle
Phase 2: reset pointer to head
Move both → meet at start
🧠 One-Line Understanding

👉 After collision, moving both pointers equally leads to cycle start

🔥 Pattern You Learned

👉 Advanced Fast & Slow Pointer
👉 Mathematical pointer reasoning

"""