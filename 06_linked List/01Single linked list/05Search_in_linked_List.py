'''
Input: 0->1->2, val = 2
Output: True
Explanation: Since element 2 is present in the list, return true.

Input: 12->5->8->7, val = 6 
Output: False
Explanation: The list does not contain element 6. Therefore, return false.

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def SearchInLL(self,head,val:int):
        current = head   
        while current is not None:
            if(current.data==val):
                return True
            current = current.next  # Move in the next node 
        return False
         
        


        
