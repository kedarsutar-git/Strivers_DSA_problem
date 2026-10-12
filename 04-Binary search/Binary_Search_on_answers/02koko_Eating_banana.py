'''
Koko has piles of bananas and h hours to eat them all. She eats at a fixed speed k (bananas/hour).
The goal is to find the minimum speed k so she finishes within h hours.

'''

# Brute force method 
import math
class Solution:
    def minimumRateToEatBananas(self, nums, h):
        
        for k in range(1,max(nums)+1):
            totalH = 0
            for bananas in nums:
                totalH +=math.ceil(bananas/k)

            if(totalH<=h):
                return k
                
    

nums = [3, 6, 7, 11]
object = Solution()
print(object.minimumRateToEatBananas(nums,8))     

'''
Time Complexity:O(n**2)
Space Complexity:O(1)

'''


# Optimal method 

import math

class Solution:
    def minEatingSpeed(self, nums:list[int],k:int):
        start,end = 1,max(nums)

        while(start<=end):
            k = start +(end-start)//2

            totalH = 0
            for bananas in nums:
                totalH +=math.ceil(bananas/k)

            if(totalH<=h):
                end= k-1

            else:
                start = k+1

        return start            
    
nums = [3, 6, 7, 11]
h = 8
obj = Solution()
print(obj.minEatingSpeed(nums, h))

'''
Time Complixity:O(n)XO(log(max(pil)))
Space Complexity:O(1)

'''
                

