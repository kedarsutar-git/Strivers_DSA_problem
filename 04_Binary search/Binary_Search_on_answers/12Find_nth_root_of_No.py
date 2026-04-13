# Breute force method
class Solution:
    def nth_root(self,n,m:int) ->int:
        for i in range(1,m+1):
            power = i**n
            if(power ==m):
                return i
            
        return -1
object = Solution()
print(object.nth_root(3,27))
'''
Time Complixity:O(n)
Space Complixity:O(1)
'''

