
class Solution:
    def FindXOR(self,n:int) ->int:
        if(n%4==1):
            return 1 
        
        if(n%4==2):
            return n+1
        
        if(n%4==3):
            return 0
        
        if(n%4==0):
            return n
        
object = Solution()
print(object.FindXOR(4)) 

