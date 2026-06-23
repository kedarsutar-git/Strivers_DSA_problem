class Solution:
    def printName(self,n:int):
        if(n==0):          # Base Case 
            return
        
        print("python")    # Work 

        self.printName(n-1) # call

object = Solution()
print(object.printName(10))        