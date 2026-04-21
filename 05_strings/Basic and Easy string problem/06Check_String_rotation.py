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
    def CheckString(self,s:str,goal:str):
        result = s+s
        if(len(s)!=len(goal)):
            return False
        
        return goal in result
             
s = "rotation"
goal = "tionrota"
object =Solution()
print(object.CheckString(s,goal))
'''
Time Comlexity:O(1)
Space Complexity:O(1)

'''