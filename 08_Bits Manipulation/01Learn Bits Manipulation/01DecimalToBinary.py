class Solution:
    def DecimalToBinary(self,n:int) ->str:
        res = ""

        while(n>0):
            if(n%2==1):
                res +="1"

            else:
                res +="0"
            n = n//2

            
        return res[::-1]

n = 234
object =Solution()
print(object.DecimalToBinary(n))      

'''
Time Complexity:O(logn)
Space Compexity:O(logn)

'''