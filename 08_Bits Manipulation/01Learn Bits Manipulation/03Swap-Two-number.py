class Solution:
    def Swapnumber(self,a:int,b:int):
        a = a^b
        b = a^b
        a = a^b

        return a,b

object = Solution()
print(object.Swapnumber(2,3))

'''
Time Complexity:O(1)
Space Complexity:O(1)
'''