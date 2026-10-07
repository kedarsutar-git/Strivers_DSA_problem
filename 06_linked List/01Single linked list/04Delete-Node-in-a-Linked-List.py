
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

        