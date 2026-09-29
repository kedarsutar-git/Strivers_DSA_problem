'''
Given an array nums of length n, return an array answer of length n - 1 such that answer[i] = nums[i] | nums[i + 1] where | is the bitwise OR operation

Example 1:
Input: nums = [1,3,7,15]

Output: [3,7,15]

Example 2:
Input: nums = [8,4,2]

Output: [12,6]
'''

class Solution:
    def XORNnums(self,nums:list[int]) ->list[int]:
        ans = []
        for i in range(len(nums)-1):
            ans.append(nums[i] | nums[i+1])
        return ans

nums = [1,3,7,15]
object = Solution()
print(object.XORNnums(nums))


'''
Time Complexity:O(n)
Sapce Complexity:O(n)
'''