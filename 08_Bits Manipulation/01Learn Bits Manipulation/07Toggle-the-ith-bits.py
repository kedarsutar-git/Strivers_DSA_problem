class Solution:
    def Togglebits(self,n:int,i:int) -> int:
        return (n^(1<<i))
    
object = Solution()
print(object.Togglebits(13,2))


'''
Time Complexity:O(1)
Space Compexity:O(1)

'''