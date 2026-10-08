'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
'''


# Brute Force method 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def ConvertBinaryToDecimal(self,head):
        arr = []

        current = head
        while(current is not None):
            arr.append(current.data)

            current = current.next
        Decimal = 0
        for i in range(len(arr)):
            Decimal = Decimal * 2 + arr[i]

        return Decimal
      

head = Node(1)
head.next  = Node(0)
head.next.next = Node(1)
head.next.next.next = Node(1)

object = Solution()
result = object.ConvertBinaryToDecimal(head)
print(result)



'''
Time Complexity:O(n)
Space Complexity:O(n)

'''

# Optimal method

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def ConvertBinaryToDecimal(self,head) ->int:
        Decimal = 0
        current = head

        while(current is not None):
            Decimal = Decimal * 2 + current.data

            current = current.next

        return Decimal

head = Node(1)
head.next = Node(0)
head.next.next = Node(1)
head.next.next.next = Node(1)

object = Solution()
result = object.ConvertBinaryToDecimal(head)
print(result)

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''

