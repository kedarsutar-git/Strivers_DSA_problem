'''
Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums such that they add up to target.
Each input will have exactly one solution, and the same element cannot be used twice. Return the answer in any order.


Example 1

Input: nums = [1, 6, 2, 10, 3], target = 7
Output: [0, 1]

Explanation:
nums[0] + nums[1] = 1 + 6 = 7



Example 2

Input: nums = [1, 3, 5, -7, 6, -3], target = 0
Output: [1, 5]

Explanation:
nums[1] + nums[5] = 3 + (-3) = 0
'''

# Brute force method 


class Solution:
    def Twosum(self,nums:list[int],tar:int) -> int:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==tar):
                    return 1
        return -1
nums = [1,2,3,4,5,112]
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





            
        