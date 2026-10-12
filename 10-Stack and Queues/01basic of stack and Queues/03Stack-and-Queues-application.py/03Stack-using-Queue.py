from collections import deque


class Stack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        if not self.q:
            return "Empty"
        return self.q.popleft()

    def peek(self):
        if not self.q:
            return "Empty"
        return self.q[0]


# Example
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.pop())
print(s.peek())