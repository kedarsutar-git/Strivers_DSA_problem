# Class representing a node in Doubly Linked List
class Node:
    # Constructor to initialize a node
    def __init__(self, data, next=None, prev=None):
        # Stores data of the node
        self.data = data

        # Pointer to the next node
        self.next = next

        # Pointer to the previous node
        self.prev = prev

# Initializing an array to create nodes
arr = [2, 5, 8, 7]

# Creating the head node of the doubly linked list
head = Node(arr[0])

# Printing the memory reference of head
print(head)

# Printing the data stored in head node
print(head.data)





