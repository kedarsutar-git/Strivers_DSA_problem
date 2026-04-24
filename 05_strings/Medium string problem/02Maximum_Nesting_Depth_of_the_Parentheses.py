'''
Example 1:
Input:
s = "(1+(2*3)+((8)/4))+1"
Output:
3
Explanation:
Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input:
s = "(1)+((2))+(((3)))"
Output:
3
Explanation:
Digit 3 is inside of 3 nested parentheses in the string.
'''

class Solution:
    def MaxNestingDepthofparenthesis(self,s:str) ->int:
        Max_depth = 0
        current_depth = 0
        for brac in s:
            if(brac=="("):
                current_depth +=1
                Max_depth = max(Max_depth,current_depth)

            elif(brac==")"):
                current_depth -=1
        return Max_depth
s = "(1+(2*3)+((8)/4))+1"     
object =Solution()
print(object.MaxNestingDepthofparenthesis(s))        
        

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''        
