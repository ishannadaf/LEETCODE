
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

def search(node, target):
    if node is None:
        return None 
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

def insert(node, data):
    if node is None:
        return TreeNode(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node


# Insert new nodes
insert(root, 10)
insert(root, 20)
# Traverse
inOrderTraversal(root)

# Time Complexity: O(h) where h is the height of the tree in average case for balanced BST, 
#                        O(n) in worst case for unbalanced BST. where n is number of nodes
# Space Complexity: O(h) due to recursion stack in average case for balanced BST, 
#                        O(n) in worst case for unbalanced BST. Where n is number of nodes


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

val = minValueNode(root)
print(f"\nMinimum value in the BST: {val.data}")
# Time Complexity: O(h) where h is the height of the tree in average case for balanced BST, 
#                        O(n) in worst case for unbalanced BST. where n is number of nodes
# Space Complexity: O(1) as we are using iterative approach.

def maxValueNode(node):
    current = node
    while current.right is not None:
        current = current.right
    return current

val = maxValueNode(root)
print(f"\nMaximum value in the BST: {val.data}")
# Time Complexity: O(h) where h is the height of the tree in average case for balanced BST,
#                        O(n) in worst case for unbalanced BST. where n is number of nodes
# Space Complexity: O(1) as we are using iterative approach.

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root

# Delete a node
root = deleteNode(root, 7)
print("In-order Traversal after deletion:")
inOrderTraversal(root)
# Time Complexity: O(h) where h is the height of the tree in average case for balanced BST,
#                        O(n) in worst case for unbalanced BST. where n is number of nodes
# Space Complexity: O(h) due to recursion stack in average case for balanced BST,
#                        O(n) in worst case for unbalanced BST. Where n is number of nodes

def findHeight(node):
    if node is None:
        return -1
    else:
        left_height = findHeight(node.left)
        right_height = findHeight(node.right)
        return max(left_height, right_height) + 1

height = findHeight(root)
print(f"\nHeight of the BST: {height}")

# Time Complexity: O(n) where n is number of nodes as we visit each node once.
# Space Complexity: O(h) due to recursion stack in average case for balanced BST,
#                        O(n) in worst case for unbalanced BST. Where n is number of nodes.