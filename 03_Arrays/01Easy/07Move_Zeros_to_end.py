# Brute force method
class Solution:
    def MoveZerosToend(self,nums:list[int]) ->list[int]:
        nums.sort()
        i = 0
        j = len(nums)-1
        while(i<=j):
            nums[i],nums[j] = nums[j],nums[i]
            i +=1
            j-=1

        return nums
nums = [1,2,3,4,0,0,20,4,3,0]
object = Solution()
print(object.MoveZerosToend(nums))    
'''
Time complixity:O(nlogn)
Space Complixity:O(1)
''' 


# Optimal method
class Solution:
    def movezero(self,nums:list[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[i],nums[j] = nums[j],nums[i]

                j+=1
nums = [1,2,3,4,0,0,20,4,3,0]
obj = Solution()
obj.movezero(nums)
print(nums)

'''
Time Complixity:O(n)
Space Complixity:O(1)
'''
      




