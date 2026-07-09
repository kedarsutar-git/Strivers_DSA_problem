'''
Example 1
Input: head = [10, 20, 30]
Output: [30, 20, 10]


Example 2
Input: head = [1, 3, 5, 7, 9]
Output: [9, 7, 5, 3, 1]
'''

class Node:
    def __init__(self,data,prev,next):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def ReverseDll(self,head):
        # for empty and single Dll
        if(head is None or head.next is None):
            return head
        
        current = head
        temp = None

        while(current is not None):
            # swap the prev and next
            temp = current.prev
            current.prev = current.next
            current.next = temp
            
            # move in next node 
            current = current.prev
        
        # new head
        return temp.prev

