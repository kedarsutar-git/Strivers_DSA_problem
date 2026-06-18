class Solution:
    def MyPow(self,x:int,n:int):
        if(n==0):
            return 1
        
        if(n<0):
            return 1/self.MyPow(x,-n)

        return x*self.MyPow(x,n-1)

object =Solution()
print(object.MyPow(2,10))

'''
Time Complexity:O(logn)
space Complexity:O(logn)
'''

