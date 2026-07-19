class Solution:
    def printdig(self,n:int):
        if(n==0):
            return 
        
        digit = n%10
        n = n//10

        self.printdig(n)
        print(digit,end=" ")

object = Solution()
object.printdig(1234)
