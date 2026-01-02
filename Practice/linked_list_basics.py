
def SingleLinkedList():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
        
    node1 = Node(3)
    node2 = Node(5)
    node3 = Node(13)
    node4 = Node(2)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    currentNode = node1
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def DoubleLinkedList():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
        
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)

    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3

    currentNode = node1
    while currentNode:
        print(currentNode.data, end=" <-> ")
        currentNode = currentNode.next
    print("null")
    
def CircularLinkedList():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    node1 = Node(7)
    node2 = Node(14)
    node3 = Node(21)
    node4 = Node(28)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1  # Making it circular

    currentNode = node1
    count = 0
    while count < 8:  # Print two cycles to demonstrate circularity
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
        count += 1
    print("(back to head)")

def CircularDoubleLinkedList():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
        
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3
    node4.next = node1  # Making it circular
    node1.prev = node4  # Making it circular

    currentNode = node1
    count = 0
    while count < 8:  # Print two cycles to demonstrate circularity
        print(currentNode.data, end=" <-> ")
        currentNode = currentNode.next
        count += 1
    print("(back to head)")
