'''
Example 1

Input: head -> 3 -> 7 -> 5 -> 7 -> 3
Output: true
Explanation: 37573 is a palindrome.



Example 2

Input: head -> 1 -> 1 -> 2 -> 1\
Output: false
Explanation: 1121 is not a palindrome.
'''
class Node:
    def __init__(self,data,val = 0):
        self.data = data 
        self.next = None 

class Solution:
    def IsPalindrome(self,head):
        stack = []
        temp = head

        while(temp is not None):
            stack.append(temp.val)
            temp = temp.next

        temp = head 

        while(temp is not None):
            if(temp.val!=stack.pop()):
                return False
            temp = temp.next

        return True 

'''
Time Compliexity:O(2n)
Space Compliexity:O(n)

'''    

        