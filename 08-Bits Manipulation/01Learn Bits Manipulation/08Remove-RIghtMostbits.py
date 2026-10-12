class Solution:
    def Remove(self,n:int)->int:
        return (n & (n-1))
    
object = Solution()
print(object.Remove(2))   

'''
Time Complexity:O(1)
Space Complexity:O(1)
'''