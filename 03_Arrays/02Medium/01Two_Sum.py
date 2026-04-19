# Brute force method 

class Solution:
    def Twosum(self,nums:list[int],tar:int) -> int:
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(nums[i]+nums[j]==tar):
                    return 1
                return -1
nums = [1,2,3,4,5,6]
object  = Solution()
print(object.Twosum(nums,10))
   
'''
Time Complixity: O(n**2)
space Complixity:O(1)

'''   
# optimal method
class Solution:
    def TwoSum(self,nums:list[int])-> int:
        tar = 10
        D = {}
        for i in range(len(nums)): # O(n)
            first = nums[i]
            sec = tar - first
            if sec in D:
                return [D[sec],i] # O(1)

            D[first] = i
nums = [1,2,3,4,5,6]
object = Solution()
print(object.TwoSum(nums))
'''
Time Complexity:O(n)
Space Complexity:O(n)
'''



