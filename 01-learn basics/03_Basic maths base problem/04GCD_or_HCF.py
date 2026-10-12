class Solution:
    def GCD(self,n1:int,n2:int) ->int:
        small = min(n1,n2)
        for i in range(small,0,-1):
            if(n1%i==0 and n2%i==0):
                break

        return i
n1 = 456
n2 = 789
object = Solution()
print(object.GCD(n1,n2))

'''
Time comlexity :O(n)
Space Complexity :O(1)
'''