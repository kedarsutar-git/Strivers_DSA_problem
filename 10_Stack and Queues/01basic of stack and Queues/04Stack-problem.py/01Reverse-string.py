'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
'''

class Solution:
    def Reversestr(self,s:str) ->None:
        Stack = []

        for char in s:
            Stack.append(char)

        for i in range(len(s)):
            s[i] = Stack.pop()

        return s

s = ["h","e","l","l","o"]
object = Solution()
print(object.Reversestr(s))

'''
Time Complexity:O(n)
Sapce Complexity:O(n)
'''