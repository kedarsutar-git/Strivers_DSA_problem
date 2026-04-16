
class Solution:
     def linerSearch(self,nums:list[int],n:int) -> int:
          
          for i in range(len(nums)):
               if(nums[i]==n):
                    return i
          else:
               return -1
nums = [1,2,3,4,5,43]
object = Solution()
print(object.linerSearch(nums,34))  
'''
Time Complixity:O(n)
Space Complixity:O(1)
'''              