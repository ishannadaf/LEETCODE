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



class SolutionBrute:
    def detectCycle(self, head):
        visited = set()
        curr = head
        
        while curr:
            if curr in visited:
                return curr   # cycle start
            visited.add(curr)
            curr = curr.next
        
        return None



# 🧪 Test
head = create_cycle_list([1,2,3,4,5], 1)  # cycle at node with value 2

res1 = SolutionBrute().detectCycle(head)
# res2 = SolutionOptimal().detectCycle(head)

print("Brute Force Cycle Start:", res1.val if res1 else None)
# print("Optimal Cycle Start:", res2.val if res2 else None)