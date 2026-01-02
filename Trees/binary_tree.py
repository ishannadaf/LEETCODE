"""
Docstring for Trees.binary_tree

This module defines a simple binary tree structure with nodes and demonstrates
how to create a tree and access its elements.
Binary Tree : A tree data structure in which each node has at most two children, referred to as the left child and the right child.
To implement a binary tree in a programming language, we need:
1. A Node class to represent each node in the tree, containing data and pointers to left
    and right children.
2. A way to create nodes and link them together to form the tree structure.


"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Test
print("root.right.left.data:", root.right.left.data)


# Time Complexity: O(1) for accessing nodes directly
# Space Complexity: O(n) where n is the number of nodes in the tree