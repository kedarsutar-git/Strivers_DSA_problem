'''
Example 1

Input: head = [1, 2, 3], X = 3

Output: head = [3, 1, 2, 3]

Explanation: 3 was added before the 1st node. Note that the head's value is changed.
'''

class Node:
    def __int__(self,data,next,prev):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def Insertion(self,head,X:int):
        Newnode = Node(X) 
        Newnode.next = head

        if(head):
            head.prev = Newnode

        return Newnode




            
