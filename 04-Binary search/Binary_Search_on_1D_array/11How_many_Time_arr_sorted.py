'''
Example 1

Input : nums = [4, 5, 6, 7, 0, 1, 2, 3]
Output: 4
Explanation: The original array should be [0, 1, 2, 3, 4, 5, 6, 7]. So, we can notice that the array has been rotated 4 times.



Example 2

Input: nums = [3, 4, 5, 1, 2]
Output: 3
Explanation: The original array should be [1, 2, 3, 4, 5]. So, we can notice that the array has been rotated 2 times.
'''



'''
Note :first find the min number in the array and then return the index of this number 
'''
class Solution:
    def findKRotation(self,nums:list[int]) ->int:
        start = 0
        end = len(nums)-1
        ans = float('inf')

        while(start<=end):
            mid = start +(end-start)//2

            if(nums[start]<nums[mid]):
                ans = min(ans,nums[start])

                start = mid+1

            else:
                ans = min(ans,nums[mid])

                end = mid-1

        return nums.index(ans)    
    
nums =  [3, 4, 5, 1, 2]
obj = Solution()
print(obj.findKRotation(nums))
