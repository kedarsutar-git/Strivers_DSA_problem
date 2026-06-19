class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def InsertionAtEnd(self,head,x:int):
        newnode = Node(x)

        if(head is None):
            return newnode
        
        current = head

        while current.next is not None:
            current = current.next

        current.next = newnode 

        return head   

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Insert at end
obj = Solution()
head = obj.InsertionAtEnd(head, 50)

# Print linked list
temp = head

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
