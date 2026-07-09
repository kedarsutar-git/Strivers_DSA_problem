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
    def SearchNode(self,head,val:int):
        temp = head 

        while(temp is not None):
            if(temp.data==val):
                return True

            temp = temp.next
        return False 
        
head = Node(10)        
head.next = Node(20)
head.next.next = Node(30)

object = Solution()
print(object.SearchNode(head,2))
