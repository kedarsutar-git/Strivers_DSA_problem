class Solution:
    def reverse(self,num:int) ->int:
        reversed = 0
        while(num>0):
            m = num%10
            num = num//10

            reversed = (reversed*10) + m

        return reversed
num = 1234
object = Solution()
print(object.reverse(num))

'''
Time Complexity:O(logn)
Space Complexity:O(1)
'''
