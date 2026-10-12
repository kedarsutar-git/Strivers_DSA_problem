class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top is None:
            return "Stack Underflow"

        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            return "Stack is Empty"
        return self.top.data

    def isEmpty(self):
        return self.top is None

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Example
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
print(s.pop())

'''
| Operation | Complexity |
| --------- | ---------- |
| Push      | O(1)       |
| Pop       | O(1)       |

'''