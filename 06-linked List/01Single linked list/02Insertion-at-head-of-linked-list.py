"""
Insert a Node at the Beginning of a Singly Linked List

You are given the head of a singly linked list and an integer `x`. Insert a
new node containing `x` at the beginning of the list and return the new head.

The new node must become the first node, while the order of all existing nodes
remains unchanged.

Example:
    Input:  head = 10 -> 20 -> 30 -> None, x = 50
    Output: 50 -> 10 -> 20 -> 30 -> None

Constraints:
    - The linked list may be empty.
    - `x` is an integer.
"""


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


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

object =Solution()
head = object.insertionAtHead(head,50)

# printing the linked list
current= head
while current is not None:
    print(current.data,end ="->")
    current = current.next

print("None")


'''
Time Complexity:O(n)
Space Complexity:O(1)

'''
