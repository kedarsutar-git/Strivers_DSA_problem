"""
Delete a Node by Value in a Singly Linked List

You are given the head of a singly linked list and an integer `x`. Delete the
first node whose value is equal to `x`, then return the head of the updated
linked list.

If `x` is not present, return the original list unchanged. If the list is
empty, return `None`.

Example:
    Input:  head = 10 -> 20 -> 30 -> None, x = 30
    Output: 10 -> 20 -> None

Constraints:
    - The linked list may be empty.
    - Node values and `x` are integers.
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution:
    def DeleteNode(self,head,x):

        if(head is None):
            return None
        
        # if head itself needs to be deleted

        if(head.data == x):
            return head.next
        
        temp = head
        while(temp.next is not None):
            if(temp.next.data==x):
                temp.next = temp.next.next
                return head

            temp = temp.next

        return head 

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

object = Solution()
head = object.DeleteNode(head,30)
temp = head
while(temp is not None):
    print(temp.data,end = "--")

    temp = temp.next

print("None")    

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''

        
