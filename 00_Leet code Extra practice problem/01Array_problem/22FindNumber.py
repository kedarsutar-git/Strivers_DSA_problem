'''
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]


Example 2:
Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
'''

class Solution:
    def FindNumbers(Self,nums:list) ->list[int]:
        arr = set(nums)
        temp = []

        for i in range(1,len(nums)+1):
            if(i not in arr):
                temp.append(i)

        return temp

nums = [4,3,2,7,8,2,3,1]
object = Solution()
print(object.FindNumbers(nums)) 

'''
Time Complexity:O(n)
Space Complexity:O(n)
'''