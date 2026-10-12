'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list
that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]


Example 2:

Input: head = [], val = 1
Output: []


Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
'''
class Node:
    def __init__(self,data,val=0):
        self.data = data
        self.next = None

class Solution:
    def RemoveElement(self,head,Val:int):
        dummy = Node(0)

        dummy.next = head

        temp = dummy

        while(temp.next is not None):
            if(temp.next.val== Val):
                temp.next = temp.next.next

            else:
                temp = temp.next

        return dummy.next
                       
'''
Time Complexity:O(n)
Space Complexity:O(1)

'''                       