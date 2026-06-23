'''
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.

 

Example 1:

Input: head = [1,1,2]
Output: [1,2]


Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''

class Node:
    def __init__(self,data,val = 0):
        self.data = data
        self.next = None 


class Solution:
    def RemoveDuplicate(self,head):

        temp = head 

        while(head is not None and head is not None):
            if(head.val == head.next.val):
                head.next = head.next.next

            else:
                head = head.next

        return temp    

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''


# Code Explanation

'''
Initialization:

1. 
temp = head

The function takes the head of a sorted linked list as input.
It initializes a variable res to keep track of the head of the modified list.
Traverse the Linked List:

2.
while head is not None and head.next is not None:

The function uses a while loop to traverse the linked list.
The loop continues as long as head and head.next are not None.
Check for Duplicates:

3.
if head.val == head.next.val:

Inside the loop, it checks if the current node's value (head.val) is equal to the 
next node's value (head.next.val).
Remove Duplicates:

4.
head.next = head.next.next

If the values are equal, it means there is a duplicate.
The next pointer of the current node is updated to skip the next node and point to the 
node after the next (head.next.next).
Move to the Next Node:

5.
else:
    head = head.next

If the values are not equal, the function moves the head pointer to the next node.
Return the Result:


6.
return temp

After the loop completes, the function returns res, which points to the head of the 
modified linked list with duplicates removed.
'''

        