"""

232. Implement Queue using Stacks
Implement a first in first out (FIFO) queue using only two stacks.
Example:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

"""

class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x):
        self.inStack.append(x)

    def pop(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

        return self.outStack.pop()

    def peek(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

        return self.outStack[-1]

    def empty(self):
        return not self.inStack and not self.outStack
    
    
# Time Complexity: O(1) for push, O(n) for pop and peek in the worst case when outStack is empty, 
# O(1) for empty.
# Space Complexity: O(n) for the stacks.


"""

💡 Intuition (VERY IMPORTANT 🔥)

👉 Use two stacks:

inStack → for push
outStack → for pop
🔥 Key Idea:
Push always goes to inStack
When popping:
If outStack is empty → move all from inStack
Else → just pop

👉 This is called lazy transfer


⚡ Key Insight (VERY IMPORTANT)

Reverse order only when needed

👉 Pattern:

Two stacks → reverse order
Lazy transfer → optimize operations

"""