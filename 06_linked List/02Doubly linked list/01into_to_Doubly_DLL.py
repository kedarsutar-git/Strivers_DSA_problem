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




class Node:
    def __init__(self,data,next = None,prv = None):
        self.data = data 
        self.next = next
        self.prv = prv

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)


node1.next = node2
node2.next = node3
node3.next = node4
head = node1
current = head

while(current is not None):
    print(current.data ,end = "->")

    current = current.next
print("None")

