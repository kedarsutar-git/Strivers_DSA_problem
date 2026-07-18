'''
Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.


Example 1

Input: nums = [2, 3, 5, -2, 7, -4]
Output: 15

Explanation:
The subarray from index 0 to index 4 has the largest sum = 15



Example 2

Input: nums = [-2, -3, -7, -2, -10, -4]
Output: -2

Explanation:
The element on index 0 or index 3 make up the largest sum when taken as a subarray
'''

# optimal method(kadanes algorithm)
class Solution:
    def Max_SubArr_Sum(self,nums:list[int]) -> int:
        Max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(nums[i],current_sum+nums[i])
            Max_sum = max(Max_sum,current_sum)

        return Max_sum

nums =  [1,2,5,3,2,4,6,4,3,5,3]  
object = Solution()
print(object.Max_SubArr_Sum(nums))

'''
Time complexity:O(n)
space complexity:O(1)
'''


class Solution:
    def SubArrSum(self,nums:list[int]) ->int:
        current_sum,Max_sum = 0,0
        for i in range(len(nums)):
            current_sum += nums[i]
            Max_sum = max(current_sum,Max_sum)

            if(current_sum<0):
                current_sum = 0

        return Max_sum
nums = [1,2,5,3,2,4,6,4,3,5,3]
object = Solution()
print(object.SubArrSum(nums))




            