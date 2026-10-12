'''
Example 1:
Input:
s = "((()))"
Output:
 "(())"
Explanation:
 The input string is a single primitive: "((()))".  
Removing the outermost layer yields: "(())".

Example 2:
Input:
s = "()(()())(())"
Output:
"(()())()"
Explanation:
 Primitive decomposition: "()" + "(()())" + "(())"  
After removing outermost parentheses: "" + "()()" + "()"
Final result: "(()())()".
'''
class Solution:
    def RemoveOuterParenteses(self,s:str) ->str:
        result = []
        depth =  0
        for ch in s:
            if(ch=="("):
                if(depth>0):
                    result.append(ch)
                depth +=1
            else:
                depth -=1
                if(depth>0):
                    result.append(ch)    

        return ''.join(result)  

s = "()(()())(())"    
object = Solution()
print(object.RemoveOuterParenteses(s))   

'''
Time Complexity :O(n)
Space Complexity:O(n)
'''


class Solution:
    def removeOuterParentheses(self,s:str) ->str:
        count = 0
        ans = ""
        for ch in s:
            if(ch=="("):
                if(count>0):
                    ans +=ch
                count +=1

            else:
                count -=1
                if(count>0):
                    ans +=ch

        return ans

s = "()(()())(())"    
object = Solution()
print(object.removeOuterParentheses(s))      

'''
Time Complexity :O(n)
Space Complexity:O(n)
'''