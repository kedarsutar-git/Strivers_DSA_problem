'''
Example 1:
Input:
nums = [1, 2, 1, 3, 5, 2]
Output:
[3, 5]
Explanation:

The integers 3 and 5 have appeared only once.

Example 2:
Input:
nums = [-1, 0]
Output:
[-1, 0]
Explanation:

The integers -1 and 0 have appeared only once.
'''
class Solution:
    def SingleNumber(self,nums:list[int]) ->list[int]:
        ans = 0
        for i in range(len(nums)):
            ans = ans ^nums[i]

            
        return ans 
object = Solution()
nums = [1, 2, 1, 3, 5, 2]
print(object.SingleNumber(nums))            
