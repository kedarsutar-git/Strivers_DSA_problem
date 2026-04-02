'''
Reverse pair :
Case.1: i<j
Case.2:nums[i]>2*nums[j]
'''

# Brute Force method
class Solution:
    def Reverse_Pairs(self,nums:list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(i<j and nums[i]> 2*nums[j]):
                    count +=1

        return count 

nums = [9,8,7,6,5,4,3]
object = Solution()
print(object.Reverse_Pairs(nums))                
'''
Time Complxity :O(n**2)
Space Complixity :O(1)
'''



# Optimal method
