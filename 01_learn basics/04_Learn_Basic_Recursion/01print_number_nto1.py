
class Solution:
    def PrintNumber(self,n):
        if(n==0):  # Base Case 
            return 
        
        print(n)   # Work 
        self.PrintNumber(n-1) # call 

object =Solution()
print(object.PrintNumber(10))  

'''
Time Complexity:O(n)
Sapce CompelxityO(1)

'''