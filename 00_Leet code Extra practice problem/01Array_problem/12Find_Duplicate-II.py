'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that 
nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true


Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true


Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

class Solution:
    def FindDuplicate(self,nums:list[int],k:int) ->bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j] and abs(i-j)<=k):
                    return True 
                
        return False 

nums = [1,2,3,1]
object = Solution()
print(object.FindDuplicate(nums,3))            

'''
Time Complexity:O(n^2)
Space Complexity:O(1)

'''


# optimal method 
class Solution:
    def FindDuplicate(self,nums:list[int],k:int) ->bool:
        Map ={}
        for i in range(len(nums)):
            if(nums[i] in Map and i-Map[nums[i]]<=k):
                return True

            Map[nums[i]] = i 

        return False

nums = [1,2,3,1]
object = Solution()
print(object.FindDuplicate(nums,3))    

'''
Time Complexity:O(n)
Sapce Complexity:O(n)
'''