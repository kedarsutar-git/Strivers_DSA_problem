class Solution:
    def printnumber(self,n:int,count):
        if(count>n):
            return
        
        print(count)
        self.printnumber(n,count+1)
object = Solution()
object.printnumber(10,1)





