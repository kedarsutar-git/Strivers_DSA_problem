class Solution:
    def printName(self,n:int):
        if(n==0):
            return 
        
        print("kedar")
        self.printName(n-1)
        

object = Solution()
print(object.printName(10))    


class Solution:
    def printnumber(self,n:int,count):
        if(n<count):
            return 
        
        self.printnumber(n,count+1)
        print(count)
        


object = Solution()
print(object.printnumber(10,1))        