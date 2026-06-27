class Solution:
    def ClearithBits(self,n:int,i:int) ->int:
        return (n & ~(1<<i))
    
object = Solution()
print(object.ClearithBits(13,2))    