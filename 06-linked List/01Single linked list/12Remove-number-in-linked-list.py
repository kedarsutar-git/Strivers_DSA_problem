'''
Given the head of a singly linked list and an integer X, delete the node with value X and return the head of the modified list.

Example 1:
Input: linkedList = [3, 4, 5], X = 5

Output: [3, 4]

Explanation:

The node with value 5 was removed.

Example 2:
Input: linkedList = [3, 4, 5], X = 7

Output: [3, 4, 5]

Explanation:

No nodes were removed.
'''



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def deleteNodeWithValueX(self,head,X):
        if(head is not None and head.data==X):
            return head.next

        temp = head
        while(temp is not None and temp.next is not None):
            if(temp.next.data==X):
                temp.next = temp.next.next

                return head 
            temp = temp.next

        return head
    


head = Node(1)
head.next = Node(9)
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(3)

obj = Solution()
result = obj.deleteNodeWithValueX(head, 4)

while result is not None:
    print(result.data, end=" -> ")
    result = result.next

print("None")


'''
Time Complexity:O(n)
Space Complexity:O(1)

'''