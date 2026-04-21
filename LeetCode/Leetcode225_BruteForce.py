"""

225. Implement Stack using Queues
Implement a last-in-first-out (LIFO) stack using only two queues.

Example:
Input
["MyStack", "push", "top", "pop", "empty"]
[[], [1], [2], [2], []]
Output
[null, null, 2, 2, false]


"""

from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        # rotate previous elements
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0
    
    
# Time Complexity: O(n) for push, O(1) for pop, top, and empty.
# Space Complexity: O(n) for the queue.