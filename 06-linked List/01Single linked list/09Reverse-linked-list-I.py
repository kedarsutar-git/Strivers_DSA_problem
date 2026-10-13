'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
'''


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

        
class Solution:
    def ReverseLinkedList(self,head):
        arr = []
        current = head

        while(current is not None):
            arr.append(current.data)
            current = current.next

        i = 0
        j = len(arr) - 1

        while(i<j):
            arr[i],arr[j] = arr[j],arr[i]

            i += 1
            j -= 1

        current = head
        k = 0
        while(current is not None):
            current.data = arr[k]
            current = current.next
            k += 1

        return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

object = Solution()
result = object.ReverseLinkedList(head)

while result:
    print(result.data, end="->")
    result = result.next

'''
Time Complexity:O(n)
Space Complexity:O(n)

'''