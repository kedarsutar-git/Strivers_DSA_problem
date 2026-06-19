class Solution:
    def printNumber(self,n:int) ->None:
        if(n==0):
            return 
        
        print(n)
        self.printNumber(n-1)

object =Solution()
print(object.printNumber(10))
