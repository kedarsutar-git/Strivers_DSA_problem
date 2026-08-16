'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]
'''
class Solution:
    def findClosestElements(self, nums: list[int], k: int, target: int) -> list[int]:
        left, right = 0, len(nums) - k
        
        while left < right:
            mid = left + (right - left) // 2
            # Compare distance of nums[mid] vs nums[mid + k] from target
            if target - nums[mid] > nums[mid + k] - target:
                left = mid + 1
            else:
                right = mid
                
        return nums[left : left + k]


object = Solution()
nums = [1,1,2,3,4,5]
print(object.findClosestElements(nums,4,-1))