class Solution:
    def sum(self,num:int) ->int:
        if(num==1):
            return 1
        else:
            return num + self.sum(num-1)
        
num = 123
object = Solution()
print(object.sum(num))  

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''
  
        
