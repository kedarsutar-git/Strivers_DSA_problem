'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].


Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.



Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
'''

class Solution:
    def Atmost(self,nums:list[int],k:int) ->int:
        right ,left = 0 ,0
        Sum = 0
        count = 0

        while(right<len(nums)):
            Sum += (nums[right]%2)

            while(Sum>k):
                Sum -= (nums[left]%2)
                left += 1

            count += (right - left + 1)
            right += 1

        return count         

    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        return self.Atmost(nums,k) - self.Atmost(nums,k-1)
    
nums = [1,1,2,1,1]
object = Solution()
print(object.numberOfSubarrays(nums,3))   

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''

