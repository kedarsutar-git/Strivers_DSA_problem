'''

Given the array of integers nums, you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1). 
Note : array contain all unique number 

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is,
(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 


Example 2:

Input: nums = [1,4,5]
Output: 12
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), 
you will get the maximum value of (4-1)*(5-1) = 16.


Example 3:

Input: nums = [3,7]
Output: 12
 

Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3

'''

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        def Largest(nums):
            largest = nums[0]
            for i in range(1, len(nums)):
                if nums[i] > largest:
                    largest = nums[i]
            return largest

        def secondlargest(nums):
            largest = max(nums)
            seclargest = -1
            for num in nums:
                if num != largest:
                    seclargest = max(num, seclargest)
            return seclargest

        Largestnum = Largest(nums) - 1
        Seclargestnum = secondlargest(nums) - 1

        return Largestnum * Seclargestnum

nums = [3,4,5,2]
object = Solution()
print(object.maxProduct(nums))


'''
Time Complexity:O(n+m)
Sapce Complexity:O(1)
'''