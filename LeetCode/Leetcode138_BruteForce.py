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


🐢 Brute Force Approach (HashMap)
💡 Idea:
Create copy of each node
Store mapping: original → copy
Assign next and random using map

"""

class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class SolutionBrute:
    def copyRandomList(self, head):
        if not head:
            return None
        
        old_to_new = {}
        
        # Step 1: create all nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        # Step 2: assign next & random
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
        
        return old_to_new[head]




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
res1 = SolutionBrute().copyRandomList(head)
# res2 = SolutionOptimal().copyRandomList(head)

print("Brute Copy:")
print_list(res1)

# print("Optimal Copy:")
# print_list(res2)


"""
⏱ Complexity:
Time: O(n)
Space: O(n)
"""

