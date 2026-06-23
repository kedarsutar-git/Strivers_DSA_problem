class Solution:
    def printNum(self,n:int):
        if(n==0):
            return
        self.printNum(n-1)
        print(n)

        

object =Solution()
print(object.printNum(5))