'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


Example 2:

Input: head = [1,2]
Output: [2,1]
Example 3:


Example 3:
Input: head = []
Output: []
'''

class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class Solution:
    def ReverseLinkedList(self,head):
        stack = []
        temp = head

        while(temp is not None):
            stack.append(temp.val)

            temp = temp.next

        temp = head
        while(temp is not None):
            temp.val = stack.pop()

            temp = temp.next

        return head
        


'''
Time Complexity:O(n)
Space Complexity:O(1)

'''

        