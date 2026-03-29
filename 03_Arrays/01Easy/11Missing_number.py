
def missing(arr):
        n = len(arr)
        lotalsum = sum(arr)
        N = (n+1)
        expsum = N*(N+1)//2

        return expsum-lotalsum
    
arr = [1,6,5,3,4]

print(missing(arr))    



# leet code style 
class Solution:
        def missingnum(self,nums:list[int]):
                n = len(nums)
                Tsum = (n+1)*(n+2)//2
                Esum = sum(nums)
                return Tsum - Esum
nums = [1,3,4,5,6,7]
object = Solution()
print(object.missingnum(nums))        