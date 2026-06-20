'''
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).


Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
'''
class Solution:
    def Countpairs(Self,nums:list[int],lower:int,upper:int) ->int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(lower <= nums[i] + nums[j] <= upper):
                    count+=1

        return count

nums = [0,1,7,4,4,5]
object =Solution()
print(object.Countpairs(nums,3,6))                

'''
Time Complexity:O(n^2)
Space Complexity:O(1)

'''

# optimal method 
class Solution:
    def countFairPairs(Self,nums:list[int],lower:int,upper:int) ->int:

        nums.sort()

        # count pairs for sum<= upper

        start = 0
        end = len(nums)-1
        upper_count = 0

        while(start<end):
            if(nums[start]+nums[end]<=upper):
                upper_count += (end-start)
                start += 1
            else:
                end -= 1

        # Count pairs with sum <= lower - 1
        start = 0
        end = len(nums) - 1
        lower_count = 0

        while(start < end):
            if nums[start] + nums[end] <= lower - 1:
                lower_count += (end - start)
                start += 1
            else:
                end -= 1

        return upper_count - lower_count
    
nums = [0,1,7,4,4,5]
object =Solution()
print(object.countFairPairs(nums,3,6))      
