
class Solution:
    def PrintNumber(self,n):
        if(n==0):
            return 
        
        print(n)
        self.PrintNumber(n-1)

object =Solution()
print(object.PrintNumber(10))        