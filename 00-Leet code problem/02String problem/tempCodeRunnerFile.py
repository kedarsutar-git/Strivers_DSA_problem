class Solution:
#     def minimalKSum(self, nums: list[int], k: int) -> int:
#         nums_set = set(nums)
        
#         count = 0
#         curr = 1
#         ans = 0
#         while(count<k):
#             if curr not in nums:
#                 ans += curr
#                 count += 1
#             curr += 1
#         return ans
    
# nums = [1]
# object = Solution()
# print(object.minimalKSum(nums,100000000))