class Solution:
    def Fibonacci(self,num:int):
        if(num==0 or num==1):
            return num
        else:
            return self.Fibonacci(num-1)+self.Fibonacci(num-2)
        
num = 4
object = Solution()
print(object.Fibonacci(num))


    