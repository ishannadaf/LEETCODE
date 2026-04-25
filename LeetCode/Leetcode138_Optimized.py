"""

138. Copy List with Random Pointer
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.


Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]


⚡ Optimal Approach (O(1) Space – VERY IMPORTANT)
💡 Idea (3 Steps):
Insert copied nodes in between original nodes
Set random pointers
Separate the lists
"""

class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class SolutionOptimal:
    def copyRandomList(self, head):
        if not head:
            return None
        
        # Step 1: insert copy nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        
        # Step 2: assign random
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Step 3: separate lists
        curr = head
        new_head = head.next
        
        while curr:
            copy = curr.next
            curr.next = copy.next
            
            if copy.next:
                copy.next = copy.next.next
            
            curr = curr.next
        
        return new_head




def print_list(head):
    curr = head
    while curr:
        rand = curr.random.val if curr.random else None
        print(f"[Val: {curr.val}, Random: {rand}]", end=" -> ")
        curr = curr.next
    print("None")


# 🧪 Create test list
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

n1.random = n3
n2.random = n1
n3.random = n2

head = n1

# Test
# res1 = SolutionBrute().copyRandomList(head)
res2 = SolutionOptimal().copyRandomList(head)

# print("Brute Copy:")
# print_list(res1)

print("Optimal Copy:")
print_list(res2)


"""
⏱ Complexity:
Time: O(n)
Space: O(1)
"""

