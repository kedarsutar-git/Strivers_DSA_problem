class Solution:
    def printName(self,n:int):
        if(n==0):
            return 
        
        print("kedar")
        self.printName(n-1)
        

object = Solution()
print(object.printName(10))        