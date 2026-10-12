'''
Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]


Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]


Example 3:

Input: head = []
Output: []
'''

class Node:
    def __init__(self,data,val = 0):
        self.data = data
        self.next = None

class Solution:
    def SortLL(self,head):

        if(temp is None):
            return None
        
        temp = head 
        arr = []

        while(temp is not None):
            arr.append(temp.val)

            temp = temp.next

        arr.sort()
        temp = head 
        i = 0
        while(temp is not None):
            temp.val = arr[i]

            i+=1
            temp = temp.next

        return head 


        