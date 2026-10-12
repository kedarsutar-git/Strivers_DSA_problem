'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"
 
'''
class Solution:
    def toLowerCase(self,s:str) -> str:
        return s.lower()
s = "Hello"
object = Solution()
print(object.toLowerCase(s))

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
