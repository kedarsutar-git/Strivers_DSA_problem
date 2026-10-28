'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
Example 4:

Input: s = "("
Output: false
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
'''

class Solution:
    def ValidPar(self,s:str) ->bool:
        low ,high = 0 ,0 
        for brac in s:
            if brac=="(":
                low += 1
                high += 1

            elif brac==")":
                low -= 1
                high -=1

            else:
                low -= 1
                high += 1

            if(high<0):
                return False

            low = max(low, 0)

        return low==0

object = Solution()
s = "("
print(object.ValidPar(s))


'''
Time Complexity:O(n)
Space Complexity:O(1)

'''