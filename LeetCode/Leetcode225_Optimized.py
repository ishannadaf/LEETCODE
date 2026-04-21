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
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        # swap
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0
    
    
# Time Complexity: O(n) for push, O(1) for pop, top, and empty.
# Space Complexity: O(n) for the queue.


"""

push → O(n)
pop → O(1)
top → O(1)
⚡ Key Insight

We reverse queue order to simulate stack behavior

👉 Pattern:

Queue = FIFO
Stack = LIFO
→ We manipulate order to convert behavior

"""