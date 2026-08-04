'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isvalid(self,s:str) ->bool:
        stack = []
        for i in range(len(s)):
            char = s[i]

            # if opening braket push into the stack
            if(char=="(" or char=="{" and char=="["):
                stack.append(char)

            else:   # if close braket top and pop the braket in the stack 
                if(len(stack)!=0):
                    top = stack[-1]

                    if(char==")" and top == "("  or  char=="}" and top == "{"  or char=="]" and top =="["):
                        stack.pop()

                    else:
                        False

                else:
                    False


        if(len(stack)==0):
            return True 

        else:
            return False

s =  "([])"
object = Solution()
print(object.isvalid(s))

'''
Time complexity:O(n)
Space Complexity:O(n)
'''
