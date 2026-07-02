'''
Problem Statement: Search in a Nearly Sorted Array
Description:

A nearly sorted array (or almost sorted array) is an array where an element that is at index i in the sorted array can appear at index i-1, i, or i+1 in the given array.

Given a nearly sorted array nums and a target integer target, return the index of target if it exists in the array. If it does not exist, return -1.

You must write an algorithm that runs in 
 time complexity.

Example 1:
Input: nums = [10, 30, 20, 50, 40, 70, 60, 80], target = 30
Output: 1



Example 2:
Input: nums = [10, 30, 20, 50, 40, 70, 60, 80], target = 90
Output: -1

Constraints:

The array is nearly sorted such that each element at index i could be at i-1, i, or i+1.
'''
class Solurion:
    def SearchAlmostSortarr(self,nums:list[int],target:int) ->int:
        start = 0
        end = len(nums)-1

        while(start<=end):
            mid = start + (end - start)//2

            if(mid-1>=0 and nums[mid-1]==target):
                return mid -1
            
            if(mid+1<len(nums) and nums[mid]==target):
                return mid
            
            if(nums[mid-1]==target):
                return mid-1
            
            if(target>nums[mid]):
                start = mid +1

            else:
                end = mid -1

        return -1

nums =   [10, 30, 20, 50, 40, 70, 60, 80]
object = Solurion()
print(object.SearchAlmostSortarr(nums,30))       
