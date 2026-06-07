'''
Example 1:
Input:
s = "rotation", goal = "tionrota"
Output:
 true
Explanation:
After multiple left shifts on "rotation", we get:
    1st shift → "otationr"
    2nd shift → "tationro"
    3rd shift → "ationrot"
    4th shift → "tionrota"
    So the goal string can be obtained by rotating the original string.

Example 2:
Input:
s = "hello", goal = "lohelx"
Output:
false
Explanation:
 
Even after all possible rotations of "hello", we cannot form "lohelx" due to the presence of an extra character 'x'. Hence, it's not possible.
         
'''
class Solution:
    def IfRotate(self,s:str,goal:str) ->bool:
        s1 = s+s
        if(goal in s1 and len(goal)==len(s)):
            return True 
        
        return False 
    
s = "rotation"
goal = "tionrota"
object =Solution() 
print(object.IfRotate(s,goal))
   
'''
Time Comlexity:O(1)
Space Complexity:O(1)

'''

