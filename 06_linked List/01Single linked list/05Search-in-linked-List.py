"""
Search for a Value in a Singly Linked List

You are given the head of a singly linked list and an integer `val`. Return
`True` if any node in the linked list contains `val`; otherwise, return
`False`.

Example 1:
    Input:  head = 0 -> 1 -> 2 -> None, val = 2
    Output: True
    Explanation: Node `2` is present in the linked list.

Example 2:
    Input:  head = 12 -> 5 -> 8 -> 7 -> None, val = 6
    Output: False
    Explanation: No node contains the value `6`.

Constraints:
    - The linked list may be empty.
    - Node values and `val` are integers.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def SearchInLL(self,head,val:int):
        current = head   
        while current is not None:
            if(current.data==val):
                return True
            current = current.next  # Move in the next node 
        return False
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

object = Solution()
print(object.SearchInLL(head,30))

    
'''
Time Complexity:O(n)
Space Complexity:O(1)

'''

         
        


        
