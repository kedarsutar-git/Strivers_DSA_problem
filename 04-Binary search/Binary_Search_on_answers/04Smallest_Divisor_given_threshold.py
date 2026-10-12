import math
class Solution:
    def smallestDivisor(self, nums:list[int], limit:int) ->int:
        for dev in range(min(nums),max(nums)+1):
            sum = 0
            for num in nums:
                sum +=math.ceil(num/dev)
            if(sum<=limit):
                return dev

        return -1        
nums =  [1,2,5,9] 
object =Solution()
print(object.smallestDivisor(nums,6))      
 
'''
Time Complixity:O(max*n)
Space Complixity:O(1)
'''

# Optimal method  
import math
class Solution:
    def Find_min_Div(self,nums:list[int],thr:int) ->int:
        start = 1
        end = max(nums)
        ans = -1
       
        while(start<=end):
            mid = start+(end-start)//2
            sum = 0 
            for num in nums:
                sum += math.ceil(num/mid)
            if(sum<=thr):
                ans = mid
                end = mid-1

            else:
                start = mid+1

        return ans            
           
           
nums = [1,2,5,9] 
object = Solution()
print(object.Find_min_Div(nums,6))   

'''
Time Complixity:O(log(max)*n)
space Complixity:O(1)
'''


         

       

          