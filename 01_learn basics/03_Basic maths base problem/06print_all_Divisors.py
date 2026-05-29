class Solution:
    def Divisors(self,num:int) ->int:
        for i in range(1,num+1):
            if(num%i==0):
                print(i, end=" ")
                
num = 123
object = Solution()
print(object.Divisors(num))            

'''
Time Complexity:O(n)
Space Complexity:O(1)
'''        