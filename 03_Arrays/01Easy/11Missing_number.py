class Solution:
        def missingnum(self,nums:list[int]):
                n = len(nums)
                Tsum = (n+1)*(n+2)//2
                Esum = sum(nums)
                return Tsum - Esum
nums = [0,1]
object = Solution()
print(object.missingnum(nums))      
'''
Time Complexity:O(1)
Space Complexity:O(1)
'''  


        

