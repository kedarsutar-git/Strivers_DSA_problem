class Solution:
    def BinaryToDecimal(self,n:str) ->str:
        Sum = 0
        power = 0
        for i in range(len(n)-1,-1,-1):
            Sum += int(n[i])*(2**power)

            power +=1
        return Sum

n = "111010111"
object = Solution()
print(object.BinaryToDecimal(n))

