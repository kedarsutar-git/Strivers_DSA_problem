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


class Solution:
    def nthRoot(self,n:int,m:int) ->int:
        start = 1
        end = m
        ans = 1
        while(start<=end):
            mid = start + (end - start)//2

            if(n**mid<=m):
                ans = mid
                start = mid + 1

            else:
                end = mid -1

        return ans 

object = Solution()
print(object.nthRoot(2,64))              

'''
Time complexity:O(logn)
Space Complexity:O(1)

'''

