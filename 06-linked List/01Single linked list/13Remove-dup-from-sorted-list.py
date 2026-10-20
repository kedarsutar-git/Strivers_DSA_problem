'''
ou are given the head of a sorted linked list.

Delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''
# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        dummy = Node(0)
        dummy.next = head

        prev = dummy
        temp = head

        while(temp is not None):
            if(temp.next and temp.val==temp.next.val):
                dup = temp.val

                while(temp and temp.val==dup):
                    temp = temp.next

                prev.next = temp


            else:
                prev = temp
                temp = temp.next

        return dummy.next



head = Node(1)
head.next = Node(9)
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(3)

obj = Solution()
result = obj.deleteDuplicates(head, 4)

while result is not None:
    print(result.data, end=" -> ")
    result = result.next

print("None")


