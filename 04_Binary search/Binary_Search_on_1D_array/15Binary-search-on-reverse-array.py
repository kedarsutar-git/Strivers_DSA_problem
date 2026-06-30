'''
Given an array arr[] sorted in decreasing order, and an integer X, the task is to check if X 
is present in the given array or not. If X is present in the array, print its index ( 0-based indexing). 
Otherwise, print -1.

Examples: 

Input: arr[] = {5, 4, 3, 2, 1}, X = 4
Output: 1
Explanation: Element X (= 4) is present at index 1.
Therefore, the required output is 1.



Input: arr[] = {10, 8, 2, -9}, X = 5
Output: -1
Explanation: Element X (= 5) is not present in the array.
Therefore, the required output is -1.
'''
class Solution:
    def BinarySearch(self,nums:list[int],target:int) ->int:
        start = 0
        end = len(nums)-1

        while(start<=end):
            mid = start + (end - start)//2

            if(nums[mid] == target):
                return mid
            
            elif(nums[mid]>target):
                start = mid + 1

            else:
                end = mid -1

        return -1 

nums = [5, 4, 3, 2, 1]
object = Solution()
print(object.BinarySearch(nums,4))  

'''
Time Complexity:O(logn)
Space Complexity:O(1)

'''