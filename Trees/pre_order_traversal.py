"""
Docstring for Trees.pre_order_traversal

This module implements the Pre-Order Traversal algorithm for binary trees.
Pre-Order Traversal : A depth-first traversal method that visits the root node, the left
subtree, and then the right subtree recursively.
To implement the Pre-Order Traversal algorithm in a programming language, we need:
1. A binary tree structure with nodes containing data and pointers to left and right children.
2. A recursive function that performs the pre-order traversal.

"""

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)