'''
Given the head of a singly linked list representing a positive integer number. Each node of the linked list represents a digit of the number, with the 1st node containing the leftmost digit of the number and so on. Check whether the linked list values form a palindrome or not. Return true if it forms a palindrome, otherwise, return false.

A palindrome is a sequence that reads the same forward and backwards.

Example 1:
Input: head -> 3 -> 7 -> 5 -> 7 -> 3

Output: true

Explanation: 37573 is a palindrome.

Example 2:
Input: head -> 1 -> 1 -> 2 -> 1

Output: false

Explanation: 1121 is not a palindrome.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def LinkedListPalindrome(self,head):
        ans = []
        temp = head
        while(temp is not None):
            ans.append(temp.data)
            temp = temp.next

        

        i = 0
        j = len(ans)-1
        while(i<j):
            if(ans[i]!=ans[j]):
                return False
            i+=1
            j-=1    

        return True
        
            

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)


object = Solution()

result = object.LinkedListPalindrome(head)
print(result)

while(result is None):
    print(result.data,end= "->")

    result = result.next

'''
Time Complexity:O(n)
Space COmplexity:O(1)

'''