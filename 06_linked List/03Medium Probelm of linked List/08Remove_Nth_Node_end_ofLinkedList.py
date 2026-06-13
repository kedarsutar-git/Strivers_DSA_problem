'''
Input:  5->1->2, N=2
Output: 5->2
Explanation: The 2nd node from the end of the linked list is 1. Therefore, we get this result after removing 1 from the linked list.

Input:  1->2->3->4->5, N=3
Output: 1->2->4->5
Explanation: The 3rd node from the end is 3, therefore, we remove 3 from the linked list.
'''

# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        
        # Step 1: Find length of linked list
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        # If head needs to be deleted
        if length == n:
            return head.next

        # Step 2: Find (L-N)th node
        temp = head
        res = length - n

        while res > 1:
            temp = temp.next
            res -= 1

        # Step 3: Delete (L-N+1)th node
        temp.next = temp.next.next

        return head



