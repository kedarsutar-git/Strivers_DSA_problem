class StackQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if self.isEmpty():
            return "Queue Underflow"

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):
        if self.isEmpty():
            return "Queue Underflow"

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def isEmpty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

q = StackQueue()

