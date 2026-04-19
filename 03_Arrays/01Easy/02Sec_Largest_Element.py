# Brute Force method
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
Time Complexity:O(logn*n)
space Complexity:O(1)
'''


