'''
Given the head of a singly linked list, delete the tail of the linked list and return the head of the modified list.

The tail is the last node of the linked list.

Example 1:
Input: linkedList = [1, 2, 3]

Output: [1, 2]

Explanation:

The last node was removed

Example 2:
Input: linkedList = [1]

Output: []

Explanation:

Note that the value of head is null here.
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def DeleteLastNode(self,head):
        if(head is None):
            return None

        if(head.next is None):
            return None

        current = head
        while(current.next.next is not None):
            current = current.next

        current.next = None

        return head

head = Node(20)
head.next = Node(30)
head.next.next = Node(40)
head.next.next.next = Node(50)

object = Solution()
head = object.DeleteLastNode(head)

temp = head
while(temp is not None):
    print(temp.data,end = "->")
    temp = temp.next

print(None)


