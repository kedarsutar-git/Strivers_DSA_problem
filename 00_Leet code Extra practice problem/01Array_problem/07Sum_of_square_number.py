'''
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5


Example 2:
Input: c = 3
Output: false
'''

class Solution:
    def squareNum(self,c:int) ->int:
        start = 0
        end = int(c**0.5)

        while(start<=end):
            total = start*start + end*end
            if(total==c):
                return True 
            
            elif(total>c):
                end -=1

            else:
                start +=1

        return False 

object = Solution()
print(object.squareNum(3))   
'''
Time Complexity:O(n)
Space Complexity:O(1)

'''          