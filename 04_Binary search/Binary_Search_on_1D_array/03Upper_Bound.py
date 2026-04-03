# Brute Force Method
class soluion:
    def Upper_Bound(self,nums:list[int],x:int) -> int:
        for i in range(len(nums)):
            if(nums[i]>x):
                return i
        return len(nums)

nums = [3,5,8,9,15,19]  

object = soluion()
print(object.Upper_Bound(nums,9))

'''
Time Complixity :O(n)
Space Complixity :O(1)
'''


# Optimal method

class Solution:
    def upper_Bound(self,nums:list[int],x:int) -> int:
        start = 0
        end = len(nums) - 1

        while(start<=end):
            mid = start +(end-start)//2

            if(nums[mid]>x):
                return mid
                end  =mid -1

            else:
                start = mid+1

        return len(nums)

nums = [1,2,2,3]  
object = Solution()
print(object.upper_Bound(nums,2))

'''
Time complixity :O(logn)
space Complixity :O(1)
'''