'''
Example 1:
Input : 
start = 10 , goal = 7
Output :
 3
Explanation :
 The binary representation of 10 is "1010". The binary representation 
 of 7 is "111". If we flip the underlined bits in binary representation 
 of 10 then we will obtain our goal.

 
Example 2 :
Input :
 start = 3 , goal = 4
Output :
 3
Explanation :
 The binary representation of 3 is "011".The binary representation of 4 
 is "100". So if we flip all the three bits of 3 then we will reach our 
 goal number.
'''

# Brute force method 
class Solution:
    def MinFlipped(self,start:int,goal:int) ->int:
        ans = start^goal
        count = 0
        for i in range(32):
            if(ans & (1<<i)):
                count +=1

        return count        

object = Solution()
print(object.MinFlipped(10, 7))            


'''
Time Complexity:O(n)
Space Complexity:O(1)

'''
