'''
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
'''

class Solution:
    def maxlenstr(self,s:str) ->int:
        stack = []
        validstr = 0
        for i in range(len(s)):
            if(s[i]=="("):
                stack.append(i)

            else:
                stack.pop()

            if(not stack):
                stack.append(i)

            else:
                validstr = max(validstr,i-stack[-1])

        return validstr
s = ""
object = Solution()
print(object.maxlenstr(s))

'''
Time Complexity:O(n)
Space Complexity:O(n)
'''

