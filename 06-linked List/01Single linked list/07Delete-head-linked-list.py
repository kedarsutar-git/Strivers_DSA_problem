"""
Delete the Head of a Singly Linked List

You are given the head of a singly linked list. Delete its first node and
return the head of the updated list.

If the linked list is empty or contains only one node, return `None`.

Example:
    Input:  head = 10 -> 20 -> 30 -> 40 -> None
    Output: 20 -> 30 -> 40 -> None
    Explanation: The node containing `10` is removed.

Constraints:
    - The linked list may be empty.
    - Node values are integers.
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def deleteHead(self,head):
        if(head is None):
            return None

        if(head.next is None):
            return None


        return head.next   # Return the second Node of the linked list


head = Node(10)
head.next  = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)


object = Solution()
head = object.deleteHead(head)
temp = head

while(temp is not None):
    print(temp.data,end ="->")

    temp = temp.next

print(None)

'''
Time Complexity:O(1)
Sapce Complexity:O(1)

'''
