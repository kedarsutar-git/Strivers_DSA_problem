'''
Given the head of a singly linked list and an integer k, delete the kth node of the linked list and return the head of the modified list.

Example 1:
Input: linkedList = [3, 4, 5], k = 2

Output: linkedList = [3, 5]

Explanation:

The 2nd node with value 4 was removed.

Example 2:
Input: linkedList = [1, 2, 3], k = 1

Output: [2, 3]

Explanation:

The 1st Node was removed, note that the value of the head has changed.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    def deleteKthNode(self,head,k):
        if(k==1):
            return head.next

        prev = None
        count = 1
        temp = head
        while(temp is not None and count<k):
            prev = temp
            temp = temp.next
            count += 1

        prev.next = temp.next   

        return head 

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

object = Solution()
head = object.deleteKthNode(head,2)

temp = head
while(temp is not None):
    print(temp.data,end="->")
    temp = temp.next

print(None)


'''
Time Complexity:O(n)
Space Complexity:O(1)

'''