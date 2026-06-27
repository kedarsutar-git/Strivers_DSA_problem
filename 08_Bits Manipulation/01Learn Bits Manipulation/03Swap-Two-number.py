# using temp variable 

class Solution:
    def swapnumber(self,a:int,b:int):
        temp = a
        a = b
        b = temp

        return a,b
    
object = Solution()
print(object.swapnumber(12,23)) 
'''
Time Complexity:O(1)
Space Comepexity:O(1)

'''   

# optimal (using XOR operator)
class Solution:
    def Swapnumber(self,a:int,b:int):
        a = a^b
        b = a^b
        a = a^b

        return a,b

object = Solution()
print(object.Swapnumber(2,3))

'''
Time Complexity:O(1)
Space Complexity:O(1)
'''
