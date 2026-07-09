class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def deletetheNode(self,head,X):
        temp = head

        while(temp.next is not None):
            temp = temp.next

            if(temp.next is X):
                temp.next.next = head

            return head 

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

object = Solution()
head = object.deletetheNode(head,30)
temp = head
while(temp is not None):
    print(temp.data,end="--")

    temp = temp.next
print("None")    
        