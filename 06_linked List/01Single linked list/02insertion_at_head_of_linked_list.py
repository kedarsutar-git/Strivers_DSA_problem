class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def insertionAtHead(self,head,x:int):
        # Create new node
        newNode = Node(x)

        # Point new node to current head
        newNode.next = head

        # Move head to new node
        head = newNode
        return head


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

object =Solution()
head = object.insertionAtHead(head,50)

# printing the linked list
current= head
while current is not None:
    print(current.data,end ="->")
    current = current.next

print("None")


'''
Time Complexity:O(n)
Space Complexity:O(1)

'''
