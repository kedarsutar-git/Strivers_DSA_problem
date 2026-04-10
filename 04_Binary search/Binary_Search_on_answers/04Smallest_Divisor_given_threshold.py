import math
class Solution:
    def Smallest_Div(self,nums:list[int],thr:int) -> int:
        for div in range(1,max(nums)):
            sum = 0
            for i in range(len(nums)):
                sum += math.ceil(nums[i]/div)

            if(sum<=thr):
                return div

        return -1
    
nums = [1,2,5,9]
object = Solution()
print(object.Smallest_Div(nums,6))    
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
        ans = 0
       
        while(start<=end):
            mid = start+(end-start)//2
            sum = 0 
            for i in range(len(nums)):
                sum += math.ceil(nums[i]/mid)
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


       

          