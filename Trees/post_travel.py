"""
Docstring for Trees.post_travel

This module implements the Post-Order Traversal algorithm for binary trees.
Post-Order Traversal : A depth-first traversal method that visits the left subtree, the right
subtree, and then the root node recursively.
To implement the Post-Order Traversal algorithm in a programming language, we need:
1. A binary tree structure with nodes containing data and pointers to left and right children.
2. A recursive function that performs the post-order traversal.

"""

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")