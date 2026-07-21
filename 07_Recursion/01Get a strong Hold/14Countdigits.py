class Solution:
    def countdigits(self,n:int):
        if(n==0):
            return 
        
        digit = n%10
        n = n//10

        self.countdigits(n)
        print(digit,end=" ")

object = Solution()
object.countdigits(1234)
