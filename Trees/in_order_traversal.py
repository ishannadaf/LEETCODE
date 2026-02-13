
"""
Docstring for Trees.in_order_traversal

This module implements the In-Order Traversal algorithm for binary trees.
In-Order Traversal : A depth-first traversal method that visits the left subtree, the root node, and then the right subtree recursively.
To implement the In-Order Traversal algorithm in a programming language, we need:
1. A binary tree structure with nodes containing data and pointers to left and right children.
2. A recursive function that performs the in-order traversal.

"""

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)