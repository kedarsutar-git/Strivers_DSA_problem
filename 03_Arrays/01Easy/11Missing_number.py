class Solution:
        def missingnum(self,nums:list[int]):
                n = len(nums)
                Tsum = (n+1)*(n+2)//2
                Esum = sum(nums)
                return Tsum - Esum
nums = [1,3,4,5,6,7]
object = Solution()
print(object.missingnum(nums))      
'''
Time Complixity:O(1)
Space Complixity:O(1)
'''  