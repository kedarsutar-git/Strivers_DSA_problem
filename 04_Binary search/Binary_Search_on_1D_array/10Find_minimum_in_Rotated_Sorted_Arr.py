'''
Example 1:
nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.


Example 2:
nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.


Example 3:

nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
'''

# Brute Force method
class Solution:
    def find_min(self,nums:list[int]) ->int:
        MIN = nums[0]
        for i in range(len(nums)):
           
            if(nums[i]<MIN):
                MIN = min(MIN,nums[i])

        return MIN
nums = [11,13,15,17]   
object = Solution()
print(object.find_min(nums))         
'''
Time Complixity:O(n)
Space Complixity:O(1)
'''


# Optimal method
class Solution:  
    def find_min(self, nums: list[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2

            if nums[mid] > nums[end]:
                # Minimum is in the RIGHT half
                start = mid + 1
            else:
                # Minimum is in the LEFT half (mid could be the answer)
                end = mid
 
        return nums[start]

nums = [4, 5, 6, 7, 1, 2]
obj = Solution()
print(obj.find_min(nums))  # Output: 1


