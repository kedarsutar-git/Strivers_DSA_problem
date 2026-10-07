"""
Insert a Node at the End of a Singly Linked List

You are given the head of a singly linked list and an integer `x`. Insert a
new node containing `x` at the end of the list and return the head of the
updated list.

If the linked list is empty, the new node becomes the head.

Example:
    Input:  head = 10 -> 20 -> 30 -> None, x = 50
    Output: 10 -> 20 -> 30 -> 50 -> None

Constraints:
    - The linked list may be empty.
    - `x` is an integer.
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def InsertionAtEnd(self,head,x:int):
        newnode = Node(x)

        if(head is None):
            return newnode
        
        current = head

        while current.next is not None:
            current = current.next

        current.next = newnode 

        return head   

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Insert at end
obj = Solution()
head = obj.InsertionAtEnd(head, 50)

# Print linked list
temp = head

while(temp is not None):
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")





        



        
