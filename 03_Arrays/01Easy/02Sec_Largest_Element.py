# leet code style 
class Solution:
    def Seclar(self,nums:list[int]) -> int:
        nums.sort()
        largest = nums[len(nums)-1]
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]!=largest):
                return nums[i]
                break

        return nums[i]
nums = [23,54,34,446,78,1]
object =Solution()
print(object.Seclar(nums))   

'''
Time Complixity:O(logn*n)
space Complixity:O(1)
'''


