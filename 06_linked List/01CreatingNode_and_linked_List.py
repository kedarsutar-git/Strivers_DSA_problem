class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
head = Node(10)
second = Node(20)
third = Node(30)

# Link nodes
head.next = second
second.next = third

# Traverse
temp = head

while temp:
    print(temp.data,end ="->")
    temp = temp.next

print("NULL")
