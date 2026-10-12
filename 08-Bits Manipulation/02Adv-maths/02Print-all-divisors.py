class Solution:
    def PrintDivisors(self,n:int) ->list[int]:
        temp = []
        for i in range(1,n+1):
            if self.isDivisors(n,i):
                temp.append(i)

        return temp

    def isDivisors(self,n,i):
        if(n%i==0):
            return True 
        
        return False 
    
object = Solution()
print(object.PrintDivisors(12))   
'''
Time Complexity:O(n)
Space Complexity:O(n)

''' 
                
