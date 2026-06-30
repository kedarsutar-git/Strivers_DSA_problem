'''
Given a sorted array arr[] of infinite numbers. The task is to search for an element k in the array.

Examples:

Input: arr[] = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170], k = 10
Output: 4
Explanation: 10 is at index 4 in array.

Input: arr[] = [2, 5, 7, 9], k = 3
Output: -1
Explanation: 3 is not present in array.
'''

class Solution:
    def BinarySeachInfinity(self,nums:list[int],target:int) ->int:
        
        def BinarySearch(nums,start,end):
            while(start<=end):
                mid = start + (end - start)//2

                if(nums[mid]==target):
                    return mid

                elif(nums[mid]>target):
                    end = mid - 1

                else:
                    start = mid + 1

            return -1
        
        start = 0
        end = 1

        while(end<len(nums) and target>nums[end]):
            start = end +1
            end = end * 2

            if(end>=len(nums)):
                end = len(nums)-1

        return BinarySearch(nums,start,end)
            

nums = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
object = Solution()
print(object.BinarySeachInfinity(nums,140))

'''
Time complexity:O(logn)
Space Complexity:O(1)

'''
