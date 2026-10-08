class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


node1 = Node(12)
node2 = Node(29)
node3 = Node(34)
node4 = Node(45)

node1.next = node2
node2.next = node3
node3.next = node4

current = node1
while(current is not None):  # Move the 
    print(current.data,end = "->")
    
    current = current.next

print(None)
