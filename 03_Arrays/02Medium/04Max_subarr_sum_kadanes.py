# optimal method(kadanes algorithm)
class Solution:
    def Max_SubArr_Sum(self,nums:list[int]) -> int:
        Max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(nums[i],nums[0]+nums[i])
            Max_sum = max(Max_sum,current_sum)

        return Max_sum

nums =  [1,2,5,3,2,4,6,4,3,5,3]  
object = Solution()
print(object.Max_SubArr_Sum(nums))

'''
Time complexity:O(n)
space complexity:O(1)
'''



     
            