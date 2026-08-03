# Stack using Linked List
# A stack follows LIFO rule: Last In, First Out.
# In this implementation, the top of the stack is the first node of the linked list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackUsingLinkedList:
    def __init__(self):
        self.top = None

    def push(self, value):
        # Insert at the beginning of the linked list
        # This makes the new element the new top of the stack.
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        # Remove the top element from the stack
        if self.is_empty():
            return "Stack Underflow"
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def peek(self):
        # Return the top element without removing it
        if self.is_empty():
            return "Empty Stack"
        return self.top.value

    def is_empty(self):
        # Check whether the stack is empty
        return self.top is None


# Working of the code:
# 1. push(10) -> 10 becomes the top
# 2. push(20) -> 20 becomes the new top
# 3. push(30) -> 30 becomes the new top
# 4. peek() -> shows 30 (top element)
# 5. pop() -> removes 30
# 6. peek() -> shows 20

stack = StackUsingLinkedList()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())
print("Pop:", stack.pop())
print("Top element after pop:", stack.peek())
