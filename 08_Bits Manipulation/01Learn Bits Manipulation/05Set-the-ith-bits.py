class Solution:
    def Set_ith_bits(self,n:int,i:int) ->int:
        return (n|(1<<i))
    
object = Solution()
print(object.Set_ith_bits(13,2))
'''
Time Complexity:O(1)
Space Complexity:O(1)

'''

