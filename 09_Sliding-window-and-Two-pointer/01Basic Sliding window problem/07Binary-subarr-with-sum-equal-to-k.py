'''
Input: nums = [1, 0, 0, 1, 1, 0], goal = 2  
Output: 6
Explanation: There are 6 subarrays with sum exactly equal to 2:
[1, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1], [1, 1], [1, 1, 0], [0,0,1,1,0]


Input: nums = [0,0,0,0,0,0], goal = 0  
Output: 21  
Explanation: All subarrays with only 0s will have sum = 0.  
There are 21 such subarrays in total (n(n+1)/2 = 6*7/2 = 21).
'''
# Brute force method 

class Solution:
    def BinarySubarrSum(self,nums:list[int],goal:int) ->int:
        count = 0
        for i in range(len(nums)):
            Sum = 0
            for j in range(i,len(nums)):
                Sum += nums[j]
                if(Sum==goal):
                    count += 1

        return count

object = Solution()
nums = [0,0,0,0,0]
print(object.BinarySubarrSum(nums,0))       

'''
Time Complexity:O(n**2)
Space Complexity:O(1)

'''