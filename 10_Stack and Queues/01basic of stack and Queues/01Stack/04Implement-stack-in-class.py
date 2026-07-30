class Stack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Stack Underflow"

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return "Empty Stack"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.peek())      # 30
print(s.pop())       # 30
print(s.size())      # 2
print(s.is_empty())  # False