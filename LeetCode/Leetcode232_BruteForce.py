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
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        while self.s1:
            self.s2.append(self.s1.pop())

        val = self.s2.pop()

        while self.s2:
            self.s1.append(self.s2.pop())

        return val

    def peek(self):
        while self.s1:
            self.s2.append(self.s1.pop())

        val = self.s2[-1]

        while self.s2:
            self.s1.append(self.s2.pop())

        return val

    def empty(self):
        return len(self.s1) == 0
    
    
# Time Complexity: O(n) for pop and peek, O(1) for push and empty.
# Space Complexity: O(n) for the stacks.