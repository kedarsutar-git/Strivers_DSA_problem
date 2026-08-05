class Stack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.isEmpty():
            return "Stack Underflow"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)


# Example
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print(s.pop())
print(s.peek())

'''
| Operation | Complexity     |
| --------- | -------------- |
| Push      | O(1) Amortized |
| Pop       | O(1)           |
| Peek      | O(1)           |
'''