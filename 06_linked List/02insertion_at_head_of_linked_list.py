class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def insertionAtHead(self,head,x:int):
        # Create new node
        newNode = Node(x)

        # Point new node to current head
        newNode.next = head

        # Move head to new node
        head = newNode
        return head

