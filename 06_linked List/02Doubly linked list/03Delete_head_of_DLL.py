'''
Example 1
Input: doublyLinkedList = [1, 2, 3]
Output: [2, 3]

Explanation:
The node with value 1 was removed.



Example 2
Input: doublyLinkedList = [7]
Output: [ ]

Explanation:
Note that the head has null value after the removal.

'''
class Node:
    def __init(self,data,prev,next):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def DeleteHead(self,head):
        if(not head):
            return None 

        head= head.next

        if(head is not None):
            head.prev = None

        return head            