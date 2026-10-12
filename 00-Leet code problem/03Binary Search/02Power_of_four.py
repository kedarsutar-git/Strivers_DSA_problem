'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
'''

class Solution:
    def powerofFour(self,n:int) ->bool:
        if(n<=0):
            return False
        
        start,end = 0,int(n**0.5)
        
        while(start<=end):
            mid = start+(end-start)//2
            val = 4**mid
            if(val==n):
                return True
            
            elif(val>n):
                end = mid-1

            else:
                start = mid+1

        return False

object = Solution()
print(object.powerofFour(5))            

'''
Time Complexity:O(1/2logn)
Sapce Complexity:O(1)
'''
