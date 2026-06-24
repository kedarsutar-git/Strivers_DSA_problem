class Solution:
    def printNum(self,n:int):
        if(n==0):     # base case
            return
        self.printNum(n-1)   # function call
        print(n)      # work

        

object =Solution()
print(object.printNum(5))